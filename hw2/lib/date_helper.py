"""
helper functions for translating between datetime objects and strings
standardized on the format YYYY-MM-DD
"""


from datetime import datetime


DATE_FORMAT = '%Y-%m-%d'


def date_to_string(date: datetime) -> str:
    """
    :param date: datetime, the date to convert
    :return: str, the date in the format specified in config.date_format
    """
    return datetime.strftime(date, DATE_FORMAT)

def string_to_date(datestring: str) -> datetime:
    """
    :param datestring: str, the date to convert
    :return: datetime, the date in the format specified in config.date_format
    """
    return datetime.strptime(datestring, DATE_FORMAT)
