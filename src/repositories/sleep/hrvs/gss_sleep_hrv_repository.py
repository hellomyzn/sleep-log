"""gss sleep hrv repository"""
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
SHEET_NAME = CONFIG["GSS_SHEET_NAME"]["HRV"]
PATH_KEYS = CONFIG["KEYS_SLEEP"]["HRV"]


@dataclass
class GssSleepHrvRepository(GssBaseRepository):
    """gss sleep repository """
    sheet: str = field(init=False, default=SHEET_NAME)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
