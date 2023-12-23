"""base service"""
#########################################################
# Builtin packages
#########################################################
import copy

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.interfaces import CsvRepoInterface
from common.config import Config
from common.log import (
    debug,
    info
)


class BaseService(object):
    """sleep base service"""

    def __init__(self, csv_repo: CsvRepoInterface):
        self.config = Config().config
        self.csv_repo = csv_repo

    def all(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        return self.csv_repo.all()

    def add(self, data: list) -> None:
        """_summary_

        Args:
            sleep_data (list): _description_

        Returns:
            _type_: _description_
        """
        self.csv_repo.add(data)

    def add_ids(self, data: list, id_: int) -> list:
        """_summary_

        Args:
            data (list): _description_
            id_ (int): _description_

        Returns:
            list: _description_
        """
        debug("add id to each elements. data num: {0}, id: {1}", len(data), id_)
        # deepcopy
        data_with_id = copy.deepcopy(data)

        for d in data_with_id:
            d["id"] = id_
            id_ += 1

        return data_with_id

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
