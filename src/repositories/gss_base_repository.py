"""gss base repository"""
#########################################################
# Builtin packages
#########################################################
import time
from dataclasses import dataclass, field

#########################################################
# 3rd party packages
#########################################################
import gspread

#########################################################
# Own packages
#########################################################
from common.google_spreadsheet import GssAccessor
from repositories.interfaces import RepoInterface
from common.config import Config
from common.log import (
    warn,
    info
)
CONFIG = Config().config
SHEET_KEY = CONFIG["GSS"]["SHEET_KEY"]


@dataclass
class GssBaseRepository(RepoInterface):
    """gss base repository"""
    sheet: str = field(init=False, default=None)
    keys: list = field(init=False, default_factory=list)
    worksheet: gspread = field(init=False, default=None)
    sleep_time_sec: float = field(init=False, default=1.0)

    def __post_init__(self):
        gss = GssAccessor()
        workbook = gss.connection.open_by_key(SHEET_KEY)
        self.worksheet = workbook.worksheet(self.sheet)

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
        if not self.has_header():
            self.write_header()

        row_num = self.find_next_available_row()

        for d in data:
            for col_num, key in enumerate(self.keys, start=2):
                try:
                    v = d[key]
                    self.worksheet.update_cell(row_num, col_num, str(v))
                    info("added data in gss({0}). column: {1}, value: {2}",
                         self.sheet, key, v)
                    time.sleep(self.sleep_time_sec)
                except KeyError as err:
                    warn("key({0}) is not in a data. {1}: {2}",
                         key,  err.__class__.__name__, err)
            row_num += 1

    def has_header(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        header = self.worksheet.row_values(1)
        return any(header)

    def write_header(self) -> None:
        for i, column in enumerate(self.keys, start=2):
            self.worksheet.update_cell(1, i, column)

    def find_next_available_row(self) -> int:
        """ Find a next available row on GSS
            This is for confirming from which row is available
            when you add data on GSS.

        Returns:
            int: _description_
        """
        # it is a list which contains all data on first column
        fist_column_data = list(filter(None, self.worksheet.col_values(2)))
        available_row = int(len(fist_column_data)) + 1
        return available_row

    def update(self, data: dict):
        pass

    def delete_by_id(self, id_: int):
        pass

    def delete_all(self):
        pass

    def tail(self, num: int) -> list:
        pass
