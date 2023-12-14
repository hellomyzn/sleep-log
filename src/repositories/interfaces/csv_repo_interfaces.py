"""csv.sample_interface"""
#########################################################
# Builtin packages
#########################################################
import abc
import csv
import os
import pathlib

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from common.log import (
    warn,
    error
)


class CsvRepoInterface(metaclass=abc.ABCMeta):
    """csv repository interface"""
    COLUMNS = None

    def __init__(self):
        self.path = None
        self.keys = None

    @abc.abstractmethod
    def all(self, data_type: str):
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

    @abc.abstractmethod
    def tail(self, data_type: str, num: int) -> list:
        """tail"""
        raise NotImplementedError()

    def check_file(self, path: str) -> None:
        # TODO: make decorator
        if not self.file_exists(path):
            pathlib.Path(path).touch()
            warn(f"create a csv file since there was not the file. path: {path}")

        if not self.has_header(path):
            self.write_header(path)

    def file_exists(self, path: str) -> bool:
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            bool: _description_
        """
        return os.path.isfile(path)

    def has_header(self, path: str) -> bool:
        """_summary_

        Args:
            path (str): _description_

        Raises:
            Exception: _description_

        Returns:
            bool: _description_
        """
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames

            if header is None:
                warn(f"header does not exist. path: {path}")
                return False

            # if not header == self.COLUMNS:
            #     error(f"the csv's header is unexpected. columns: {header}, path: {path}")
            #     raise Exception("can not continue since the header is not expected")

            return True

    def write_header(self, path: str) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
        warn(f"write header. path: {path}")
        with open(path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.keys)
            writer.writeheader()

        warn("successfully write header.")
