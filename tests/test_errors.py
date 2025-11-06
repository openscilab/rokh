import pytest
from rokh import get_events, DateSystem, RokhValidationError

TEST_CASE_NAME = "Errors tests"


def test_year_error1():
    with pytest.raises(RokhValidationError, match=r"`year` must be a positive integer"):
        _ = get_events(year="1404", month=1, day=1, input_date_system=DateSystem.JALALI)


def test_year_error2():
    with pytest.raises(RokhValidationError, match=r"`year` must be a positive integer"):
        _ = get_events(year=0, month=1, day=1, input_date_system=DateSystem.JALALI)


def test_month_error1():
    with pytest.raises(RokhValidationError, match=r"`month` must be a positive integer between 1 and 12"):
        _ = get_events(year=1404, month="1", day=1, input_date_system=DateSystem.JALALI)


def test_month_error2():
    with pytest.raises(RokhValidationError, match=r"`month` must be a positive integer between 1 and 12"):
        _ = get_events(year=1404, month=13, day=1, input_date_system=DateSystem.JALALI)


def test_day_error1():
    with pytest.raises(RokhValidationError, match=r"`day` must be a positive integer between 1 and 31"):
        _ = get_events(year=1404, month=1, day="1", input_date_system=DateSystem.JALALI)


def test_day_error2():
    with pytest.raises(RokhValidationError, match=r"`day` must be a positive integer between 1 and 31"):
        _ = get_events(year=1404, month=1, day=32, input_date_system=DateSystem.JALALI)


def test_input_date_system_error():
    with pytest.raises(RokhValidationError, match=r"`input_date_system` must be an instance of DateSystem"):
        _ = get_events(year=1404, month=1, day=1, input_date_system="Jalali")


def test_event_date_system_error():
    with pytest.raises(RokhValidationError, match=r"`event_date_system` must be None or an instance of DateSystem"):
        _ = get_events(year=1404, month=1, day=1, input_date_system=DateSystem.JALALI, event_date_system="Jalali")
