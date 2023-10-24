"""
helper functions for translating between datetime objects and strings
standardized on the format YYYY-MM-DD
"""


from datetime import datetime


DATE_FORMAT = '%Y-%m-%d'


def catch_invalid_datestring_errors(func):
    """
    decorator to catch invalid datestring errors and return None
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            print('WARNING: invalid datestring', flush=True) # TODO logging?
            return None
    return wrapper


@catch_invalid_datestring_errors
def date_to_string(date: datetime) -> str:
    """
    :param date: datetime, the date to convert
    :return: str, the date in the format specified in config.date_format
    """
    return datetime.strftime(date, DATE_FORMAT)


@catch_invalid_datestring_errors
def string_to_date(datestring: str) -> datetime:
    """
    :param datestring: str, the date to convert
    :return: datetime, the date in the format specified in config.date_format
    """
    return datetime.strptime(datestring, DATE_FORMAT)
