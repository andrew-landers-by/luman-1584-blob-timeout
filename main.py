"""
This script generates and runs batches of concurrent requests
to the Ocean PTA service (currently, local or dev)
"""
from luman_1584 import PayloadProcessor, summarize_run_params
import logging

logger = logging.getLogger(__file__)

if __name__ == "__main__":
    try:
        message = f"Sending requests to the Ocean_PTA_Service with these local settings: {summarize_run_params()}"
        logger.info(message)
        processor = PayloadProcessor()
        with processor.timer.scope("MAIN PROGRAM"):
            processor.process()

    except Exception as e:
        logger.error(f"ERROR: {e}")
