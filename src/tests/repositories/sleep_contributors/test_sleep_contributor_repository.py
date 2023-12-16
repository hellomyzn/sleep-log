"""test csv sleep contributors repository"""
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
from repositories.sleep_contributors import CsvSleepContributorsContributor


class TestCsvSleepContributorsRepository(object):
    """test csv sleep repo"""

    def test_all(self):
        """test all"""
        csv_path = "tests/src/csv/sleep_contributors.csv"

        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            expected_data = [row for row in reader]

        obj = CsvSleepContributorsContributor()
        obj.path = csv_path
        actual = obj.all()

        assert actual == expected_data
