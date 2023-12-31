"""gss sleep heart rate repository"""
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
SHEET_NAME = CONFIG["GSS_SHEET_NAME"]["HEART_RATE"]
PATH_KEYS = CONFIG["KEYS_SLEEP"]["HEART_RATE"]


@dataclass
class GssSleepHeartRateRepository(GssBaseRepository):
    """gss sleep heart rate repository """
    sheet: str = field(init=False, default=SHEET_NAME)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
