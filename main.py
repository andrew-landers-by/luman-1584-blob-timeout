"""
This script attempts to reproduce a failure
where heavy request traffic eventually causes the
blob downloading process to hang.
"""
import logging
from luman_1584 import PayloadProcessor

logger = logging.getLogger(__file__)

if __name__ == "__main__":
    try:
        logger.info("Attempting to reproduce the failure")
        processor = PayloadProcessor()
        with processor.timer.scope("MAIN PROGRAM"):
            processor.process()

    except Exception as e:
        logger.error(f"ERROR: {e}")
