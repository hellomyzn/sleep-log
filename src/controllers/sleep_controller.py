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
        cr = CsvSleepRepository()
        ssc = SleepService(cr)

        sleep_data = ssc.get()
        sleep_data_from_csv = ssc.all()

        new_data = sleep_data
        next_id = 1
        if sleep_data_from_csv:
            latest_datetime = sleep_data_from_csv[-1]["bedtime_start"]
            next_id = int(sleep_data_from_csv[-1]["id"]) + 1
            new_data = ssc.filter_data_by_datetime(sleep_data, latest_datetime)

        info(f"new data num: {len(new_data)}")

        if new_data:
            new_data_with_id = ssc.put_id(new_data, next_id)

            # remove unnecessary data
            contributors = ssc.extract_from_sleep_data(new_data_with_id, "contributors")
            heart_rate = ssc.extract_from_sleep_data(new_data_with_id, "heart_rate")
            hrv = ssc.extract_from_sleep_data(new_data_with_id, "hrv")
            readiness = ssc.extract_from_sleep_data(new_data_with_id, "readiness")

            # ssc.add(new_data_with_id)
        return None
