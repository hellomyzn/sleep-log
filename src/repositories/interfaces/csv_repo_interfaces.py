"""csv.sample_interface"""
#########################################################
# Builtin packages
#########################################################
import abc
import csv
from dataclasses import dataclass
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
    info,
    warn,
    debug
)


@dataclass
class CsvRepoInterface(metaclass=abc.ABCMeta):
    """csv repository interface"""
    path: str = None

    @abc.abstractmethod
    def find_by_id(self, id_: int):
        """find by id"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_by_id(self, id_: int):
        """delete by id"""
        raise NotImplementedError()

    def all(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        info("start to get all csv data.")
        self.check_file(self.path)

        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        info(f"finish to get all data from csv. all csv data num: {len(data)}")
        return data

    def add(self, data: dict) -> None:
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        info("start to add sleep log into csv. data type: {0}, data num",
             data["data_type"], len(data["data"]))

        self.check_file(self.path)

        with open(self.path, 'a', encoding="utf-8", newline="") as f:
            for d in data["data"]:
                writer = csv.DictWriter(f, fieldnames=self.keys)
                writer.writerow(d)
                debug("added data into csv: {0}", d)
        info("finish to add sleep log into csv")
        return None

    # TODO: move into helper

    def check_file(self, path: str) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
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

    def tail(self, num: int) -> list:
        """_summary_

        Args:
            num (int): _description_

        Returns:
            list: _description_
        """
        info("start to tail")

        with open(self.path, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tail_lines = []
            for r in reader:
                tail_lines.append(r)

        info("finish to tail")
        return tail_lines[-num:]
