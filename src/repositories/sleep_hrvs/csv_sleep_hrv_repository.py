"""csv sleep hrv repository"""
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
PATH_HRV = CONFIG["CSV_SLEEP"]["HRV"]
PATH_KEYS_HRV = CONFIG["KEYS_SLEEP"]["HRV"]


@dataclass
class CsvSleepHrvRepository(CsvRepoInterface):
    """csv sleep hrv repository """
    keys = json_load(PATH_KEYS_HRV)["keys"]
    path: str = field(init=False, default=PATH_HRV)

    def find_by_id(self, id_: int):
        pass

    def delete_by_id(self, id_: int):
        pass
