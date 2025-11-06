from rokh import get_events, get_today_events, DateSystem
from rokh.events.jalali import EVENTS as JALALI_EVENTS
from rokh.events.gregorian import EVENTS as GREGORIAN_EVENTS
from rokh.events.hijri import EVENTS as HIJRI_EVENTS
import datetime
import jdatetime
import hijridate
TEST_CASE_NAME = "Gregorian tests"


def test_get_events_gregorian_gregorian():
    month = 1
    day = 1
    year = 2025
    result = get_events(
        day,
        month,
        year,
        input_date_system=DateSystem.GREGORIAN,
        event_date_system=DateSystem.GREGORIAN)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["gregorian"]
    assert result["event_date_system"] == "gregorian"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])


def test_get_events_gregorian_jalali():
    month = 1
    day = 1
    year = 2025
    result = get_events(day, month, year, input_date_system=DateSystem.GREGORIAN, event_date_system=DateSystem.JALALI)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["jalali"]
    assert result["event_date_system"] == "jalali"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])


def test_get_events_gregorian_hijri():
    month = 1
    day = 1
    year = 2025
    result = get_events(day, month, year, input_date_system=DateSystem.GREGORIAN, event_date_system=DateSystem.HIJRI)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["hijri"]
    assert result["event_date_system"] == "hijri"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_events_gregorian_all():
    month = 1
    day = 1
    year = 2025
    result = get_events(day, month, year, input_date_system=DateSystem.GREGORIAN)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_events_gregorian_all_current_year():
    today = datetime.datetime.now()
    month = 1
    day = 1
    year = today.year
    result = get_events(day, month, input_date_system=DateSystem.GREGORIAN)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_today_events_gregorian():
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year
    result = get_today_events(event_date_system=DateSystem.GREGORIAN)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["gregorian"]
    assert result["event_date_system"] == "gregorian"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])


def test_get_today_events_jalali():
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year
    result = get_today_events(event_date_system=DateSystem.JALALI)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["jalali"]
    assert result["event_date_system"] == "jalali"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])


def test_get_today_events_hijri():
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year
    result = get_today_events(event_date_system=DateSystem.HIJRI)
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["hijri"]
    assert result["event_date_system"] == "hijri"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_today_events_all():
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    year = today.year
    result = get_today_events()
    j = jdatetime.GregorianToJalali(year, month, day)
    h = hijridate.Gregorian(year, month, day).to_hijri()
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "gregorian"
    assert result["gregorian_date"]["year"] == year
    assert result["gregorian_date"]["month"] == month
    assert result["gregorian_date"]["day"] == day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(month), {}).get(str(day), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])
