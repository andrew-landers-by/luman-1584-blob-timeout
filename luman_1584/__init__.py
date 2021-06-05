from .config import configs, ConfigKeys
from .helpers import load_env_vars
from .logging import set_logging_config
from .processor import Processor

set_logging_config()
load_env_vars()
