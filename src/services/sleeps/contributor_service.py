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
from repositories.interfaces import RepoInterface
from services import SubDataBaseService


class SleepContributorService(SubDataBaseService):
    """sleep contributor service"""

    def __init__(self, repo: RepoInterface):
        super().__init__(
            repo=repo,
            key="contributors"
        )
