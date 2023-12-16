"""csv sleep readiness repository"""
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
PATH_READINESS = CONFIG["CSV_SLEEP"]["READINESS"]
PATH_KEYS_READINESS = CONFIG["KEYS_SLEEP"]["READINESS"]


@dataclass
class CsvSleepReadinessRepository(CsvRepoInterface):
    """csv sleep readiness repository """
    keys = json_load(PATH_KEYS_READINESS)["keys"]
    path: str = field(init=False, default=PATH_READINESS)

    def find_by_id(self, id_: int):
        pass

    def delete_by_id(self, id_: int):
        pass
