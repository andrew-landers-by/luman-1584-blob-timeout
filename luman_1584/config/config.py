import logging
import os
import yaml

CONFIG_FILE_NAME = "config.yaml"

logger = logging.getLogger(__file__)

class Keys:

    # For environment settings:
    ENVIRONMENT = "ENVIRONMENT"
    LOCAL_URL_ENV_VAR = "LOCAL_URL"
    DEV_URL_ENV_VAR = "DEV_URL"
    MODEL_STORE_PATH_ENV_VAR = "MODEL_STORE_PATH"

    LOGGING_LEVEL = "LOGGING_LEVEL"

    # For run parameters
    RUN_PARAMS = "RUN_PARAMS"
    IS_LOCAL_RUN = "IS_LOCAL_RUN"
    RUN_CONTINUOUS = "RUN_CONTINUOUS"
    RANDOMIZE_ROUTES = "RANDOMIZE_ROUTES"
    NUM_OF_BATCHES = "NUM_OF_BATCHES"
    CONCURRENT_PAYLOADS = "CONCURRENT_PAYLOADS"
    ITEMS_PER_PAYLOAD = "ITEMS_PER_PAYLOAD"

def load_config() -> dict:
    """
    Load configurations for a YAML file
    """
    yaml_file_path = os.path.join(
        os.path.dirname(__file__), CONFIG_FILE_NAME
    )
    try:
        with open(yaml_file_path, 'r') as yaml_file:
            config: dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
            return config
    except yaml.YAMLError as ye:
        message = f"Unsuccessful in loading data from YAML: {ye}"
        logger.exception(message)
        raise yaml.YAMLError(message)
