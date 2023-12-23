"""csv base repository"""
#########################################################
# Builtin packages
#########################################################
import csv
from dataclasses import dataclass, field
import os
import pathlib

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.interfaces import CsvRepoInterface
from common.log import (
    info,
    warn,
    debug
)


@dataclass
class CsvBaseRepository(CsvRepoInterface):
    """csv base repository"""
    path: str = None
    keys: list = field(init=False, default_factory=list)

    def all(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        info("get all csv data. {0}", self.path)
        self.check_file(self.path)

        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        info("got all csv. data num: {0}", len(data))
        return data

    def find_by_id(self, id_: int):
        pass

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

    def update(self, data: dict):
        pass

    def delete_by_id(self, id_: int):
        pass

    def delete_all(self):
        pass

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
