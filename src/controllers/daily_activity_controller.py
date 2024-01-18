"""daily activity controller"""
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
from services.daily_activities import DailyActivityService
from services.daily_activities import ContributorService
from services.daily_activities import MetService
from services.daily_activities import RingMetService
from repositories.daily_activity.daily_activities import CsvDailyActivityRepository
from repositories.daily_activity.daily_activities import GssDailyActivityRepository
from repositories.daily_activity.contributors import CsvContributorRepository
from repositories.daily_activity.contributors import GssContributorRepository
from repositories.daily_activity.met import CsvMetRepository
from repositories.daily_activity.met import GssMetRepository
from repositories.daily_activity.ring_met import CsvRingMetRepository
from repositories.daily_activity.ring_met import GssRingMetRepository


class DailyActivityController(object):
    """daily activity controller"""

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """

        da_ser = DailyActivityService(CsvDailyActivityRepository)
        contributors_ser = ContributorService(CsvContributorRepository)
        met_ser = MetService(CsvMetRepository)
        ring_met_ser = RingMetService(CsvRingMetRepository)

        new_daily_activity_data = da_ser.get_new_data()
        if not new_daily_activity_data:
            # add: log
            return

        # extract data from daily activity
        contributors = contributors_ser.extract_from(new_daily_activity_data)
        met = met_ser.extract_from(new_daily_activity_data)
        ring_met = ring_met_ser.extract_from(new_daily_activity_data)
        print(new_daily_activity_data[-1])

        # add
        # da_ser.add(new_daily_activity_data)
        # contributors_ser.add(contributors)
        # met_ser.add(met)
        # ring_met_ser.add(ring_met)

        # change repo to gss
        # add
