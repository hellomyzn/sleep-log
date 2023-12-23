"""gss sleep contributors repository"""
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
SHEET_NAME = CONFIG["GSS_SHEET_NAME"]["CONTRIBUTORS"]
PATH_KEYS = CONFIG["KEYS_SLEEP"]["CONTRIBUTORS"]


@dataclass
class GssSleepContributorRepository(GssBaseRepository):
    """gss sleep contributor repository """
    sheet: str = field(init=False, default=SHEET_NAME)
    keys: list = field(init=False, default_factory=lambda: json_load(PATH_KEYS)["keys"])
