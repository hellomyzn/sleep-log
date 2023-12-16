"""test csv sleep hrv repository"""
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
from repositories.sleep_heart_rates import CsvSleepHeartRateRepository
from common.config import Config

CONFIG = Config().config


class TestCsvSleepHrvRepository(object):
    """test csv sleep heart rate repo"""

    PATH = CONFIG["TEST_CSV_SLEEP"]["HRV"]

    def test_all(self):
        """test all"""
        csv_path = self.PATH

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            expected_data = [row for row in reader]

        obj = CsvSleepHeartRateRepository()
        obj.path = csv_path
        actual = obj.all()

        assert actual == expected_data
