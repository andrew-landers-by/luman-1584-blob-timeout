"""
This attempts to reproduce a failure where large/frequent requests
cause the blob download to hang for 30 minutes. The presumed fix is to
implement a custom time-out (up to 30 seconds) for each blob service action.
"""
import asyncio
import aiohttp
import json
import logging
import os
import random
from typing import Dict, Iterable, List, Union
from .config import configs, ConfigKeys
from .request_generator import RequestGenerator

RNG_SEED = 4567

class Processor(object):
    """

    """
    def __init__(self):
        self.logger = logging.getLogger(f"{__file__}")

        random.seed(RNG_SEED)

        if is_local := configs.get(ConfigKeys.IS_LOCAL_RUN):
            self.url = os.environ.get(ConfigKeys.LOCAL_URL_ENV_VAR)
        else:
            self.url = os.environ.get(ConfigKeys.DEV_URL_ENV_VAR)

        # Load settings from configs:
        params = configs.get(ConfigKeys.RUN_PARAMS)
        self.randomize_routes: bool = params.get(ConfigKeys.RANDOMIZE_ROUTES)
        self.num_of_batches: int = params.get(ConfigKeys.NUM_OF_BATCHES)
        self.concurrent_payloads: int = params.get(ConfigKeys.CONCURRENT_PAYLOADS)
        self.items_per_payload: int = params.get(ConfigKeys.ITEMS_PER_PAYLOAD)

    def run(self):
        request_generator = RequestGenerator(self.randomize_routes)
        for idx, _ in enumerate(range(self.num_of_batches)):
            concurrent_payloads = [
                request_generator.batch_payload(size=self.items_per_payload)
                for _ in range(self.concurrent_payloads)
            ]
            self.logger.info(
                f"Fetched a batch of {len(concurrent_payloads)} payloads containing {len(concurrent_payloads[0])} payloads each."  # noqa
            )
            asyncio.run(self.bulk_process_requests(concurrent_payloads))

            self.logger.info(
                f"[Completed a set of concurrent batches. {idx + 1} of {self.num_of_batches} are complete]."
            )

    async def bulk_process_requests(self, payloads: Iterable[Union[Dict, List]]) -> None:
        """
        Concurrently process the input payloads
        """
        async with aiohttp.ClientSession() as session:
            tasks = []
            for payload in payloads:
                tasks.append(self.process_request(payload=payload, session=session))

            self.logger.debug(f"Running {len(tasks)} coroutines")
            try:
                await asyncio.gather(*tasks)
            except Exception as e:
                message = f"An unexpected error occurred while processing the coroutines. Exception: {e}"
                self.logger.exception(e)
                raise type(e)(message)

    async def process_request(self, payload: Union[Dict, List],
                              session: aiohttp.ClientSession) -> None:
        """
        Process a single coroutine (that is, get the response for 1 payload)
        """
        try:
            response = await session.post(self.url, data=json.dumps(payload))
        except Exception as e:
            message = f"Unexpected error occurred: {e}"
            self.logger.exception(message)
            raise Exception(message)
