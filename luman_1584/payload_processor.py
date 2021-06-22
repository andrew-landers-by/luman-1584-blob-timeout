"""
Process concurrent batches of payloads for Ocean PTA.
Two options:
- Run a set number of concurrent requests
- Run continuously until the process is killed
"""
import asyncio
import aiohttp
import json
import logging
import os
import random
from typing import Any, Dict, Iterable, List, Tuple, Union
from . import configs, ConfigKeys
from .payload_generator import PayloadGenerator
from .timing import TimingStats

RUN_PARAMS = configs.get(ConfigKeys.RUN_PARAMS)
RNG_SEED = 6789


class PayloadProcessor(object):
    """
    Sends batches of requests (asynchronously) to the Ocean PTA service.
    """
    randomize_routes: bool = RUN_PARAMS.get(ConfigKeys.RANDOMIZE_ROUTES)
    num_of_batches: int = RUN_PARAMS.get(ConfigKeys.NUM_OF_BATCHES)
    concurrent_payloads: int = RUN_PARAMS.get(ConfigKeys.CONCURRENT_PAYLOADS)
    items_per_payload: int = RUN_PARAMS.get(ConfigKeys.ITEMS_PER_PAYLOAD)

    def __init__(self, seed: int = None):

        self.logger = logging.getLogger(f"{__file__}")
        self.timer = TimingStats(verbose=True)
        self.batches_started = 0
        self.batches_completed = 0

        random.seed(seed) if seed else random.seed(RNG_SEED)

        self.payload_generator = PayloadGenerator(self.randomize_routes)

        if is_local := configs.get(ConfigKeys.IS_LOCAL_RUN):
            self.url = os.environ.get(ConfigKeys.LOCAL_URL_ENV_VAR)
        else:
            self.url = os.environ.get(ConfigKeys.DEV_URL_ENV_VAR)

    def process(self):
        """Continuous or limited batches, see config.yaml"""
        if RUN_PARAMS.get(ConfigKeys.RUN_CONTINUOUS):
            self.process_continuously()
        else:
            n = self.num_of_batches
            self.process_a_sequence_of_batches(n)

    def process_continuously(self):
        """Run a non-ending loop of concurrent batches"""
        while True:
            self.process_batch()

    def process_a_sequence_of_batches(self, n: int):
        """Run a pre-defined number of concurrent batches"""
        for idx in range(n):
            self.process_batch()

    def process_batch(self):
        """
        Process a batch of concurrent payloads
        """
        n_jobs, job_size = self.concurrent_payloads, self.items_per_payload
        message = f"Attempting to process {n_jobs} payloads of {job_size} predictions in each one."
        self.logger.info(message)
        jobs = self.fetch_concurrent_jobs()
        self.batches_started += 1

        with self.timer.scope("PROCESS A BATCH OF CONCURRENT JOBS"):
            asyncio.run(self.bulk_process_payloads(jobs))

        self.batches_completed += 1
        count = self.batches_completed
        message = f"Completed a set of concurrent batches. {count} batches are complete."
        self.logger.info(message)
    
    def fetch_concurrent_jobs(self) -> List:
        """Fetch a new batch of requests"""
        return [
            self.payload_generator.batch_payload(size=self.items_per_payload)
            for _ in range(self.concurrent_payloads)
        ]

    async def bulk_process_payloads(self, payloads: Iterable[Union[Dict, List]]):
        """
        Concurrently process the inputs given in 'payloads'
        """
        try:
            async with aiohttp.ClientSession() as session:
                tasks = []
                for payload in payloads:
                    tasks.append(self.process_payload(payload=payload, session=session))

                self.logger.debug(f"Running {len(tasks)} concurrent requests as coroutines")
                await asyncio.gather(*tasks)
        except Exception as e:
            message = f"An unexpected error occurred while processing the coroutines. Exception: {e}"
            self.logger.exception(e)
            raise Exception(e)

    async def process_payload(self,
                              payload: Union[Dict, List],
                              session: aiohttp.ClientSession):
        """
        Process a single coroutine (that is, get the response for 1 payload)
        """
        try:
            async with self.timer.async_scope("PROCESS ONE REQUEST"):

                headers = {
                    'x-functions-key': os.environ.get(ConfigKeys.API_KEY),
                    'content-type': 'application/json'
                }
                response = await session.post(
                    self.url,
                    headers=headers,
                    data=json.dumps(payload)
                )
                self.logger.debug(f"Completed a call to the function app with status code [{response.status}].")

                if response.status == 200:
                    res_json = await response.json()
                    self.logger.debug(f"Successful result: {json.dumps(res_json)}")
                else:
                    message = f"BAD RESPONSE: {response}"
                    self.logger.error(message)

        except aiohttp.ContentTypeError as ce:
            message = f"ContentTypeError occurred with input payload {json.dumps(payload)} response {response}: {ce}"
            print(f"Status: {response.status}")
            self.logger.exception(message)
        except Exception as e:
            message = f"Unexpected error occurred: {e}"
            self.logger.exception(message)
