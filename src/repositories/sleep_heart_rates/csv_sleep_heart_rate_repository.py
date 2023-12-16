"""csv sleep heart rate repository"""
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
PATH_HEART_RATE = CONFIG["CSV_SLEEP"]["HEART_RATE"]
PATH_KEYS_HEART_RATE = CONFIG["KEYS_SLEEP"]["HEART_RATE"]


@dataclass
class CsvSleepHeartRateRepository(CsvRepoInterface):
    """csv sleep repository """
    path: str = field(init=False, default=PATH_HEART_RATE)
    keys = json_load(PATH_KEYS_HEART_RATE)["keys"]

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
