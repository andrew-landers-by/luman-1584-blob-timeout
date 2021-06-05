"""
This script attempts to reproduce a failure
where heavy request traffic eventually causes the
blob downloading process to hang for up to 30 min
"""
import logging
from luman_1584 import Processor

logger = logging.getLogger(__file__)

if __name__ == "__main__":
    try:
        logger.info("Attempting to reproduce the failure")
        processor = Processor()
        processor.run()
    except Exception as e:
        logger.error(f"ERROR: {e}")
