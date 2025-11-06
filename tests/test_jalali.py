from rokh import get_events, DateSystem
from rokh.events.jalali import EVENTS as JALALI_EVENTS
from rokh.events.gregorian import EVENTS as GREGORIAN_EVENTS
from rokh.events.hijri import EVENTS as HIJRI_EVENTS
import jdatetime
import hijridate
TEST_CASE_NAME = "Jalali tests"


def test_get_events_jalali_gregorian():
    month = 1
    day = 1
    year = 1404
    result = get_events(day, month, year, input_date_system=DateSystem.JALALI, event_date_system=DateSystem.GREGORIAN)
    g = jdatetime.JalaliToGregorian(year, month, day)
    h = hijridate.Gregorian(g.gyear, g.gmonth, g.gday).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["gregorian"]
    assert result["event_date_system"] == "gregorian"
    assert result["input_date_system"] == "jalali"
    assert result["gregorian_date"]["year"] == g.gyear
    assert result["gregorian_date"]["month"] == g.gmonth
    assert result["gregorian_date"]["day"] == g.gday
    assert result["jalali_date"]["year"] == year
    assert result["jalali_date"]["month"] == month
    assert result["jalali_date"]["day"] == day
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.gmonth), {}).get(str(g.gday), [])


def test_get_events_jalali_jalali():
    month = 1
    day = 1
    year = 1404
    result = get_events(day, month, year, input_date_system=DateSystem.JALALI, event_date_system=DateSystem.JALALI)
    g = jdatetime.JalaliToGregorian(year, month, day)
    h = hijridate.Gregorian(g.gyear, g.gmonth, g.gday).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["jalali"]
    assert result["event_date_system"] == "jalali"
    assert result["input_date_system"] == "jalali"
    assert result["gregorian_date"]["year"] == g.gyear
    assert result["gregorian_date"]["month"] == g.gmonth
    assert result["gregorian_date"]["day"] == g.gday
    assert result["jalali_date"]["year"] == year
    assert result["jalali_date"]["month"] == month
    assert result["jalali_date"]["day"] == day
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(month), {}).get(str(day), [])


def test_get_events_jalali_hijri():
    month = 1
    day = 1
    year = 1404
    result = get_events(day, month, year, input_date_system=DateSystem.JALALI, event_date_system=DateSystem.HIJRI)
    g = jdatetime.JalaliToGregorian(year, month, day)
    h = hijridate.Gregorian(g.gyear, g.gmonth, g.gday).to_hijri()
    assert isinstance(result, dict)
    assert list(result["events"].keys()) == ["hijri"]
    assert result["event_date_system"] == "hijri"
    assert result["input_date_system"] == "jalali"
    assert result["gregorian_date"]["year"] == g.gyear
    assert result["gregorian_date"]["month"] == g.gmonth
    assert result["gregorian_date"]["day"] == g.gday
    assert result["jalali_date"]["year"] == year
    assert result["jalali_date"]["month"] == month
    assert result["jalali_date"]["day"] == day
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_events_jalali_all():
    month = 1
    day = 1
    year = 1404
    result = get_events(day, month, year, input_date_system=DateSystem.JALALI)
    g = jdatetime.JalaliToGregorian(year, month, day)
    h = hijridate.Gregorian(g.gyear, g.gmonth, g.gday).to_hijri()
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "jalali"
    assert result["gregorian_date"]["year"] == g.gyear
    assert result["gregorian_date"]["month"] == g.gmonth
    assert result["gregorian_date"]["day"] == g.gday
    assert result["jalali_date"]["year"] == year
    assert result["jalali_date"]["month"] == month
    assert result["jalali_date"]["day"] == day
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.gmonth), {}).get(str(g.gday), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(month), {}).get(str(day), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])


def test_get_events_jalali_all_current_year():
    today = jdatetime.datetime.now()
    month = 1
    day = 1
    year = today.year
    result = get_events(day, month, input_date_system=DateSystem.JALALI)
    g = jdatetime.JalaliToGregorian(year, month, day)
    h = hijridate.Gregorian(g.gyear, g.gmonth, g.gday).to_hijri()
    assert isinstance(result, dict)
    assert set(result["events"].keys()) == {"hijri", "jalali", "gregorian"}
    assert result["event_date_system"] == "all"
    assert result["input_date_system"] == "jalali"
    assert result["gregorian_date"]["year"] == g.gyear
    assert result["gregorian_date"]["month"] == g.gmonth
    assert result["gregorian_date"]["day"] == g.gday
    assert result["jalali_date"]["year"] == year
    assert result["jalali_date"]["month"] == month
    assert result["jalali_date"]["day"] == day
    assert result["hijri_date"]["year"] == h.year
    assert result["hijri_date"]["month"] == h.month
    assert result["hijri_date"]["day"] == h.day
    assert result["events"]["gregorian"] == GREGORIAN_EVENTS.get(str(g.gmonth), {}).get(str(g.gday), [])
    assert result["events"]["jalali"] == JALALI_EVENTS.get(str(month), {}).get(str(day), [])
    assert result["events"]["hijri"] == HIJRI_EVENTS.get(str(h.month), {}).get(str(h.day), [])
