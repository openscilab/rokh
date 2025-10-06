# -*- coding: utf-8 -*-
"""Functions for the rokh package"""
from typing import List, Dict, Tuple, Union
from .events.jalali import EVENTS as JALALI_EVENTS
from .params import Calendar
import jdatetime
from hijridate


def _convert_to_gregorian(input_date_system: DateSystem, year: int, month: int, day: int) -> Tuple[int, int, int]:
    """
    Convert from input date system to Gregorian.

    :param input_date_system: input date system
    :param year: year
    :param month: month
    :param day: day
    """
    if input_date_system == DateSystem.GREGORIAN:
        return (year, month, day)
    elif input_date_system == DateSystem.JALALI:
        g = jdatetime.JalaliToGregorian(year, month, day)
        return (g.gyear, g.gmonth, g.gday)
    elif input_date_system == DateSystem.HIJRI:
        g = hijridate.Hijri(year, month, day).to_gregorian()
        return (g.year, g.month, g.day)


def _convert_from_gregorian(target_date_system: DateSystem, year: int, month: int, day: int) -> Tuple[int, int, int]:
    """
    Convert from Gregorian to target date system.

    :param target_date_system: target date system
    :param year: year
    :param month: month
    :param day: day
    """
    if target_date_system == DateSystem.GREGORIAN:
        return (year, month, day)
    elif target_date_system == DateSystem.JALALI:
        import jdatetime
        j = jdatetime.GregorianToJalali(year, month, day)
        return (j.jyear, j.jmonth, j.jday)
    elif target_date_system == DateSystem.HIJRI:
        h = hijridate.Gregorian(g_date.year, g_date.month, g_date.day).to_hijri()
        return (h.year, h.month, h.day)


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
