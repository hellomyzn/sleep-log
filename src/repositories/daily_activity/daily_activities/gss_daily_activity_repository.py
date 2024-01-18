"""gss daily activity repository"""
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
from repositories import GssBaseRepository
from common.config import Config
from utils.helper import json_load

CONFIG = Config().config
SHEET_NAME = CONFIG["GSS_SHEET_NAME"]["DAILY_ACTIVITY"]
PATH_KEYS = CONFIG["KEYS_DAILY_ACTIVITY"]["DAILY_ACTIVITY"]


@dataclass
class GssDailyActivityRepository(GssBaseRepository):
    """gss daily activity repository """
    sheet: str = field(init=False, default=SHEET_NAME)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
