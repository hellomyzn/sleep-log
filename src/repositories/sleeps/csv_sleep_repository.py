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
from common.config import Config
from common.log import (
    info
)


class CsvSleepRepository(object):
    """csv sleep repository """

    def __init__(self):
        self.config = Config().config
        self.path = self.config["CSV"]["SLEEP"]
        return None

    def add(self, data: list) -> None:
        """add sleep log
        Returns:
            None: _description_
        """
        info("start to add sleep log into csv")
        with open(self.path, 'a', encoding="utf-8", newline='') as f:
            for d in data:
                writer = csv.writer(f)
                writer.writerow(d)
                info("added data into csv: {0}", d)
        info("finish to add sleep log into csv")
        return None
