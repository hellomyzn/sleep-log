"""csv sleep repository"""
#########################################################
# Builtin packages
#########################################################
import csv
import dataclasses

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


@dataclasses.dataclass
class CsvSleepRepository(CsvRepoInterface):
    """csv sleep repository """
    # TODO: make conf and import them
    PATH_SLEEP = CONFIG["CSV_SLEEP"]["SLEEP"]

    KEYS_SLEEP = ['id', 'average_breath', 'average_breath_variation', 'average_heart_rate', 'average_hrv', 'awake_time',
                  'bedtime_end', 'bedtime_start', 'contributors', 'day', 'deep_sleep_duration', 'efficiency', 'got_ups',
                  'heart_rate', 'hrv', 'latency', 'light_sleep_duration', 'lowest_heart_rate',
                  'lowest_heart_rate_time_offset', 'movement_30_sec', 'period', 'readiness', 'readiness_score_delta',
                  'rem_sleep_duration', 'restless_periods', 'score', 'segment_state', 'sleep_algorithm_version',
                  'sleep_midpoint', 'sleep_score_delta', 'time_in_bed', 'total_sleep_duration', 'type', 'wake_ups',
                  'sleep_phase_5_min', 'restless', 'timezone', 'bedtime_start_delta', 'bedtime_end_delta',
                  'midpoint_at_delta']

    path: str = PATH_SLEEP

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
