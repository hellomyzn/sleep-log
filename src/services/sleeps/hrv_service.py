"""sleep hrv service"""
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
from repositories.sleep.hrvs import CsvSleepHrvRepository
from services import SubDataBaseService


class SleepHrvService(SubDataBaseService):
    """sleep hrv service"""

    def __init__(self):
        super().__init__(
            csv_repo=CsvSleepHrvRepository(),
            key="hrv"
        )
