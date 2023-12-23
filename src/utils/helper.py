"""helper"""
#########################################################
# Builtin packages
#########################################################
import json
from datetime import datetime

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
# (None)


def fromisoformat_to_datetime(datetime_str: str) -> datetime:
    """_summary_

    Args:
        datetime_str (str): _description_

    Returns:
        datetime: _description_
    """
    return datetime.fromisoformat(datetime_str).replace(tzinfo=None)


def json_load(path: str) -> list:
    """_summary_

    Args:
        path (str): _description_

    Returns:
        list: _description_
    """
    with open(path, mode="r", encoding="utf-8") as f:
        json_load_ = json.load(f)
    return json_load_
