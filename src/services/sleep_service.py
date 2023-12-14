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
    debug,
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
        # get data
        path = self.config["OURA"]["SLEEP"]
        info("start to get sleep log. {0}", path)

        with open(path, mode="r", encoding="utf-8") as f:
            json_data = json.load(f)
            sleep_data = json_data["sleep"]

        # remove unnecessary data
        # sleep_data = sleep_data[-10::]
        info("finish to get sleep log. data len: {0}", len(sleep_data))
        return sleep_data

    def all(self, data_type: str) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        data = self.repo.all(data_type)
        return data

    def filter_data_by_datetime(self, data: list, datetime_str: str) -> list:
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

    def put_id(self, data: list, next_id: int) -> list:
        """_summary_

        Args:
            data (list): _description_
            _id (int): _description_

        Returns:
            list: _description_
        """
        info("start to put id to each elements. data num: {0}, next id: {1}", len(data), next_id)
        data_with_id = []
        for i, d in enumerate(data):
            # 参照渡しの影響を考慮しd.copy()
            # -> append(d)にすると参照元のdataにidが追加されてしまう
            data_with_id.append(d.copy())
            data_with_id[i]["id"] = next_id
            next_id += 1

        info("finish to put id to each elements. next id: {0}", next_id)
        return data_with_id

    def extract_from_sleep_data(self, sleep_data: list, key: str) -> list:
        """_summary_

        Args:
            sleep_data (list): _description_
            key (str): _description_

        Returns:
            [list, list]: _description_
        """
        info("start extract data from sleep data. key: {0}, sleep data num: {1}", key, len(sleep_data))
        data = []

        for d in sleep_data:
            data_id = d["id"]
            try:
                # 参照渡しの影響を考慮しd.copy()
                # -> append(d)にすると参照元のdataにidが追加されてしまう
                copied_data = d[key].copy()
                copied_data["sleep_id"] = data_id
                data.append(copied_data)

                # update from sleep_data[key] to id
                d.update({key: copied_data["id"]})
                debug("copied_data's id: {0}, sleep_data[key]: {1}", copied_data["id"], d[key])

            except KeyError as err:
                warn("key({0}) is not in a data. {1}: {2}, sleep data: {3}.", key,  err.__class__.__name__, err, d)

        info("finish extract data from sleep data. key: {0}, extracted data num: {1}", key, len(data))
        return data

    def add(self, data: list) -> None:
        """_summary_

        Args:
            sleep_data (list): _description_

        Returns:
            _type_: _description_
        """
        self.repo.add(data)

    def transform_to_dict(self, data_type: str, data: list) -> dict:
        """_summary_

        Args:
            data_type (str): _description_
            data (list): _description_

        Returns:
            list: _description_
        """
        info("start to add data type. data type: {0}", data_type)
        data_dict = {"data_type": data_type, "data": data}

        info("finish to add data type. data type: {0}, data num: {1}",
             data_dict["data_type"], len(data_dict["data"]))
        return data_dict

    def get_latest_id(self, data_type: str) -> int:
        """_summary_

        Args:
            data_type (str): _description_

        Returns:
            int: _description_
        """
        all_data = self.repo.all(data_type)
        if not all_data:
            return 0

        return all_data[-1]["id"]
