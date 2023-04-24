import sys
from typing import Dict

import yaml

from src.exception import CustomException


def read_bot_config() -> Dict:
    """
    This function reads a YAML configuration file for a specified bot type and returns the corresponding
    dictionary.

    Args:
      bot_type (str): a string representing the type of bot for which the configuration is being read.

    Returns:
      a dictionary containing the configuration settings for a specific type of bot, as specified by the
    `bot_type` parameter. The dictionary is obtained by reading the contents of a YAML file located at
    "config/bot_config.yaml". If an error occurs during the reading process, a `CustomException` is
    raised with the error message and the `sys` module.
    """
    try:
        with open("config/bot_config.yaml", "r") as f:
            dic = yaml.safe_load(f)

        return dic

    except Exception as e:
        raise CustomException(e, sys)
