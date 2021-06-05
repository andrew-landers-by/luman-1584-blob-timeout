"""
This attempts to reproduce a failure where large/frequent requests
cause the blob download to hang for 30 minutes. The presumed fix is to
implement a custom time-out (up to 30 seconds) for each blob service action.
"""
import asyncio
import aiohttp
import json
import logging
import random
from typing import Dict, Iterable, List, Union
from .constants import Constants
from .logging import set_logging_config
from .request_generator import RequestGenerator

set_logging_config()
logger = logging.getLogger(f"{__file__}")

URL = Constants.OCEAN_PTA_LOCAL_URL
RANDOMIZE_ROUTES = True
BATCHES = 5
CONCURRENT_PAYLOADS = 10
ITEMS_PER_PAYLOAD = 25

def reproduce_failure():
    """
    """
    random.seed(4567)

    request_generator = RequestGenerator(RANDOMIZE_ROUTES)
    for idx, _ in enumerate(range(BATCHES)):
        concurrent_payloads = [
            request_generator.batch_payload(size=ITEMS_PER_PAYLOAD)
            for _ in range(CONCURRENT_PAYLOADS)
        ]
        message = f"Fetched a batch of {len(concurrent_payloads)} payloads containing {len(concurrent_payloads[0])} payloads each."  # noqa
        logger.info(message)

        asyncio.run(bulk_process_ocean_pta_requests(concurrent_payloads))
        logger.info(f"[Completed a set of concurrent batches. {idx+1} of {BATCHES} are completed].")


async def bulk_process_ocean_pta_requests(payloads: Iterable[Union[Dict, List]]) -> None:
    """
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for payload in payloads:
            tasks.append(
                process_payload(payload=payload, session=session)
            )
        await asyncio.gather(*tasks)


async def process_payload(payload: Union[Dict, List],
                          session: aiohttp.ClientSession):
    """
    """
    response = await session.post(URL, data=json.dumps(payload))
    response_body = await response.json()
    logger.debug(f"{json.dumps(response_body)}")
