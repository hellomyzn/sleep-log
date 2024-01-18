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
from repositories.sleeps import CsvSleepRepository
from repositories.sleeps import GssSleepRepository


class SleepController(object):
    """sleep controller"""

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        sleep_ser = SleepService(CsvSleepRepository)
        new_sleep_data = sleep_ser.get_new_data()

        if not new_sleep_data:
            return

        sleep_ser.add(new_sleep_data)
        # sleep_ser.repo = GssSleepRepository()
        # sleep_ser.add(new_sleep_data)

        return None
