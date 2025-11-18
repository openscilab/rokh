# -*- coding: utf-8 -*-
"""Hijri Events."""

EVENTS = {
    # ٱلْمُحَرَّم
    "1": {
        '9': [{'description': 'تاسوعای حسینی', 'is_holiday': True}],
        '10': [{'description': 'عاشورای حسینی', 'is_holiday': True}],
        '12': [{'description': 'شهادت امام زین العابدین علیه السلام', 'is_holiday': False}]
    },
    # صَفَر
    "2": {
        '20': [{'description': 'اربعین حسینی', 'is_holiday': True}],
        '28': [{'description': 'رحلت رسول اکرم', 'is_holiday': True},
               {'description': 'شهادت امام حسن مجتبی علیه السلام', 'is_holiday': True}],
        '30': [{'description': 'شهادت امام رضا علیه السلام', 'is_holiday': True}]
    },
    # رَبِيع ٱلْأَوَّل
    "3": {
        '1': [{'description': 'هجرت پیامبر اکرم از مکه به مدینه', 'is_holiday': False}],
        '8': [{'description': 'شهادت امام حسن عسکری علیه السلام', 'is_holiday': True}],
        '12': [{'description': 'میلاد رسول اکرم به روایت اهل سنت', 'is_holiday': False}],
        '17': [{'description': 'میلاد رسول اکرم', 'is_holiday': True},
               {'description': 'ولادت امام جعفر صادق علیه السلام', 'is_holiday': True}]
    },
    # رَبِيع ٱلثَّانِي
    "4": {
        '8': [{'description': 'ولادت امام حسن عسکری علیه السلام', 'is_holiday': False}],
        '10': [{'description': 'وفات حضرت معصومه سلام الله علیها', 'is_holiday': False}]
    },
    # جُمَادَىٰ ٱلْأُولَىٰ
    "5": {
        '5': [{'description': 'ولادت حضرت زینب سلام الله علیها و روز پرستار و بهورز', 'is_holiday': False}]
    },
    # جُمَادَىٰ ٱلثَّانِيَة
    "6": {
        '3': [{'description': 'شهادت حضرت فاطمه زهرا سلام الله علیها', 'is_holiday': True}],
        '20': [{'description': 'ولادت حضرت فاطمه زهرا سلام الله علیها و روز مادر', 'is_holiday': False}]
    },
    # رَجَب
    "7": {
        '1': [{'description': 'ولادت امام محمد باقر علیه السلام', 'is_holiday': False}],
        '3': [{'description': 'شهادت امام علی النقی علیه السلام', 'is_holiday': False}],
        '10': [{'description': 'ولادت امام محمد تقی علیه السلام', 'is_holiday': False}],
        '13': [{'description': 'ولادت امام علی علیه السلام و روز پدر', 'is_holiday': True}],
        '15': [{'description': 'وفات حضرت زینب سلام الله علیها', 'is_holiday': False}],
        '25': [{'description': 'شهادت امام موسی کاظم علیه السلام', 'is_holiday': False}],
        '27': [{'description': 'مبعث رسول اکرم (ص)', 'is_holiday': True}]
    },
    # شَعْبَان
    "8": {
        '3': [{'description': 'ولادت سالار شهیدان، امام حسین علیه السلام و روز پاسدار', 'is_holiday': False}],
        '4': [{'description': 'ولادت ابوالفضل العباس علیه السلام و روز جانباز', 'is_holiday': False}],
        '5': [{'description': 'ولادت امام زین العابدین علیه السلام', 'is_holiday': False}],
        '11': [{'description': 'ولادت علی اکبر علیه السلام و روز جوان', 'is_holiday': False}],
        '15': [{'description': 'ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان', 'is_holiday': True}]
    },
    # رَمَضَان
    "9": {
        '15': [{'description': 'ولادت امام حسن مجتبی علیه السلام', 'is_holiday': False}],
        '18': [{'description': 'شب قدر', 'is_holiday': False}],
        '19': [{'description': 'ضربت خوردن حضرت علی علیه السلام', 'is_holiday': False}],
        '21': [{'description': 'شهادت حضرت علی علیه السلام', 'is_holiday': True}],
        '22': [{'description': 'شب قدر', 'is_holiday': False}]
    },
    # شَوَّال
    "10": {
        '1': [{'description': 'عید سعید فطر', 'is_holiday': True}],
        '2': [{'description': 'تعطیل به مناسبت عید سعید فطر', 'is_holiday': True}],
        '25': [{'description': 'شهادت امام جعفر صادق علیه السلام', 'is_holiday': True}]
    },
    # ذُو ٱلْقَعْدَة
    "11": {
        '1': [{'description': 'ولادت حضرت معصومه سلام الله علیها و روز دختران', 'is_holiday': False}],
        '11': [{'description': 'ولادت امام رضا علیه السلام', 'is_holiday': False}],
        '30': [{'description': 'شهادت امام محمد تقی علیه السلام', 'is_holiday': False}]
    },
    # ذُو ٱلْحِجَّة
    "12": {
        '7': [{'description': 'شهادت امام محمد باقر علیه السلام', 'is_holiday': False}],
        '9': [{'description': 'روز عرفه', 'is_holiday': False}],
        '10': [{'description': 'عید سعید قربان', 'is_holiday': True}],
        '15': [{'description': 'ولادت امام علی النقی علیه السلام', 'is_holiday': False}],
        '18': [{'description': 'عید سعید غدیر خم', 'is_holiday': True}],
        '20': [{'description': 'ولادت امام موسی کاظم علیه السلام', 'is_holiday': False}]
    }
}

