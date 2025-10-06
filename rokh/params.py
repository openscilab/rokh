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
