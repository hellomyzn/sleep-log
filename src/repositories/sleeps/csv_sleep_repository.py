"""csv sleep repository"""
#########################################################
# Builtin packages
#########################################################
from dataclasses import dataclass, field

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories import CsvBaseRepository
from common.config import Config
from utils.helper import json_load

CONFIG = Config().config
PATH_SLEEP = CONFIG["CSV_SLEEP"]["SLEEP"]
PATH_KEYS_SLEEP = CONFIG["KEYS_SLEEP"]["SLEEP"]


@dataclass
class CsvSleepRepository(CsvBaseRepository):
    """csv sleep repository """
    keys = json_load(PATH_KEYS_SLEEP)["keys"]
    path: str = field(init=False, default=PATH_SLEEP)
