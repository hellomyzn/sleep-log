"""sleep controller"""
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
from repositories.sleeps import CsvSleepRepository
from services import SleepService
from common.log import (
    info
)


class SleepController(object):
    """sleep controller"""

    def __init__(self):
        return None

    def add(self) -> None:
        """add sleep log
        Returns:
            None: _description_
        """
        csr = CsvSleepRepository()
        ssc = SleepService(csr)

        sleep_data_from_csv = ssc.all()
        new_sleep_data = ssc.get()

        if sleep_data_from_csv:
            latest_datetime = sleep_data_from_csv[-1]["bedtime_start"]
            new_sleep_data = ssc.filter_data_after_datetime(
                data=new_sleep_data, datetime_str=latest_datetime)

        # TODO: remove
        new_sleep_data = new_sleep_data[-10:]
        info(f"new data num: {len(new_sleep_data)}")

        if not new_sleep_data:
            info("there is no new data.")
            return

        next_id = int(ssc.get_latest_id()) + 1
        sleep_data = ssc.add_ids_to_data(
            data=new_sleep_data, next_id=next_id)

        extracted_contributors = ssc.extract_from_sleep_data(sleep_data=new_sleep_data, key="contributors")
        c_next_id = int(ssc.get_latest_id("contributors")) + 1
        contributors = ssc.put_id(extracted_contributors, c_next_id)

        heart_rate_without_id = ssc.extract_from_sleep_data(new_sleep_data_with_id, "heart_rate")
        hr_next_id = int(ssc.get_latest_id("heart_rate")) + 1
        heart_rate = ssc.put_id(heart_rate_without_id, hr_next_id)

        hrv_without_id = ssc.extract_from_sleep_data(new_sleep_data_with_id, "hrv")
        h_next_id = int(ssc.get_latest_id("hrv")) + 1
        hrv = ssc.put_id(hrv_without_id, h_next_id)

        readiness_without_id = ssc.extract_from_sleep_data(new_sleep_data_with_id, "readiness")
        r_next_id = int(ssc.get_latest_id("readiness")) + 1
        readiness = ssc.put_id(readiness_without_id, r_next_id)

        for r in readiness:
            readiness_contributors = r.pop("contributors")
            r.update(readiness_contributors)

        # transform from list to dict to add data type
        sleep_dict = ssc.transform_to_dict("sleep", new_sleep_data_with_id)
        contributors_dict = ssc.transform_to_dict("contributors", contributors)
        heart_rate_dict = ssc.transform_to_dict("heart_rate", heart_rate)
        hrv_dict = ssc.transform_to_dict("hrv", hrv)
        readiness_dict = ssc.transform_to_dict("readiness", readiness)

        ssc.add(sleep_dict)
        ssc.add(contributors_dict)
        ssc.add(heart_rate_dict)
        ssc.add(hrv_dict)
        ssc.add(readiness_dict)

        return None
