<div align="center">
    <img src="https://github.com/openscilab/rokh/raw/main/otherfiles/logo.png" alt="Rokh Logo" width="250">
    <h1>Rokh: Iranian Calendar Events Collection</h1>
    <br/>
    <a href="https://codecov.io/gh/openscilab/rokh"><img src="https://codecov.io/gh/openscilab/rokh/graph/badge.svg?token=9AH3WVVWF4"></a>
    <a href="https://badge.fury.io/py/rokh"><img src="https://badge.fury.io/py/rokh.svg" alt="PyPI version"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
    <a href="https://github.com/openscilab/rokh"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/openscilab/rokh"></a>
    <a href="https://discord.gg/G73QMkmVzg"><img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel"></a>
</div>

----------


## Overview
<p align="justify">
Rokh provides a unified interface for accessing Iranian calendar events across Jalali, Gregorian, and Hijri date systems. It lets you easily retrieve national holidays, cultural events, and religious occasions by simply passing a date. It automatically converts between calendars and return event's description.
You can use it in your apps, bots, and research tools that rely on Iranian date conversions, holidays, and cultural event data.

In Farsi, Rokh is derived from Rokhdad, meaning "event." Rokh itself also means "face" and even refers to the "rook" piece in chess.

</p>

<table>
    <tr>
        <td align="center">PyPI Counter</td>
        <td align="center">
            <a href="https://pepy.tech/projects/rokh">
                <img src="https://static.pepy.tech/badge/rokh">
            </a>
        </td>
    </tr>
    <tr>
        <td align="center">Github Stars</td>
        <td align="center">
            <a href="https://github.com/openscilab/rokh">
                <img src="https://img.shields.io/github/stars/openscilab/rokh.svg?style=social&label=Stars">
            </a>
        </td>
    </tr>
</table>
<table>
    <tr> 
        <td align="center">Branch</td>
        <td align="center">main</td>
        <td align="center">dev</td>
    </tr>
    <tr>
        <td align="center">CI</td>
        <td align="center">
            <img src="https://github.com/openscilab/rokh/actions/workflows/test.yml/badge.svg?branch=main">
        </td>
        <td align="center">
            <img src="https://github.com/openscilab/rokh/actions/workflows/test.yml/badge.svg?branch=dev">
        </td>
    </tr>
</table>
<table>
    <tr> 
        <td align="center">Code Quality</td>
        <td align="center"><a href="https://www.codefactor.io/repository/github/openscilab/rokh"><img src="https://www.codefactor.io/repository/github/openscilab/rokh/badge" alt="CodeFactor"></a></td>
        <td align="center"><a href="https://app.codacy.com/gh/openscilab/rokh/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ea874378ce94451f81ef30732c68216c"></a></td>
    </tr>
</table>


## Installation

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install rokh==0.3`
### Source code
- Download [Version 0.3](https://github.com/openscilab/rokh/archive/v0.3.zip) or [Latest Source](https://github.com/openscilab/rokh/archive/dev.zip)
- Run `pip install .`

## Usage


### Get events

Use `get_events` to retrieve all Iranian calendar events for a given date.
Simply specify the date (in Jalali, Gregorian, or Hijri format), and the function returns corresponding events.

```pycon
>>> from rokh import get_events, DateSystem
>>> get_events(day=1, month=1, year=1403, input_date_system=DateSystem.JALALI)
# {
#    'events': {
#      'gregorian': [
#        {
#          'description': 'روز جهانی شادی',
#          'is_holiday': False
#        }
#      ],
#      'hijri': [],
#      'jalali': [
#        {
#          'description': 'جشن نوروز/جشن سال نو',
#          'is_holiday': True
#        }
#      ]
#    },
#    'gregorian_date': {'day': 20, 'month': 3, 'year': 2024},
#    'hijri_date': {'day': 10, 'month': 9, 'year': 1445},
#    'jalali_date': {'day': 1, 'month': 1, 'year': 1403},
#    'is_holiday': True,
#    'input_date_system': 'jalali',
#    'event_date_system': 'all'
# }
```

### Get today events

Use `get_today_events` to retrieve today events.

```pycon
>>> from rokh import get_today_events, DateSystem
>>> get_today_events()
# {
#    'events': {
#      'gregorian': [
#        {
#          'description': 'روز جهانی شادی',
#          'is_holiday': False
#        }
#      ],
#      'hijri': [],
#      'jalali': [
#        {
#          'description': 'جشن نوروز/جشن سال نو',
#          'is_holiday': True
#        }
#      ]
#    },
#    'gregorian_date': {'day': 20, 'month': 3, 'year': 2024},
#    'hijri_date': {'day': 10, 'month': 9, 'year': 1445},
#    'jalali_date': {'day': 1, 'month': 1, 'year': 1403},
#    'is_holiday': True,
#    'input_date_system': 'gregorian',
#    'event_date_system': 'all'
# }
```


## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [rokh@openscilab.com](mailto:rokh@openscilab.com "rokh@openscilab.com"). 

- Please complete the issue template

You can also join our discord server

<a href="https://discord.gg/G73QMkmVzg">
  <img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel">
</a>


## References

<blockquote>1- <a href="https://www.time.ir/">ساعت و تقویم ایران | تاریخ امروز | Time.ir</a></blockquote>
<blockquote>2- <a href="https://holidayapi.ir/">Jalali Holiday API</a></blockquote>
<blockquote>3- <a href="https://www.un.org/en/observances/list-days-weeks">United Nations List of International Days and Weeks</a></blockquote>


## Show your support


### Star this repo

Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/rokh/raw/main/otherfiles/donation.png" width="270" alt="Rokh Donation"></a>