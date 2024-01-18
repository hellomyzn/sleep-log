"""met service"""
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


class MetService(SubDataBaseService):
    """met service"""

    def __init__(self, repo: RepoInterface):
        super().__init__(
            repo=repo,
            key="met"
        )
