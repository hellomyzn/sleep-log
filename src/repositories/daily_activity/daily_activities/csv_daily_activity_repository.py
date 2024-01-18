"""csv daily activity repository"""
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
PATH_CSV = CONFIG["CSV_DAILY_ACTIVITY"]["DAILY_ACTIVITY"]
PATH_KEYS = CONFIG["KEYS_DAILY_ACTIVITY"]["DAILY_ACTIVITY"]


@dataclass
class CsvDailyActivityRepository(CsvBaseRepository):
    """csv daily activity repository """
    path: str = field(init=False, default=PATH_CSV)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
