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
from repositories.sleeps import CsvSleepRepository
from common.config import Config
from common.log import (
    info
)


class SleepService(object):
    """sleep service"""

    def __init__(self):
        self.config = Config().config
        return None

    def get(self) -> dict:
        """get sleep data

        Returns:
            dict: _description_
        """
        info("start to get sleep log")

        path = self.config["OURA"]["SLEEP"]
        with open(path, mode="r", encoding="utf-8") as f:
            json_data = json.load(f)
            sleep_data = json_data["sleep"]

        # remove unnecessary data
        for s in sleep_data:
            s.pop("movement_30_sec", None)
            s.pop("heart_rate", None)
            s.pop("hrv", None)
            s.pop("sleep_phase_5_min", None)

        num = -6
        print(sleep_data[num])
        print("day", sleep_data[num]["day"])
        print("score", sleep_data[num]["score"])
        print("type", sleep_data[num]["type"])
        print("bedtime_start", sleep_data[num]["bedtime_start"])
        print("bedtime_end", sleep_data[num]["bedtime_end"])
        print("wake_ups", sleep_data[num]["wake_ups"])
        print("contributors", sleep_data[num]["contributors"])
        print("readiness", sleep_data[num]["readiness"])
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
