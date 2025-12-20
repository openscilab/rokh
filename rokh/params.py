# -*- coding: utf-8 -*-
"""Parameters for the rokh package."""
from enum import Enum

ROKH_VERSION = "0.3"


class DateSystem(Enum):
    """Enumeration for date system types."""

    JALALI = "jalali"
    GREGORIAN = "gregorian"
    HIJRI = "hijri"
    DEFAULT = JALALI


YEAR_VALUE_ERROR = "`year` must be a positive integer"
MONTH_VALUE_ERROR = "`month` must be a positive integer between 1 and 12"
DAY_VALUE_ERROR = "`day` must be a positive integer between 1 and 31"
INPUT_DATE_SYSTEM_TYPE_ERROR = "`input_date_system` must be an instance of DateSystem"
EVENT_DATE_SYSTEM_TYPE_ERROR = "`event_date_system` must be None or an instance of DateSystem"
