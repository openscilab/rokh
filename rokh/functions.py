# -*- coding: utf-8 -*-
"""Functions for the rokh package"""
from typing import List, Dict, Tuple, Union, Optional, Any
from .events.jalali import EVENTS as JALALI_EVENTS
from .events.gregorian import EVENTS as GREGORIAN_EVENTS
from .events.hijri import EVENTS as HIJRI_EVENTS
from .params import DateSystem
import datetime
import jdatetime
import hijridate


def _convert_to_gregorian(input_date_system: DateSystem, day: int, month: int, year: int) -> Tuple[int, int, int]:
    """
    Convert from input date system to Gregorian.

    :param input_date_system: input date system
    :param day: day in input date system
    :param month: month in input date system
    :param year: year in input date system
    """
    if input_date_system == DateSystem.GREGORIAN:
        return (day, month, year)
    elif input_date_system == DateSystem.JALALI:
        g = jdatetime.JalaliToGregorian(year, month, day)
        return (g.gday, g.gmonth, g.gyear)
    elif input_date_system == DateSystem.HIJRI:
        g = hijridate.Hijri(year, month, day).to_gregorian()
        return (g.day, g.month, g.year)


def _convert_from_gregorian(target_date_system: DateSystem,  day: int, month: int, year: int) -> Tuple[int, int, int]:
    """
    Convert from Gregorian to target date system.

    :param target_date_system: target date system
    :param day: day in Gregorian date system
    :param month: month in Gregorian date system
    :param year: year in Gregorian date system
    """
    if target_date_system == DateSystem.GREGORIAN:
        return (day, month, year)
    elif target_date_system == DateSystem.JALALI:
        j = jdatetime.GregorianToJalali(year, month, day)
        return (j.jday, j.jmonth, j.jyear)
    elif target_date_system == DateSystem.HIJRI:
        h = hijridate.Gregorian(year, month, day).to_hijri()
        return (h.day, h.month, h.year)


def get_jalali_events(day: int, month: int, year: int= None) -> List[Dict[str, str]]:
    """
    Retrieve Jalali events for a specific date.

    :param day: day in Jalali date system
    :param month: month in Jalali date system
    :param year: year in Jalali date system
    """
    return JALALI_EVENTS.get(str(month), {}).get(str(day), [])


def get_gregorian_events(day: int, month: int, year: int= None) -> List[Dict[str, str]]:
    """
    Retrieve Gregorian events for a specific date.

    :param day: day in Gregorian date system
    :param month: month in Gregorian date system
    :param year: year in Gregorian date system
    """
    return GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])


def get_hijri_events(day: int, month: int, year: int= None) -> List[Dict[str, str]]:
    """
    Retrieve Hijri events for a specific date.

    :param day: day in Hijri date system
    :param month: month in Hijri date system
    :param year: year in Hijri date system
    """
    return HIJRI_EVENTS.get(str(month), {}).get(str(day), [])


def _validate_get_events(
    day: Any,
    month: Any,
    year: Any,
    input_date_system: Any,
    event_date_system: Any) -> None:
    """
    Validate get_events function inputs.

    :param day: day in input date system
    :param month: month in input date system
    :param year: year in input date system
    :param input_date_system: input date system
    :param event_date_system: event date system
    """
    if year is not None:
        if not isinstance(year, (int, str)):
            raise RokhValidationError(YEAR_VALUE_ERROR )
        try:
            year = int(year)
        except ValueError:
            raise RokhValidationError(YEAR_VALUE_ERROR )
        if year <= 0:
            raise RokhValidationError(YEAR_VALUE_ERROR)

    if not isinstance(month, (int, str)):
        raise RokhValidationError(MONTH_VALUE_ERROR)
    try:
        month = int(month)
    except ValueError:
        raise RokhValidationError(MONTH_VALUE_ERROR)
    if not 1 <= month <= 12:
        raise RokhValidationError(MONTH_VALUE_ERROR)

    if not isinstance(day, (int, str)):
        raise RokhValidationError(DAY_VALUE_ERROR)
    try:
        day = int(day)
    except ValueError:
        raise RokhValidationError(DAY_VALUE_ERROR)
    if not 1 <= day <= 31:
        raise RokhValidationError(DAY_VALUE_ERROR)

    if not isinstance(input_date_system, DateSystem):
        raise RokhValidationError(INPUT_DATE_SYSTEM_TYPE_ERROR)

    if event_date_system is not None:
        if not isinstance(event_date_system, DateSystem):
            raise RokhValidationError(EVENT_DATE_SYSTEM_TYPE_ERROR)


def get_events(
    day: int,
    month: int,
    year: Optional[int] = None,
    input_date_system: DateSystem = DateSystem.JALALI,
    event_date_system: Optional[DateSystem] = None,
) -> Dict[str, List[Dict[str, str]]]:
    """
    Retrieve events for a specific day, month and year in the specified date system.

    :param day: day in input date system
    :param month: month in input date system
    :param year: year in input date system
    :param input_date_system: input date system
    :param event_date_system: event date system
    """
    _validate_get_events(day=day, month=month, year=year, input_date_system=input_date_system, event_date_system=event_date_system)
    if year is None:
        year = datetime.now().year
    year = int(year)
    month = int(month)
    day = int(day)
    gregorian_date = _convert_to_gregorian(input_date_system, day, month, year)
    jalali_date = _convert_from_gregorian(DateSystem.JALALI, *gregorian_date)
    hijri_date = _convert_from_gregorian(DateSystem.HIJRI, *gregorian_date)
    result = {"events": []}

    if event_date_system is None:
        result["events"].extend(get_jalali_events(*jalali_date))
        result["events"].extend(get_gregorian_events(*gregorian_date))
        result["events"].extend(get_hijri_events(*hijri_date))
    else:
        if event_date_system == DateSystem.JALALI:
            result["events"] = get_jalali_events(*jalali_date)
        elif event_date_system == DateSystem.GREGORIAN:
            result["events"] = get_gregorian_events(*gregorian_date)
        elif event_date_system == DateSystem.HIJRI:
            result["events"] = get_hijri_events(*hijri_date)
    return result
