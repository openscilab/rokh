# -*- coding: utf-8 -*-
"""Parameters for the rokh package"""
from enum import Enum

ROKH_VERSION = "0.1"


class Calendar(Enum):
    """Enumeration for calendar types"""
    JALALI = "jalali"

    DEFAULT = JALALI
