# -*- coding: utf-8 -*-
"""Functions for the rokh package"""
from typing import List, Dict, Tuple, Union
from .events.jalali import EVENTS as JALALI_EVENTS
from .params import Calendar


def _handle_jalali_date(month: Union[str, int], day: Union[str, int]) -> Tuple[str, str]:
    """
    Ensure month and day are strings for Jalali calendar events lookup.

    :param month: The month in the Jalali calendar (1-12).
    :param day: The day in the Jalali calendar (1-31).
    :return: A tuple of (month, day) as strings.
    """
    return str(month), str(day)


def _get_jalali_events(month: Union[str, int], day: Union[str, int]) -> List[Dict[str, str]]:
    """
    Retrieve Jalali calendar events for a specific month and day.

    :param month: The month in the Jalali calendar (1-12).
    :param day: The day in the Jalali calendar (1-31).
    """
    month, day = _handle_jalali_date(month, day)
    return JALALI_EVENTS.get(month, {}).get(day, [])


CALENDAR_MAP = {
    Calendar.JALALI: _get_jalali_events,
}


def get_events(
        calendar: Calendar,
        month: Union[str, int],
        day: Union[str, int]) -> List[Dict[str, str]]:
    """
    Retrieve events for a specific month and day in the specified calendar.

    :param calendar: The calendar type.
    :param month: The month in the specified calendar.
    :param day: The day in the specified calendar.
    """
    return CALENDAR_MAP[calendar](month, day)
