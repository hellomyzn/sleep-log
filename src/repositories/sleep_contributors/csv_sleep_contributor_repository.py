"""csv sleep contributor repository"""
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
PATH_CONTRIBUTORS = CONFIG["CSV_SLEEP"]["CONTRIBUTORS"]
PATH_KEYS_CONTRIBUTORS = CONFIG["KEYS_SLEEP"]["CONTRIBUTORS"]


@dataclass
class CsvSleepContributorsContributor(CsvBaseRepository):
    """csv sleep contributors repository """
    keys = json_load(PATH_KEYS_CONTRIBUTORS)["keys"]
    path: str = field(init=False, default=PATH_CONTRIBUTORS)
