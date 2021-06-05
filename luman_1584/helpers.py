"""
Helper functions
"""
import os
import random
import re
from typing import Iterable, List, Optional, Tuple
from . import configs, ConfigKeys
from .constants import Constants
from ._regex import Regex


def load_env_vars() -> None:
    """
    Read in (and set) environment variables
    """
    env_vars = configs.get(ConfigKeys.ENVIRONMENT)
    for key, value in env_vars.items():
        assert isinstance(value, str)
        os.environ[key] = value
        print(f"{key}: {os.environ.get(key)}")

def modeled_od_pairs() -> List[Tuple[str, str]]:
    """
    Extract the set of OD pairs that have dedicated
    ML models. We look at the contents of the model_store,
    directory and exploit the naming convention.
    """
    locode_str_length = Constants.VALID_PORT_LOCODE_STRING_LENGTH
    pairs = []
    path_to_model_store = os.environ.get(ConfigKeys.MODEL_STORE_PATH_ENV_VAR)
    for filename in os.listdir(path_to_model_store):
        match = re.search(Regex.CONCATENATED_OD_PAIR, filename)
        if match:
            source_code = match.group(2)[:locode_str_length]
            destination_code = match.group(2)[locode_str_length:]
            pairs.append((source_code, destination_code))
    return pairs


def random_od_pairs(pairs: Optional[Iterable[Tuple[str, str]]] = None,
                    n: int = 1
                    ) -> List[Tuple[str, str]]:
    """
    Returns a randomized list of O-D paris, sampled
    from the population (with replacement)
    """
    if not pairs:
        pairs = modeled_od_pairs()

    return random.choices(population=pairs, k=n)
