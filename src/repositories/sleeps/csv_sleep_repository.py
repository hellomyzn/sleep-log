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
    debug,
    info,
    warn
)


class CsvSleepRepository(CsvRepoInterface):
    """csv sleep repository """
    COLUMNS = ['average_breath', 'average_breath_variation', 'average_heart_rate', 'average_hrv', 'awake_time',
               'bedtime_end', 'bedtime_start', 'contributors', 'day', 'deep_sleep_duration', 'efficiency', 'got_ups',
               'heart_rate', 'hrv', 'latency', 'light_sleep_duration', 'lowest_heart_rate',
               'lowest_heart_rate_time_offset', 'movement_30_sec', 'period', 'readiness', 'readiness_score_delta',
               'rem_sleep_duration', 'restless_periods', 'score', 'segment_state', 'sleep_algorithm_version',
               'sleep_midpoint', 'sleep_score_delta', 'time_in_bed', 'total_sleep_duration', 'type', 'wake_ups',
               'sleep_phase_5_min', 'restless', 'timezone', 'bedtime_start_delta', 'bedtime_end_delta',
               'midpoint_at_delta']

    def __init__(self):
        super().__init__()
        self.config = Config().config
        self.sleep_path = self.config["CSV"]["SLEEP"]

    def all(self):
        pass

    def find_by_id(self, _id: int):
        pass

    def add(self, data: list) -> None:
        """add sleep log
        Returns:
            None: _description_
        """
        info("start to add sleep log into csv")

        if not os.path.isfile(self.path):
            pathlib.Path(self.path).touch()
            warn(f"create a csv file since there was not the file. path: {self.path}")

        if not self.has_header():
            self.write_header()

        with open(self.path, 'a', encoding="utf-8", newline="") as f:
            for d in data:
                writer = csv.DictWriter(f, fieldnames=self.COLUMNS)
                writer.writerow(d)
                info("added data into csv: {0}", d)
        info("finish to add sleep log into csv")
        return None

    def delete_by_id(self, _id: int):
        pass
