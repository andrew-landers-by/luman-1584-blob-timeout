import logging
import sys

LOGGING_LEVEL = logging.INFO

def set_logging_config():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=LOGGING_LEVEL,
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )


set_logging_config()
