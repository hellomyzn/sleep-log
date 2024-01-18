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
from repositories.interfaces import RepoInterface
from common.config import Config
from common.log import (
    debug
)


class BaseService(object):
    """sleep base service"""

    def __init__(self, repo: RepoInterface):
        self.config = Config().config
        self.repo = repo()

    def add(self, data: list) -> None:
        """_summary_

        Args:
            sleep_data (list): _description_

        Returns:
            _type_: _description_
        """
        self.repo.add(data)

    def _add_ids(self, data: list, id_: int) -> list:
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
