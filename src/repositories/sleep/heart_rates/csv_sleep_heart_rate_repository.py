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
from repositories import CsvBaseRepository
from common.config import Config
from utils.helper import json_load

CONFIG = Config().config
PATH_CSV = CONFIG["CSV_SLEEP"]["HEART_RATE"]
PATH_KEYS = CONFIG["KEYS_SLEEP"]["HEART_RATE"]


@dataclass
class CsvSleepHeartRateRepository(CsvBaseRepository):
    """csv sleep heart rate repository """
    path: str = field(init=False, default=PATH_CSV)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
