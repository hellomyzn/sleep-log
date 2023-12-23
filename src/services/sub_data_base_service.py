"""sub data service"""
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
from services import BaseService
from common.log import (
    warn,
    debug,
    info
)


class SubDataBaseService(BaseService):
    """SubDataService service"""

    def __init__(self, repo: RepoInterface, key: str):
        self.key = key
        super().__init__(repo)

    def extract_from(self, from_data: list) -> list:
        """_summary_

        Args:
            from_data (list): _description_

        Returns:
            [list, list]: _description_
        """
        info("extract data by key({0}), data num: {1}", self.key, len(from_data))
        data = []
        data_id = int(self._get_latest_id()) + 1

        for d in from_data:
            from_data_id = d["id"]
            try:
                # 参照渡しの影響を考慮しd.copy()
                # -> append(d)にすると参照元のdataにidが追加されてしまう
                copied_d = d[self.key].copy()
                copied_d["sleep_id"] = from_data_id
                copied_d["id"] = data_id
                data.append(copied_d)

                # replace from value to id
                d.update({self.key: data_id})
                data_id += 1
                debug("update data. data id: {0}, data[{1}]: {2}",
                      d["id"], self.key, d[self.key])
            except KeyError as err:
                warn("key({0}) is not in a data. {1}: {2}, sleep data: {3}.",
                     self.key,  err.__class__.__name__, err, d)

        info("extracted data by key({0}), extracted data num: {1}", self.key, len(data))
        return data

    def _get_latest_id(self) -> int:
        """_summary_

        Args:
            data_type (str): _description_

        Returns:
            int: _description_
        """
        all_data = self.repo.all()
        latest_id = 0

        if all_data:
            latest_id = all_data[-1]["id"]

        debug("get the latest id of {0} is {1}", self.key, latest_id)
        return latest_id
