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

    def new(self, data) -> list:
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            list: _description_
        """
        info(f"start to retrieve new data. data num: {len(data)}")
        # get latest data from csv
        all_data = self.repo.all()
        if len(all_data) == 0:
            warn(f"there is no data. repo: {self.repo.__class__}")
            return data
        latest_data = all_data[-1]
        # TODO: remove
        print(latest_data)

        # get "day" as latest date
        latest_datetime = fromisoformat_to_datetime(latest_data["bedtime_start"])

        # remove date before the date
        new_data = []
        for d in data:
            datetime = fromisoformat_to_datetime(d["bedtime_start"])
            if latest_datetime < datetime:
                new_data.append(d)
        return new_data

    def put_id(self, data: list) -> list:
        """_summary_

        Args:
            data (list): _description_

        Returns:
            list: _description_
        """
        info(f"start to put id to each elements. data num: {len(data)}")
        all_data = self.repo.all()
        if len(all_data) == 0:
            warn(f"there is no data. repo: {self.repo.__class__}")
            _id = 1
        else:
            _id = int(all_data[-1]["id"]) + 1

        for d in data:
            d.update({"id": _id})
            _id += 1

        info(f"finish to put id to each elements. data: {data}")
        return data

    def add(self, data: list) -> None:
        """_summary_

        Args:
            sleep_data (list): _description_

        Returns:
            _type_: _description_
        """
        info(f"start service add. data num: {len(data)}")
        self.repo.add(data)

        info("finish service add")
