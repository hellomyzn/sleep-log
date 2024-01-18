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
from repositories.interfaces import RepoInterface
from common.log import (
    debug,
    info,
    error,
    warn
)


@dataclass
class CsvBaseRepository(RepoInterface):
    """csv base repository"""
    path: str = None
    keys: list = field(init=False, default_factory=list)

    def all(self, path: str) -> list:
        """_summary_

        Args:
            path (str): _description_

        Returns:
            list: _description_
        """
        debug("get all csv data. path: {0}", path)

        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        debug("get all csv data. data num: {0}", len(data))

        return data

    def find_by_id(self, id_: int):
        pass

    def add(self, data: list, columns: list, path: str) -> None:
        """_summary_

        Args:
            data (list): _description_
            columns (list): _description_
            path (str): _description_
        """
        info("add sleep data into csv. data num: {0}, path: {1}, columns: {2}",
             len(data), path, columns)

        with open(path, 'a', encoding="utf-8", newline="") as f:
            for d in data:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writerow(d)

    def update(self, data: dict):
        pass

    def delete_by_id(self, id_: int):
        pass

    def delete_all(self):
        pass

    # TODO: move into helper
    def check_file(self, path: str, columns: list) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
        if not self.file_exists(path):
            pathlib.Path(path).touch()
            warn(f"create a csv file since there was not the file. path: {path}")

        if not self.has_header(path, columns):
            self.write_header(path, columns)

    def file_exists(self, path: str) -> bool:
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            bool: _description_
        """
        return os.path.isfile(path)

    def has_header(self, path: str, columns: list) -> bool:
        """_summary_

        Args:
            path (str): _description_
            columns (list): _description_

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

            if not header == columns:
                error(f"the csv's header is unexpected. columns: {header}, path: {path}")
                raise Exception("can not continue since the header is not expected")

            return True

    def write_header(self, path: str, columns: list) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
        warn("write header. path: {0}, columns: {1}", path, columns)
        with open(path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()

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
