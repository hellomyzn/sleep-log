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
from repositories.sleep.contributors import CsvSleepContributorRepository
from services import SubDataBaseService


class SleepContributorService(SubDataBaseService):
    """sleep contributor service"""

    def __init__(self):
        super().__init__(
            csv_repo=CsvSleepContributorRepository(),
            key="contributors"
        )
