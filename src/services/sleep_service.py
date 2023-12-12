"""sleep service"""
#########################################################
# Builtin packages
#########################################################
import json

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.interfaces import CsvRepoInterface
from utils.helper import fromisoformat_to_datetime
from common.config import Config
from common.log import (
    warn,
    info
)


class SleepService(object):
    """sleep service"""

    def __init__(self, repo: CsvRepoInterface):
        self.config = Config().config
        self.repo = repo

    def get(self) -> dict:
        """get sleep data

        Returns:
            dict: _description_
        """
        info("start to get sleep log")

        # get data
        path = self.config["OURA"]["SLEEP"]
        with open(path, mode="r", encoding="utf-8") as f:
            json_data = json.load(f)
            sleep_data = json_data["sleep"]

        # remove unnecessary data
        # for s in sleep_data:
            # con = s.pop("contributors", None)
        sleep_data = sleep_data[-10::]
        info("finish to get sleep log. path: {0} data len: {1}", path, len(sleep_data))

        return sleep_data

    def add(self) -> None:
        """_summary_

        Returns:
            _type_: _description_
        """
        info("start service add")
        data = self.get()
        cs_repo = CsvSleepRepository()
        cs_repo.add(data)
        info("finish service add")
        return None
