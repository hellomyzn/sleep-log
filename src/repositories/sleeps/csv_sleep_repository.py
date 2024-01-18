"""csv sleep repository"""
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
from common.log import info

CONFIG = Config().config
PATH_CSV_SLEEP = CONFIG["CSV_PATH"]["SLEEP"]
PATH_CSV_CONTRIBUTORS = CONFIG["CSV_PATH"]["SLEEP_CONTRIBUTORS"]
PATH_CSV_HEART_RATE = CONFIG["CSV_PATH"]["SLEEP_HEART_RATE"]
PATH_CSV_HEART_RATE_ITEMS = CONFIG["CSV_PATH"]["SLEEP_HEART_RATE_ITEMS"]
PATH_CSV_HRV = CONFIG["CSV_PATH"]["SLEEP_HRV"]
PATH_CSV_HRV_ITEMS = CONFIG["CSV_PATH"]["SLEEP_HRV_ITEMS"]
PATH_CSV_READINESS = CONFIG["CSV_PATH"]["SLEEP_READINESS"]
PATH_CSV_MOVEMENT_30_SEC = CONFIG["CSV_PATH"]["SLEEP_MOVEMENT_30_SEC"]
PATH_CSV_SLEEP_PHASE_5_MIN = CONFIG["CSV_PATH"]["SLEEP_PHASE_5_MIN"]

PATH_COLUMNS_SLEEP = CONFIG["COLUMN_PATH"]["SLEEP"]
PATH_COLUMNS_CONTRIBUTORS = CONFIG["COLUMN_PATH"]["SLEEP_CONTRIBUTORS"]
PATH_COLUMNS_HEART_RATE = CONFIG["COLUMN_PATH"]["SLEEP_HEART_RATE"]
PATH_COLUMNS_HEART_RATE_ITEMS = CONFIG["COLUMN_PATH"]["SLEEP_HEART_RATE_ITEMS"]
PATH_COLUMNS_HRV = CONFIG["COLUMN_PATH"]["SLEEP_HRV"]
PATH_COLUMNS_HRV_ITEMS = CONFIG["COLUMN_PATH"]["SLEEP_HRV_ITEMS"]
PATH_COLUMNS_READINESS = CONFIG["COLUMN_PATH"]["SLEEP_READINESS"]
PATH_COLUMNS_MOVEMENT_30_SEC = CONFIG["COLUMN_PATH"]["SLEEP_MOVEMENT_30_SEC"]
PATH_COLUMNS_SLEEP_PHASE_5_MIN = CONFIG["COLUMN_PATH"]["SLEEP_PHASE_5_MIN"]


@dataclass
class CsvSleepRepository(CsvBaseRepository):
    """csv sleep repository """
    path_sleep: str = field(init=False, default=PATH_CSV_SLEEP)
    path_contributors: str = field(init=False, default=PATH_CSV_CONTRIBUTORS)
    path_heart_rate: str = field(init=False, default=PATH_CSV_HEART_RATE)
    path_heart_rate_items: str = field(init=False, default=PATH_CSV_HEART_RATE_ITEMS)
    path_hrv: str = field(init=False, default=PATH_CSV_HRV)
    path_hrv_items: str = field(init=False, default=PATH_CSV_HRV_ITEMS)
    path_readiness: str = field(init=False, default=PATH_CSV_READINESS)
    path_movement_30_sec: str = field(init=False, default=PATH_CSV_MOVEMENT_30_SEC)
    path_sleep_phase_5_min: str = field(init=False, default=PATH_CSV_SLEEP_PHASE_5_MIN)

    columns_sleep: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_SLEEP)["keys"])
    columns_contributors: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_CONTRIBUTORS)["keys"])
    columns_heart_rate: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_HEART_RATE)["keys"])
    columns_heart_rate_items: list = field(
        init=False, default_factory=lambda: json_load(PATH_COLUMNS_HEART_RATE_ITEMS)["keys"])
    columns_hrv: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_HRV)["keys"])
    columns_hrv_items: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_HRV_ITEMS)["keys"])
    columns_readiness: list = field(init=False, default_factory=lambda: json_load(PATH_COLUMNS_READINESS)["keys"])
    columns_movement_30_sec: list = field(
        init=False, default_factory=lambda: json_load(PATH_COLUMNS_MOVEMENT_30_SEC)["keys"])
    columns_sleep_phase_5_min: list = field(
        init=False, default_factory=lambda: json_load(PATH_COLUMNS_SLEEP_PHASE_5_MIN)["keys"])

    key_sleep: str = field(init=False, default="sleep")
    key_contributors: str = field(init=False, default="contributors")
    key_heart_rate: str = field(init=False, default="heart_rate")
    key_heart_rate_items: str = field(init=False, default="heart_rate_items")
    key_hrv: str = field(init=False, default="hrv")
    key_hrv_items: str = field(init=False, default="hrv_items")
    key_readiness: str = field(init=False, default="readiness")
    key_movement_30_sec: str = field(init=False, default="movement_30_sec")
    key_sleep_phase_5_min: str = field(init=False, default="sleep_phase_5_min")

    def __post_init__(self):
        self.paths = {
            self.key_sleep:             self.path_sleep,
            self.key_contributors:      self.path_contributors,
            self.key_heart_rate:        self.path_heart_rate,
            self.key_heart_rate_items:  self.path_heart_rate_items,
            self.key_hrv:               self.path_hrv,
            self.key_hrv_items:         self.path_hrv_items,
            self.key_readiness:         self.path_readiness,
            self.key_movement_30_sec:   self.path_movement_30_sec,
            self.key_sleep_phase_5_min: self.path_sleep_phase_5_min}

        self.columns = {
            self.key_sleep:             self.columns_sleep,
            self.key_contributors:      self.columns_contributors,
            self.key_heart_rate:        self.columns_heart_rate,
            self.key_heart_rate_items:  self.columns_heart_rate_items,
            self.key_hrv:               self.columns_hrv,
            self.key_hrv_items:         self.columns_hrv_items,
            self.key_readiness:         self.columns_readiness,
            self.key_movement_30_sec:   self.columns_movement_30_sec,
            self.key_sleep_phase_5_min: self.columns_sleep_phase_5_min}

    def all_sleep_data(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """

        data = {}

        for k, p in self.paths.items():
            self.check_file(p, self.columns[k])
            data[k] = self.all(p)

        info("get all sleep csv data. data num. sleep: {0}, contributors: {1}, heart_rates: {2}, heart_rate_items: {3} hrvs: {4}, hrv_items: {5} readiness: {6}, movement_30_sec: {7}, sleep_phase_5_min: {8}",
             len(data[self.key_sleep]), len(data[self.key_contributors]), len(data[self.key_heart_rate]),
             len(data[self.key_heart_rate_items]), len(data[self.key_hrv]), len(data[self.key_hrv_items]),
             len(data[self.key_readiness]), len(data[self.key_movement_30_sec]), len(data[self.key_sleep_phase_5_min]))
        return data

    def add_sleep_data(self, data: dict) -> None:
        """_summary_
        """

        for k, p in self.paths.items():
            self.check_file(p, self.columns[k])
            self.add(data[k], self.columns[k], p)
