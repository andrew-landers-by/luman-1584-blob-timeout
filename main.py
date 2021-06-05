"""
This script attempts to reproduce a failure
where heavy request traffic eventually causes the
blob downloading process to hang for up to 30 min
"""
import logging
from luman_1584 import reproduce_failure

logger = logging.getLogger(__file__)

if __name__ == "__main__":
    try:
        logging.info("Attempting to reproduce the failure")
        reproduce_failure()
    except Exception as e:
        logger.error(f"ERROR: {e}")
