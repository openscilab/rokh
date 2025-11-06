from rokh import get_events, DateSystem
from rokh.events.jalali import EVENTS as JALALI_EVENTS
from rokh.events.gregorian import EVENTS as GREGORIAN_EVENTS
from rokh.events.hijri import EVENTS as HIJRI_EVENTS
import datetime
import jdatetime
import hijridate
TEST_CASE_NAME = "Hijri tests"


def test_get_events_hijri_gregorian():
    month = 1
    day = 1
    year = 1447
    result = get_events(day, month, year, input_date_system=DateSystem.HIJRI, event_date_system=DateSystem.GREGORIAN)
    g = hijridate.Hijri(year, month, day).to_gregorian()
    j = jdatetime.GregorianToJalali(g.year, g.month, g.day)
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["gregorian"]
    assert result["event_date_system"] == "gregorian"
    assert result["input_date_system"] == "hijri"
    assert result["gregorian_date"]["year"] == g.year
    assert result["gregorian_date"]["month"] == g.month
    assert result["gregorian_date"]["day"] == g.day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == year
    assert result["hijri_date"]["month"] == month
    assert result["hijri_date"]["day"] == day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.month), {}).get(str(g.day), [])


def test_get_events_hijri_jalali():
    month = 1
    day = 1
    year = 1447
    result = get_events(day, month, year, input_date_system=DateSystem.HIJRI, event_date_system=DateSystem.JALALI)
    g = hijridate.Hijri(year, month, day).to_gregorian()
    j = jdatetime.GregorianToJalali(g.year, g.month, g.day)
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["jalali"]
    assert result["event_date_system"] == "jalali"
    assert result["input_date_system"] == "hijri"
    assert result["gregorian_date"]["year"] == g.year
    assert result["gregorian_date"]["month"] == g.month
    assert result["gregorian_date"]["day"] == g.day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == year
    assert result["hijri_date"]["month"] == month
    assert result["hijri_date"]["day"] == day
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])


def test_get_events_hijri_hijri():
    month = 1
    day = 1
    year = 1447
    result = get_events(day, month, year, input_date_system=DateSystem.HIJRI, event_date_system=DateSystem.HIJRI)
    g = hijridate.Hijri(year, month, day).to_gregorian()
    j = jdatetime.GregorianToJalali(g.year, g.month, g.day)
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["hijri"]
    assert result["event_date_system"] == "hijri"
    assert result["input_date_system"] == "hijri"
    assert result["gregorian_date"]["year"] == g.year
    assert result["gregorian_date"]["month"] == g.month
    assert result["gregorian_date"]["day"] == g.day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == year
    assert result["hijri_date"]["month"] == month
    assert result["hijri_date"]["day"] == day
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(month), {}).get(str(day), [])


def test_get_events_hijri_all():
    month = 1
    day = 1
    year = 1447
    result = get_events(day, month, year, input_date_system=DateSystem.HIJRI)
    g = hijridate.Hijri(year, month, day).to_gregorian()
    j = jdatetime.GregorianToJalali(g.year, g.month, g.day)
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "hijri"
    assert result["gregorian_date"]["year"] == g.year
    assert result["gregorian_date"]["month"] == g.month
    assert result["gregorian_date"]["day"] == g.day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == year
    assert result["hijri_date"]["month"] == month
    assert result["hijri_date"]["day"] == day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.month), {}).get(str(g.day), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(month), {}).get(str(day), [])


def test_get_events_hijri_all_current_year():
    today = datetime.datetime.now()
    month = 1
    day = 1
    year = hijridate.Gregorian(today.year, today.month, today.day).to_hijri().year
    result = get_events(day, month, input_date_system=DateSystem.HIJRI)
    g = hijridate.Hijri(year, month, day).to_gregorian()
    j = jdatetime.GregorianToJalali(g.year, g.month, g.day)
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "hijri"
    assert result["gregorian_date"]["year"] == g.year
    assert result["gregorian_date"]["month"] == g.month
    assert result["gregorian_date"]["day"] == g.day
    assert result["jalali_date"]["year"] == j.jyear
    assert result["jalali_date"]["month"] == j.jmonth
    assert result["jalali_date"]["day"] == j.jday
    assert result["hijri_date"]["year"] == year
    assert result["hijri_date"]["month"] == month
    assert result["hijri_date"]["day"] == day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.month), {}).get(str(g.day), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(j.jmonth), {}).get(str(j.jday), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(month), {}).get(str(day), [])
