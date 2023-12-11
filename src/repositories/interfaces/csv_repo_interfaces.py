"""csv.sample_interface"""
#########################################################
# Builtin packages
#########################################################
import abc
import csv

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from common.log import (
    info,
    warn,
    error
)


class CsvRepoInterface(metaclass=abc.ABCMeta):
    """csv repository interface"""
    COLUMNS = None

    def __init__(self):
        self.path = None

    @abc.abstractmethod
    def all(self):
        """all"""
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, _id: int):
        """find by id"""
        raise NotImplementedError()

    @abc.abstractmethod
    def add(self, data: dict):
        """add"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_by_id(self, _id: int):
        """delete by id"""
        raise NotImplementedError()

    def has_header(self) -> bool:
        """_summary_

        Raises:
            Exception: _description_

        Returns:
            bool: _description_
        """
        info(f"check to have header or not. path: {self.path}")
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames

            if header is None:
                warn("header does not exist.")
                return False

            if not header == self.COLUMNS:
                error(f"unexpected columns. columns: {header}")
                raise Exception("can not continue since the header is not expected")

            info("the csv file has header.")
            return True

    def write_header(self) -> None:
        """_summary_
        """
        warn(f"write header. path: {self.path}")
        with open(self.path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUMNS)
            writer.writeheader()

        warn("successfully write header.")
