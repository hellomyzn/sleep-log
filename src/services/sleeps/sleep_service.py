"""sleep service"""
#########################################################
# Builtin packages
#########################################################
import json

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories.interfaces import RepoInterface
from services import BaseService
from utils.helper import fromisoformat_to_datetime, resolve_file_path
from common.log import (
    warn,
    info
)


class SleepService(BaseService):
    """sleep service"""

    def __init__(self, repo: RepoInterface):
        super().__init__(repo)

    def get_new_data(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        new_sleep_data = self.__get()

        # get sleep data from repo
        all_sleep_data_from_repo = self.all()
        all_sleep = all_sleep_data_from_repo[self.repo.key_sleep]
        all_contributors = all_sleep_data_from_repo[self.repo.key_contributors]
        all_heart_rates = all_sleep_data_from_repo[self.repo.key_heart_rate]
        all_heart_rates_items = all_sleep_data_from_repo[self.repo.key_heart_rate_items]
        all_hrvs = all_sleep_data_from_repo[self.repo.key_hrv]
        all_hrv_items = all_sleep_data_from_repo[self.repo.key_hrv_items]
        all_readiness = all_sleep_data_from_repo[self.repo.key_readiness]
        all_movement_30_sec = all_sleep_data_from_repo[self.repo.key_movement_30_sec]
        all_sleep_phase_5_min = all_sleep_data_from_repo[self.repo.key_sleep_phase_5_min]

        # get only new sleep data if there is data in repo
        latest_sleep_id = 0
        if all_sleep:
            latest_datetime = all_sleep[-1]["bedtime_start"]
            latest_sleep_id = int(all_sleep[-1]["id"])
            new_sleep_data = self.__filter_data_after_datetime(new_sleep_data, latest_datetime)

        if not new_sleep_data:
            info("there is no new data.")
            return []

        # remove timezone
        # 2024-01-11T23:50:29.000+09:00 -> 2024-01-11T23:50:29.000
        for nsd in new_sleep_data:
            nsd["bedtime_start"] = fromisoformat_to_datetime(nsd["bedtime_start"])
            nsd["bedtime_end"] = fromisoformat_to_datetime(nsd["bedtime_end"])

        # add id to new sleep data
        next_id = latest_sleep_id + 1
        new_sleep_data = self._add_ids(new_sleep_data, next_id)

        # extract new data related sleep data.
        extract_data_list = {
            self.repo.key_contributors: all_contributors,
            self.repo.key_heart_rate: all_heart_rates,
            self.repo.key_heart_rate_items: all_heart_rates_items,
            self.repo.key_hrv: all_hrvs,
            self.repo.key_hrv_items: all_hrv_items,
            self.repo.key_readiness: all_readiness,
            self.repo.key_movement_30_sec: all_movement_30_sec,
            self.repo.key_sleep_phase_5_min: all_sleep_phase_5_min}

        # TODO: これだと計算量が多い？
        new_data = {}
        for k, d in extract_data_list.items():
            # get latest id if there is data in repo
            latest_id = 0
            if d:
                latest_id = int(d[-1]["id"])
            next_id = latest_id + 1

            if k == self.repo.key_heart_rate_items:
                data_to_extract = new_data[self.repo.key_heart_rate]
            elif k == self.repo.key_hrv_items:
                data_to_extract = new_data[self.repo.key_hrv]
            else:
                data_to_extract = new_sleep_data

            extracted_data = self.__extract_by(data_to_extract, k)
            new_data[k] = self._add_ids(extracted_data, next_id)

        new_data[self.repo.key_sleep] = new_sleep_data

        info("new sleep data num. sleep: {0}, contributors: {1}, heart_rates: {2}, heart_rate_items: {3} hrvs: {4}, hrv_items: {5}, readiness: {6}, movement_30_secs: {7}, sleep_phase_5_mins: {8}",
             len(new_data[self.repo.key_sleep]), len(new_data[self.repo.key_contributors]),
             len(new_data[self.repo.key_heart_rate]), len(new_data[self.repo.key_heart_rate_items]),
             len(new_data[self.repo.key_hrv]), len(new_data[self.repo.key_hrv_items]),
             len(new_data[self.repo.key_readiness]), len(new_data[self.repo.key_movement_30_sec]), len(new_data[self.repo.key_sleep_phase_5_min]))

        return new_data

    def __get(self) -> dict:
        """get sleep data

        Returns:
            dict: _description_
        """
        # get data
        path = resolve_file_path(self.config["OURA"]["SLEEP"])
        info("get sleep log. {0}", path)

        with open(path, mode="r", encoding="utf-8") as f:
            json_data = json.load(f)
            sleep_data = json_data["sleep"]

        info("got sleep log. data len: {0}", len(sleep_data))
        return sleep_data

    def __filter_data_after_datetime(self, data: list, datetime_str: str) -> list:
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            list: _description_
        """
        info("start to filter data by date: {0}. data num: {1}", datetime_str, len(data))

        latest_datetime = fromisoformat_to_datetime(datetime_str)

        # remove date before the date
        new_data = []
        for d in data:
            datetime = fromisoformat_to_datetime(d["bedtime_start"])
            if latest_datetime < datetime:
                new_data.append(d)

        info("finish to filter data by date. new data num: {0}", len(new_data))
        return new_data

    def __extract_by(self, data: list, key: str) -> list:
        """_summary_

        Args:
            data (list): _description_
            key (str): _description_

        Returns:
            list: _description_
        """
        info("extract data by key: {0}, data num: {1}", key, len(data))
        extracted_data = []
        for d in data:
            data_id = d["id"]
            try:
                is_items = any([key == self.repo.key_heart_rate_items,
                                key == self.repo.key_hrv_items])
                if is_items:
                    popped_data = d.pop("items")
                else:
                    popped_data = d.pop(key)
            except KeyError as err:
                warn("key is not in a data. key: {0}, {1}: {2}, sleep data: {3}.",
                     key,  err.__class__.__name__, err, d)
                continue

            # if popped data is not dict. like "21111222..."
            is_str = any([key == self.repo.key_movement_30_sec,
                          key == self.repo.key_sleep_phase_5_min])
            if is_str:
                popped_str_data = list(popped_data)
                for sd in popped_str_data:
                    str_data = {
                        "sleep_id": data_id,
                        "data": sd}
                    extracted_data.append(str_data)
                continue

            # extract items in heart rate. data is like [None, 64.0, 62.0, 62.0, 59.0, 58.0,...]
            if key == self.repo.key_heart_rate_items:
                popped_item_data = list(popped_data)
                for ld in popped_item_data:
                    list_data = {
                        "heart_rate_id": data_id,
                        "data": ld}
                    extracted_data.append(list_data)
                continue

            # extract items in heart rate. data is like [None, 64.0, 62.0, 62.0, 59.0, 58.0,...]
            if key == self.repo.key_hrv_items:
                popped_item_data = list(popped_data)
                for ld in popped_item_data:
                    list_data = {
                        "hrv_id": data_id,
                        "data": ld}
                    extracted_data.append(list_data)
                continue

            popped_data["sleep_id"] = data_id

            # sleep readiness data has contributors dict
            if key == self.repo.key_readiness:
                readiness_contributors = popped_data.pop("contributors")
                popped_data.update(readiness_contributors)

            # if need to remove timezone from timestamp
            need_to_remove_timezone = any([key == self.repo.key_heart_rate,
                                           key == self.repo.key_hrv])
            if need_to_remove_timezone:
                popped_data["timestamp"] = fromisoformat_to_datetime(popped_data["timestamp"])

            extracted_data.append(popped_data)
        return extracted_data
