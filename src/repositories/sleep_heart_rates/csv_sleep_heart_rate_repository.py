"""csv sleep heart rate repository"""
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
from repositories.interfaces import CsvRepoInterface
from common.config import Config
from utils.helper import json_load

CONFIG = Config().config
PATH_HEART_RATE = CONFIG["CSV_SLEEP"]["HEART_RATE"]
PATH_KEYS_HEART_RATE = CONFIG["KEYS_SLEEP"]["HEART_RATE"]


@dataclass
class CsvSleepHeartRateRepository(CsvRepoInterface):
    """csv sleep heart rate repository """
    path: str = field(init=False, default=PATH_HEART_RATE)
    keys = json_load(PATH_KEYS_HEART_RATE)["keys"]

    def find_by_id(self, _id: int):
        pass

    def delete_by_id(self, _id: int):
        pass
