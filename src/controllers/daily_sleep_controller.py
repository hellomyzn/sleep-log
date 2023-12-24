"""daily sleep controller"""
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
from services.daily_sleeps import DailySleepService
from repositories.daily_sleeps import CsvDailySleepRepository
from repositories.daily_sleeps import GssDailySleepRepository


class DailySleepController(object):
    """sleep controller"""

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        daily_sleep_ser = DailySleepService(CsvDailySleepRepository)
        new_daily_sleep_data = daily_sleep_ser.get_new_data()

        if not new_daily_sleep_data:
            return

        daily_sleep_ser.add(new_daily_sleep_data)

        daily_sleep_ser.repo = GssDailySleepRepository()
        daily_sleep_ser.add(new_daily_sleep_data)
