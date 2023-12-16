"""test csv sleep repository"""
#########################################################
# Builtin packages
#########################################################
import csv
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.sleeps import CsvSleepRepository


class TestCsvSleepRepository(object):
    """test csv sleep repo"""

    def test_all(self):
        """test all"""
        csv_path = "tests/src/csv/sleep/sleep.csv"

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            expected_data = [row for row in reader]

        obj = CsvSleepRepository()
        obj.path = csv_path
        actual = obj.all()

        assert actual == expected_data
