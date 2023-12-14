"""csv sleep repository"""

#########################################################
# Builtin packages
#########################################################
import csv

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
    warn,
    debug,
    info
)

CONFIG = Config().config


class CsvSleepRepository(CsvRepoInterface):
    """csv sleep repository """
    # TODO: make conf and import them
    PATH_SLEEP = CONFIG["CSV_SLEEP"]["SLEEP"]
    PATH_CONTRIBUTORS = CONFIG["CSV_SLEEP"]["CONTRIBUTORS"]
    PATH_HEART_RATE = CONFIG["CSV_SLEEP"]["HEART_RATE"]
    PATH_HRV = CONFIG["CSV_SLEEP"]["HRV"]
    PATH_READINESS = CONFIG["CSV_SLEEP"]["READINESS"]

    KEYS_SLEEP = ['id', 'average_breath', 'average_breath_variation', 'average_heart_rate', 'average_hrv', 'awake_time',
                  'bedtime_end', 'bedtime_start', 'contributors', 'day', 'deep_sleep_duration', 'efficiency', 'got_ups',
                  'heart_rate', 'hrv', 'latency', 'light_sleep_duration', 'lowest_heart_rate',
                  'lowest_heart_rate_time_offset', 'movement_30_sec', 'period', 'readiness', 'readiness_score_delta',
                  'rem_sleep_duration', 'restless_periods', 'score', 'segment_state', 'sleep_algorithm_version',
                  'sleep_midpoint', 'sleep_score_delta', 'time_in_bed', 'total_sleep_duration', 'type', 'wake_ups',
                  'sleep_phase_5_min', 'restless', 'timezone', 'bedtime_start_delta', 'bedtime_end_delta',
                  'midpoint_at_delta']

    KEYS_CONTRIBUTORS = ['id', 'sleep_id', 'deep_sleep', 'efficiency', 'latency', 'rem_sleep',
                         'restfulness', 'timing', 'total_sleep']
    KEYS_HEART_RATE = ['id', 'sleep_id', 'interval', 'items', 'timestamp']
    KEYS_HRV = ['id', 'sleep_id', 'interval', 'items', 'timestamp']
    KEYS_READINESS = ['id', 'sleep_id', 'score', 'activity_balance', 'body_temperature', 'hrv_balance', 'previous_day_activity',
                      'previous_night', 'recovery_index', 'resting_heart_rate', 'sleep_balance', 'sleep_regularity', 'temperature_trend_deviation', 'temperature_deviation']

    DATA_TYPE_SLEEP = "sleep"
    DATA_TYPE_CONTRIBUTORS = "contributors"
    DATA_TYPE_HEART_RATE = "heart_rate"
    DATA_TYPE_HRV = "hrv"
    DATA_TYPE_READINESS = "readiness"

    def __init__(self):
        super().__init__()
        self.path = None
        self.keys = None

    def all(self, data_type: str) -> list:
        """_summary_

        Args:
            data_type (str): _description_

        Returns:
            list: _description_
        """

        self.get_path_by_data_type(data_type)
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
        self.get_path_by_data_type(data["data_type"])

        self.check_file(self.path)

        with open(self.path, 'a', encoding="utf-8", newline="") as f:
            for d in data["data"]:
                writer = csv.DictWriter(f, fieldnames=self.keys)
                writer.writerow(d)
                debug("added data into csv: {0}", d)
        info("finish to add sleep log into csv")
        return None

    def get_path_by_data_type(self, data_type: str) -> None:
        """_summary_

        Args:
            data_type (str): _description_

        Returns:
            str: _description_
        """
        if data_type == self.DATA_TYPE_SLEEP:
            self.path = self.PATH_SLEEP
            self.keys = self.KEYS_SLEEP
        elif data_type == self.DATA_TYPE_CONTRIBUTORS:
            self.path = self.PATH_CONTRIBUTORS
            self.keys = self.KEYS_CONTRIBUTORS
        elif data_type == self.DATA_TYPE_HEART_RATE:
            self.path = self.PATH_HEART_RATE
            self.keys = self.KEYS_HEART_RATE
        elif data_type == self.DATA_TYPE_HRV:
            self.path = self.PATH_HRV
            self.keys = self.KEYS_HRV
        elif data_type == self.DATA_TYPE_READINESS:
            self.path = self.PATH_READINESS
            self.keys = self.KEYS_READINESS
        else:
            warn("nothing to match data type")

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

        self.get_path_by_data_type(data_type)
        info("start to tail")

        with open(self.path, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tail_lines = []
            for r in reader:
                tail_lines.append(r)

        info("finish to tail")
        return tail_lines[-num:]
