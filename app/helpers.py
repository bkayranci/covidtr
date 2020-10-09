# -*- coding: utf-8 -*-
"""Helper Module.

"""

def try_int(value: str) -> int:
    """Parse string to int.

    Args:
        value (str): string value.

    Returns:
        int: The return value. int value for success, -1 otherwise.
    """

    try:
        return int(value)
    except ValueError as _:
        return -1

def try_float(value: str):
    """Parse string to float.

    Args:
        value (str): string value.

    Returns:
        int or float: The return value. float value for success, -1 otherwise.
    """

    try:
        return float(value)
    except ValueError as _:
        return -1


def decorate_data_type(value: str or None):
    """Parse string to valid data type.

    Args:
        value (str): string value.

    Returns:
        int or float: The return value. int or float value for success, -1 otherwise.
    """

    if value is None:
        return -1
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return value

    point_count = value.count('.')

    if point_count == 1:
        if len(value.split('.')[1]) > 2:
            return try_int(value.replace('.', ''))
        return try_float(value)
    return try_int(value.replace('.', ''))
