"""sleep contributor service"""
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
from repositories.sleep.heart_rates import CsvSleepHeartRateRepository
from services import SubDataBaseService


class SleepHeartRateService(SubDataBaseService):
    """sleep contributor service"""

    def __init__(self):
        super().__init__(
            csv_repo=CsvSleepHeartRateRepository(),
            key="heart_rate"
        )
