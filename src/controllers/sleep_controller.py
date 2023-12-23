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

        heart_rate_ser = SleepHeartRateService()
        heart_rate = heart_rate_ser.extract_from(new_sleep_data)

        hrv_ser = SleepHrvService()
        hrv = hrv_ser.extract_from(new_sleep_data)

        readiness_ser = SleepReadinessService()
        readiness = readiness_ser.extract_from(new_sleep_data)

        print(new_sleep_data[-1])

        # for r in readiness:
        #     readiness_contributors = r.pop("contributors")
        #     r.update(readiness_contributors)

        # # transform from list to dict to add data type
        # sleep_dict = ss.transform_to_dict("sleep", new_sleep_data_with_id)
        # contributors_dict = ss.transform_to_dict("contributors", contributors)
        # heart_rate_dict = ss.transform_to_dict("heart_rate", heart_rate)
        # hrv_dict = ss.transform_to_dict("hrv", hrv)
        # readiness_dict = ss.transform_to_dict("readiness", readiness)

        # ss.add(sleep_dict)
        # ss.add(contributors_dict)
        # ss.add(heart_rate_dict)
        # ss.add(hrv_dict)
        # ss.add(readiness_dict)

        return None
