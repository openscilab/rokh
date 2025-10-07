# -*- coding: utf-8 -*-
"""Parameters for the rokh package"""
from enum import Enum

ROKH_VERSION = "0.1"


class DateSystem(Enum):
    """Enumeration for date system types"""
    JALALI = "jalali"
    GREGORIAN = "gregorian"
    HIJRI = "hijri"
    DEFAULT = JALALI


YEAR_TYPE_ERROR = "`year` must be int or str"
YEAR_VALUE_ERROR = "`year` must be a valid integer"
YEAR_POSITIVE_ERROR = "`year` must be positive"

MONTH_TYPE_ERROR = "`month` must be int or str"
MONTH_VALUE_ERROR = "`month` must be a valid integer"
MONTH_RANGE_ERROR = "`month` must be between 1 and 12"

DAY_TYPE_ERROR = "`day` must be int or str"
DAY_VALUE_ERROR = "`day` must be a valid integer"
DAY_RANGE_ERROR = "`day` must be between 1 and 31"

INPUT_DATE_SYSTEM_NONE_ERROR = "`input_date_system` is required and cannot be None"
INPUT_DATE_SYSTEM_TYPE_ERROR = "`input_date_system` must be an instance of DateSystem"

EVENT_DATE_SYSTEM_TYPE_ERROR = "`event_date_system` must be None or an instance of DateSystem"
