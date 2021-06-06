import logging
import sys
from . import configs, ConfigKeys

logger = logging.getLogger(__name__)

def get_logging_level() -> int:
    """
    Read in the logging level from configs
    """
    valid_choices = {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}
    level: str = configs.get(ConfigKeys.LOGGING_LEVEL)
    if level:
        upper_level: str = level.upper()

        if upper_level == "CRITICAL":
            return logging.CRITICAL
        elif upper_level == "ERROR":
            return logging.ERROR
        elif upper_level == "WARNING":
            return logging.WARNING
        elif upper_level == "INFO":
            return logging.INFO
        elif upper_level == "DEBUG":
            return logging.DEBUG
        else:
            message = f"Invalid logging level {level} was read in from config.yaml; expected one of {valid_choices}"
    else:
        message = f"Failed to read in a logging level from config.yaml. Check whether it is blank. Expected one of {valid_choices}"  # noqa

    if message:
        logger.error(message)
        raise ValueError(message)

def set_logging_config():
    """Set logging level. We get this from configs."""
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=get_logging_level(),
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )


set_logging_config()
