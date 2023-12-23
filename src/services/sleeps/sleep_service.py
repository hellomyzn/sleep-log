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
from repositories.interfaces import RepoInterface
from services import BaseService
from utils.helper import fromisoformat_to_datetime
from common.log import (
    info
)


class SleepService(BaseService):
    """sleep service"""

    def __init__(self, repo: RepoInterface):
        super().__init__(repo)

    def get_new_data(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        new_sleep_data = self.get()

        sleep_data_from_repo = self.all()
        latest_id = 0
        if sleep_data_from_repo:
            latest_datetime = sleep_data_from_repo[-1]["bedtime_start"]
            latest_id = int(sleep_data_from_repo[-1]["id"])
            new_sleep_data = self.__filter_data_after_datetime(data=new_sleep_data, datetime_str=latest_datetime)

        if not new_sleep_data:
            info("there is no new data.")
            return []

        next_sleep_id = latest_id + 1
        sleep_data_with_id = self._add_ids(new_sleep_data, next_sleep_id)

        # TODO: remove
        sleep_data_with_id = sleep_data_with_id[0:100]
        info("new sleep data num: {0}", len(sleep_data_with_id))
        return sleep_data_with_id

    def get(self) -> dict:
        """get sleep data

        Returns:
            dict: _description_
        """
        # get data
        path = self.config["OURA"]["SLEEP"]
        info("get sleep log. {0}", path)

        with open(path, mode="r", encoding="utf-8") as f:
            json_data = json.load(f)
            sleep_data = json_data["sleep"]

        info("got sleep log. data len: {0}", len(sleep_data))
        return sleep_data

    def __filter_data_after_datetime(self, data: list, datetime_str: str) -> list:
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            list: _description_
        """
        info("start to filter data by date: {0}. data num: {1}", datetime_str, len(data))

        latest_datetime = fromisoformat_to_datetime(datetime_str)

        # remove date before the date
        new_data = []
        for d in data:
            datetime = fromisoformat_to_datetime(d["bedtime_start"])
            if latest_datetime < datetime:
                new_data.append(d)

        info("finish to filter data by date. new data num: {0}", len(new_data))
        return new_data
