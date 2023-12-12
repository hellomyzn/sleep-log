"""helper"""
#########################################################
# Builtin packages
#########################################################
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
