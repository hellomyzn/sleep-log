"""test csv sleep repository"""
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
from repositories import CsvBaseRepository
from common.config import Config

CONFIG = Config().config


class TestCsvSleepRepository(object):
    """test csv sleep repo"""

    PATH = CONFIG["TEST"]["CSV_SLEEP"]

    def test_all(self):
        """test all"""
        csv_path = self.PATH

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            expected_data = [row for row in reader]

        obj = CsvBaseRepository()
        obj.path = csv_path
        actual = obj.all()

        assert actual == expected_data
