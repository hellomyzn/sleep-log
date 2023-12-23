"""sleep readiness service"""
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
from repositories.sleep.readinesses import CsvSleepReadinessRepository
from services import SubDataBaseService


class SleepReadinessService(SubDataBaseService):
    """sleep readiness service"""

    def __init__(self):
        super().__init__(
            csv_repo=CsvSleepReadinessRepository(),
            key="readiness"
        )
