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
from common.log import (
    warn,
    debug,
    info
)


class SleepReadinessService(SubDataBaseService):
    """sleep readiness service"""

    def __init__(self):
        super().__init__(
            csv_repo=CsvSleepReadinessRepository(),
            key="readiness"
        )

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
                # sleep readiness data has contributors dict
                readiness_contributors = copied_d.pop("contributors")
                copied_d.update(readiness_contributors)
                # add
                data.append(copied_d)

                # replace from value to id
                d.update({self.key: data_id})
                debug("update data. data id: {0}, data[{1}]: {2}",
                      d["id"], self.key, d[self.key])
                data_id += 1
            except KeyError as err:
                warn("key({0}) is not in a data. {1}: {2}, sleep data: {3}.",
                     self.key,  err.__class__.__name__, err, d)

        info("extracted data by key({0}), extracted data num: {1}", self.key, len(data))
        return data
