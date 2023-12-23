"""gss base repository"""
#########################################################
# Builtin packages
#########################################################
from dataclasses import dataclass, field

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.interfaces import RepoInterface
from common.log import (
    info
)


@dataclass
class GssBaseRepository(RepoInterface):
    """gss base repository"""
    path: str = None
    keys: list = field(init=False, default_factory=list)

    def all(self) -> list:
        pass

    def find_by_id(self, id_: int):
        pass

    def add(self, data: dict) -> None:
        """_summary_

        Args:
            data (dict): _description_
        """
        info("add data into gss. data num: {0}", len(data))

        # check there is sheet. create a sheet if not
        # check header in header. add header if not

    def update(self, data: dict):
        pass

    def delete_by_id(self, id_: int):
        pass

    def delete_all(self):
        pass

    def has_header(self, path: str) -> bool:
        pass

    def write_header(self, path: str) -> None:
        pass

    def tail(self, num: int) -> list:
        pass
