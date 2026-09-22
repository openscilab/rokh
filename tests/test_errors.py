import pytest
from rokh import get_events, DateSystem, RokhValidationError, RokhError

TEST_CASE_NAME = "Errors tests"


def test_error_inheritance():
    assert issubclass(RokhError, Exception)
    assert issubclass(RokhValidationError, RokhError)
    assert issubclass(RokhValidationError, ValueError)


def test_year_error1():
    with pytest.raises(RokhValidationError, match=r"`year` must be a positive integer"):
        _ = get_events(year="1404", month=1, day=1, input_date_system=DateSystem.JALALI)


def test_year_error2():
    with pytest.raises(RokhValidationError, match=r"`year` must be a positive integer"):
        _ = get_events(year=0, month=1, day=1, input_date_system=DateSystem.JALALI)


def test_year_error3():
    with pytest.raises(RokhValidationError, match=r"`year` must be a positive integer"):
        _ = get_events(year=True, month=1, day=1, input_date_system=DateSystem.JALALI)


def test_month_error1():
    with pytest.raises(RokhValidationError, match=r"`month` must be a positive integer between 1 and 12"):
        _ = get_events(year=1404, month="1", day=1, input_date_system=DateSystem.JALALI)


def test_month_error2():
    with pytest.raises(RokhValidationError, match=r"`month` must be a positive integer between 1 and 12"):
        _ = get_events(year=1404, month=13, day=1, input_date_system=DateSystem.JALALI)


def test_month_error3():
    with pytest.raises(RokhValidationError, match=r"`month` must be a positive integer between 1 and 12"):
        _ = get_events(year=1404, month=True, day=1, input_date_system=DateSystem.JALALI)


def test_day_error1():
    with pytest.raises(RokhValidationError, match=r"`day` must be a positive integer between 1 and 31"):
        _ = get_events(year=1404, month=1, day="1", input_date_system=DateSystem.JALALI)


def test_day_error2():
    with pytest.raises(RokhValidationError, match=r"`day` must be a positive integer between 1 and 31"):
        _ = get_events(year=1404, month=1, day=32, input_date_system=DateSystem.JALALI)


def test_day_error3():
    with pytest.raises(RokhValidationError, match=r"`day` must be a positive integer between 1 and 31"):
        _ = get_events(year=1404, month=1, day=True, input_date_system=DateSystem.JALALI)


def test_input_date_system_error():
    with pytest.raises(RokhValidationError, match=r"`input_date_system` must be an instance of DateSystem"):
        _ = get_events(year=1404, month=1, day=1, input_date_system="Jalali")


def test_event_date_system_error():
    with pytest.raises(RokhValidationError, match=r"`event_date_system` must be None or an instance of DateSystem"):
        _ = get_events(year=1404, month=1, day=1, input_date_system=DateSystem.JALALI, event_date_system="Jalali")


def test_date_error1():
    with pytest.raises(RokhValidationError, match=r"The input date is not valid"):
        _ = get_events(year=1404, month=12, day=31, input_date_system=DateSystem.JALALI)


def test_date_error2():
    with pytest.raises(RokhValidationError, match=r"The input date is not valid"):
        _ = get_events(month=12, day=31, input_date_system=DateSystem.JALALI)


def test_date_error3():
    with pytest.raises(RokhValidationError, match=r"The input date is not valid"):
        _ = get_events(year=2026, month=2, day=31, input_date_system=DateSystem.GREGORIAN)


def test_date_error4():
    with pytest.raises(RokhValidationError, match=r"The input date is not valid"):
        _ = get_events(year=1445, month=12, day=31, input_date_system=DateSystem.HIJRI)
