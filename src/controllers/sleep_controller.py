"""sleep controller"""
#########################################################
# Builtin packages
#########################################################
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from services import SleepService
from common.log import (
    info
)


class SleepController(object):
    """sleep controller"""

    def __init__(self):
        return None

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        info("start to add sleep log")
        cr = CsvSleepRepository()
        ssc = SleepService(cr)
        sleep_data = ssc.get()
        info("finish to add sleep log")
        return None
