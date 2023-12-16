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
from repositories import CsvBaseRepository
from common.config import Config
from utils.helper import json_load

CONFIG = Config().config
PATH_HRV = CONFIG["CSV_SLEEP"]["HRV"]
PATH_KEYS_HRV = CONFIG["KEYS_SLEEP"]["HRV"]


@dataclass
class CsvSleepHrvRepository(CsvBaseRepository):
    """csv sleep hrv repository """
    keys = json_load(PATH_KEYS_HRV)["keys"]
    path: str = field(init=False, default=PATH_HRV)
