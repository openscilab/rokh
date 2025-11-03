# -*- coding: utf-8 -*-
"""Initialize the rokh package."""

from .functions import get_events, get_today_events
from .errors import RokhValidationError
from .params import ROKH_VERSION, DateSystem

__version__ = ROKH_VERSION
