"""csv sleep readiness repository"""
#########################################################
# Builtin packages
#########################################################
import csv
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
from common.log import (
    debug,
    info
)
from utils.helper import json_load

CONFIG = Config().config
PATH_READINESS = CONFIG["CSV_SLEEP"]["READINESS"]
PATH_KEYS_READINESS = CONFIG["KEYS_SLEEP"]["READINESS"]


@dataclass
class CsvSleepReadinessRepository(CsvRepoInterface):
    """csv sleep readiness repository """
    keys = json_load(PATH_KEYS_READINESS)["keys"]
    path: str = field(init=False, default=PATH_READINESS)

    def find_by_id(self, _id: int):
        pass

    def add(self, data: dict) -> None:
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        info("start to add sleep log into csv. data type: {0}, data num",
             data["data_type"], len(data["data"]))

        self.check_file(self.path)

        with open(self.path, 'a', encoding="utf-8", newline="") as f:
            for d in data["data"]:
                writer = csv.DictWriter(f, fieldnames=self.keys)
                writer.writerow(d)
                debug("added data into csv: {0}", d)
        info("finish to add sleep log into csv")
        return None

    def delete_by_id(self, _id: int):
        pass
