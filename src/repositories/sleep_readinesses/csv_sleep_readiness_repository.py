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

CONFIG = Config().config


@dataclass
class CsvSleepReadinessRepository(CsvRepoInterface):
    """csv sleep readiness repository """
    # TODO: make conf and import them
    PATH_READINESS = CONFIG["CSV_SLEEP"]["READINESS"]
    KEYS_READINESS = ['id', 'sleep_id', 'score', 'activity_balance', 'body_temperature',
                      'hrv_balance', 'previous_day_activity', 'previous_night',
                      'recovery_index', 'resting_heart_rate', 'sleep_balance',
                      'sleep_regularity', 'temperature_trend_deviation', 'temperature_deviation']

    path: str = field(init=False, default=PATH_READINESS)

    def all(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """

        info("start to get all csv data.")

        self.check_file(self.path)

        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        info(f"finish to get all data from csv. all csv data num: {len(data)}")
        return data

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

    def tail(self, data_type: str, num: int) -> list:
        """_summary_

        Args:
            data_type (str): _description_
            num (int): _description_

        Returns:
            list: _description_
        """

        info("start to tail")

        with open(self.path, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tail_lines = []
            for r in reader:
                tail_lines.append(r)

        info("finish to tail")
        return tail_lines[-num:]
