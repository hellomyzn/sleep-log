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
from services.sleeps import SleepService
from services.sleeps import SleepContributorService
from services.sleeps import SleepHeartRateService
from services.sleeps import SleepHrvService
from services.sleeps import SleepReadinessService
from repositories.sleep.sleeps import CsvSleepRepository
from repositories.sleep.sleeps import GssSleepRepository
from repositories.sleep.contributors import CsvSleepContributorRepository
from repositories.sleep.contributors import GssSleepContributorRepository
from repositories.sleep.heart_rates import CsvSleepHeartRateRepository
from repositories.sleep.heart_rates import GssSleepHeartRateRepository
from repositories.sleep.hrvs import CsvSleepHrvRepository
from repositories.sleep.hrvs import GssSleepHrvRepository
from repositories.sleep.readinesses import CsvSleepReadinessRepository
from repositories.sleep.readinesses import GssSleepReadinessRepository


class SleepController(object):
    """sleep controller"""

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        sleep_ser = SleepService(CsvSleepRepository)
        contributors_ser = SleepContributorService(CsvSleepContributorRepository)
        heart_rate_ser = SleepHeartRateService(CsvSleepHeartRateRepository)
        hrv_ser = SleepHrvService(CsvSleepHrvRepository)
        readiness_ser = SleepReadinessService(CsvSleepReadinessRepository)

        new_sleep_data = sleep_ser.get_new_data()
        if not new_sleep_data:
            return

        contributors = contributors_ser.extract_from(new_sleep_data)
        heart_rate = heart_rate_ser.extract_from(new_sleep_data)
        hrv = hrv_ser.extract_from(new_sleep_data)
        readiness = readiness_ser.extract_from(new_sleep_data)

        sleep_ser.add(new_sleep_data)
        heart_rate_ser.add(heart_rate)
        contributors_ser.add(contributors)
        hrv_ser.add(hrv)
        readiness_ser.add(readiness)

        sleep_ser.repo = GssSleepRepository()
        contributors_ser.repo = GssSleepContributorRepository()
        heart_rate_ser.repo = GssSleepHeartRateRepository()
        hrv_ser.repo = GssSleepHrvRepository()
        readiness_ser = GssSleepReadinessRepository()

        sleep_ser.add(new_sleep_data)
        contributors_ser.add(contributors)
        heart_rate_ser.add(heart_rate)
        hrv_ser.add(hrv)
        readiness_ser.add(readiness)

        return None
