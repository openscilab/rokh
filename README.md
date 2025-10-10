<div align="center">
    <img src="https://github.com/openscilab/rokh/raw/main/otherfiles/logo.png" alt="Rokh Logo" width="220">
    <h1>Rokh: Iranian Calendar Events Collection</h1>
    <br/>
    <a href="https://badge.fury.io/py/rokh"><img src="https://badge.fury.io/py/rokh.svg" alt="PyPI version"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
    <a href="https://github.com/openscilab/rokh"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/openscilab/rokh"></a>

</div>

----------


## Overview
<p align="justify">
Rokh provides a unified interface for accessing Iranian calendar events across Jalali, Gregorian, and Hijri Ghamari date systems. It lets you easily retrieve national holidays, cultural events, and religious occasions by simply passing a date. It automatically converts between calendars and return event's description.
You can use it in your apps, bots, and research tools that rely on Iranian date conversions, holidays, and cultural event data.

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


## Installation

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install rokh==0.1`
### Source code
- Download [Version 0.1](https://github.com/openscilab/rokh/archive/v0.1.zip) or [Latest Source](https://github.com/openscilab/rokh/archive/dev.zip)
- Run `pip install .`

## Usage

Use `get_events` to retrieve all Iranian calendar events for a given date.
Simply specify the date (in Jalali, Gregorian, or Hijri format), and the function returns corresponding events.

```pycon
>> from rokh import get_events, DateSystem
>> result = get_events(day=1, month=1, year=1403, input_date_system=DateSystem.JALALI)
# {'events': {'gregorian': [{'description': 'روز جهانی شادی',
#                            'is_holiday': False}],
#             'hijri': [],
#             'jalali': [{'description': 'جشن نوروز/جشن سال نو',
#                         'is_holiday': True}]},
#  'gregorian_date': {'day': 20, 'month': 3, 'year': 2024},
#  'hijri_date': {'day': 10, 'month': 9, 'year': 1445},
#  'jalali_date': {'day': 1, 'month': 1, 'year': 1403},
#  'is_holiday': True,
#  'input_date_system': 'jalali',
#  'event_date_system': 'all'}
```

## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [rokh@openscilab.com](mailto:rokh@openscilab.com "rokh@openscilab.com"). 

- Please complete the issue template


## Show your support


### Star this repo

Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/rokh/raw/main/otherfiles/donation.png" width="270" alt="Rokh Donation"></a>