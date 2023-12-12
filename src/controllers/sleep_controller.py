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
from repositories.sleeps import CsvSleepRepository
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

        new_data = ssc.new(sleep_data)

        # remove unnecessary data or separalate
        # contributors
        # heart_rate
        # hrv
        # readiness

        if new_data:
            new_data_with_id = ssc.put_id(new_data)
            ssc.add(new_data_with_id)
        info("finish to add sleep log")
        return None
