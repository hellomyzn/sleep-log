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


class SleepController(object):
    """sleep controller"""

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        sleep_ser = SleepService()
        new_sleep_data = sleep_ser.get_new_data()

        contributors_ser = SleepContributorService()
        contributors = contributors_ser.extract_from(new_sleep_data)
        contributors_ser.add(contributors)

        heart_rate_ser = SleepHeartRateService()
        heart_rate = heart_rate_ser.extract_from(new_sleep_data)
        heart_rate_ser.add(heart_rate)

        hrv_ser = SleepHrvService()
        hrv = hrv_ser.extract_from(new_sleep_data)
        hrv_ser.add(hrv)

        readiness_ser = SleepReadinessService()
        readiness = readiness_ser.extract_from(new_sleep_data)
        readiness_ser.add(readiness)

        sleep_ser.add(new_sleep_data)

        return None
