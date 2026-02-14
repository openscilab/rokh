# -*- coding: utf-8 -*-
"""Hijri Events."""

EVENTS = {
    # ٱلْمُحَرَّم
    "1": {
        '1': [{'description': 'آغاز سال جدید هجری قمری', 'is_holiday': False},
              {'description': 'بزرگداشت محتشم کاشانی', 'is_holiday': False},
              {'description': 'روز شعر و ادبیات آیینی', 'is_holiday': False}],
        '2': [{'description': 'روز امر به معروف و نهی از منکر', 'is_holiday': False}],
        '9': [{'description': 'تاسوعای حسینی', 'is_holiday': True}],
        '10': [{'description': 'عاشورای حسینی', 'is_holiday': True}],
        '11': [{'description': 'تجلیل از اسرا و مفقودان', 'is_holiday': False}],
        '12': [{'description': 'شهادت امام زین العابدین علیه السلام', 'is_holiday': False}],
        '25': [{'description': 'شهادت امام زین‌العابدین (ع) به روایتی', 'is_holiday': False}]
    },
    # صَفَر
    "2": {
        '3': [{'description': 'ولادت امام محمدباقر (ع) به روایتی', 'is_holiday': False}],
        '7': [{'description': 'شهادت امام حسن مجتبی (ع) به روایتی', 'is_holiday': False},
              {'description': 'بزرگداشت سلمان فارسی', 'is_holiday': False}],
        '20': [{'description': 'اربعین حسینی', 'is_holiday': True}],
        '27': [{'description': 'روز وقف', 'is_holiday': False}],
        '28': [{'description': 'رحلت رسول اکرم', 'is_holiday': True},
               {'description': 'شهادت امام حسن مجتبی علیه السلام', 'is_holiday': True}],
        '30': [{'description': 'شهادت امام رضا علیه السلام', 'is_holiday': True}]
    },
    # رَبِيع ٱلْأَوَّل
    "3": {
        '1': [{'description': 'هجرت پیامبر اکرم از مکه به مدینه', 'is_holiday': False}],
        '8': [{'description': 'شهادت امام حسن عسکری علیه السلام', 'is_holiday': True},
              {'description': 'آغاز امامت حضرت ولیعصر (عج)', 'is_holiday': True}],
        '12': [{'description': 'میلاد رسول اکرم به روایت اهل سنت', 'is_holiday': False},
               {'description': 'آغاز هفته وحدت', 'is_holiday': False}],
        '14': [{'description': 'روز سیستان و بلوچستان', 'is_holiday': False}],
        '17': [{'description': 'میلاد رسول اکرم', 'is_holiday': True},
               {'description': 'ولادت امام جعفر صادق علیه السلام', 'is_holiday': True},
               {'description': 'روز اخلاق و مهرورزی', 'is_holiday': False}],
        '23': [{'description': 'روز قم', 'is_holiday': False}]
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
        '13': [{'description': 'سالروز وفات حضرت ام‌البنین (س)', 'is_holiday': False},
               {'description': 'روز تکریم مادران و همسران شهدا', 'is_holiday': False}],
        '20': [{'description': 'ولادت حضرت فاطمه زهرا سلام الله علیها و روز مادر', 'is_holiday': False}]
    },
    # رَجَب
    "7": {
        '1': [{'description': 'ولادت امام محمد باقر علیه السلام', 'is_holiday': False}],
        '3': [{'description': 'شهادت امام علی النقی علیه السلام', 'is_holiday': False}],
        '10': [{'description': 'ولادت امام محمد تقی علیه السلام', 'is_holiday': False}],
        '13': [{'description': 'ولادت امام علی علیه السلام و روز پدر', 'is_holiday': True},
               {'description': 'آغاز ایام البیض (اعتکاف)', 'is_holiday': False}],
        '15': [{'description': 'وفات حضرت زینب سلام الله علیها', 'is_holiday': False}],
        '25': [{'description': 'شهادت امام موسی کاظم علیه السلام', 'is_holiday': False}],
        '27': [{'description': 'مبعث رسول اکرم (ص)', 'is_holiday': True}]
    },
    # شَعْبَان
    "8": {
        '3': [{'description': 'ولادت سالار شهیدان، امام حسین علیه السلام و روز پاسدار', 'is_holiday': False}],
        '4': [{'description': 'ولادت ابوالفضل العباس علیه السلام و روز جانباز', 'is_holiday': False}],
        '5': [{'description': 'ولادت امام زین العابدین علیه السلام و روز صحیفه سجادیه', 'is_holiday': False}],
        '11': [{'description': 'ولادت علی اکبر علیه السلام و روز جوان', 'is_holiday': False}],
        '15': [{'description': 'ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان', 'is_holiday': True},
               {'description': 'روز جهانی مستضعفان', 'is_holiday': False},
               {'description': 'روز سربازان گمنام امام زمان (عج)', 'is_holiday': False}]
    },
    # رَمَضَان
    "9": {
        '10': [{'description': 'وفات حضرت خدیجه (س)', 'is_holiday': False}],
        '15': [{'description': 'ولادت امام حسن مجتبی علیه السلام و روز اکرام', 'is_holiday': False}],
        '18': [{'description': 'شب قدر', 'is_holiday': False}],
        '19': [{'description': 'ضربت خوردن حضرت علی علیه السلام و روز نهج البلاغه', 'is_holiday': False}],
        '20': [{'description': 'شب قدر', 'is_holiday': False}],
        '21': [{'description': 'شهادت حضرت علی علیه السلام', 'is_holiday': True}],
        '22': [{'description': 'شب قدر', 'is_holiday': False}],
    },
    # شَوَّال
    "10": {
        '1': [{'description': 'عید سعید فطر', 'is_holiday': True}],
        '2': [{'description': 'تعطیل به مناسبت عید سعید فطر', 'is_holiday': True}],
        '17': [{'description': 'روز فرهنگ پهلوانی و ورزش زورخانه‌ای', 'is_holiday': False}],
        '25': [{'description': 'شهادت امام جعفر صادق علیه السلام', 'is_holiday': True}]
    },
    # ذُو ٱلْقَعْدَة
    "11": {
        '1': [{'description': 'ولادت حضرت معصومه سلام الله علیها و روز دختران', 'is_holiday': False}],
        '5': [{'description': 'تجلیل از امامزادگان و بقاع متبرکه', 'is_holiday': False},
              {'description': 'بزرگداشت حضرت صالح بن موسی کاظم (ع)', 'is_holiday': False}],
        '6': [{'description': 'بزرگداشت حضرت احمد بن موسی شاهچراغ (ع)', 'is_holiday': False}],
        '11': [{'description': 'ولادت امام رضا علیه السلام', 'is_holiday': False}],
        '30': [{'description': 'شهادت امام محمد تقی علیه السلام', 'is_holiday': False}]
    },
    # ذُو ٱلْحِجَّة
    "12": {
        '1': [{'description': 'سالروز ازدواج حضرت علی (ع) و حضرت فاطمه (س) و روز ازدواج', 'is_holiday': False}],
        '6': [{'description': 'شهادت زائران خانه خدا به دست مأموران آل سعود', 'is_holiday': False}],
        '7': [{'description': 'شهادت امام محمد باقر علیه السلام', 'is_holiday': False}],
        '9': [{'description': 'روز عرفه', 'is_holiday': False}],
        '10': [{'description': 'عید سعید قربان', 'is_holiday': True},
               {'description': 'آغاز دهه امامت و ولایت', 'is_holiday': False}],
        '15': [{'description': 'ولادت امام علی النقی علیه السلام', 'is_holiday': False}],
        '18': [{'description': 'عید سعید غدیر خم', 'is_holiday': True}],
        '20': [{'description': 'ولادت امام موسی کاظم علیه السلام', 'is_holiday': False}],
        '24': [{'description': 'مباهله پیامبر اسلام (ص)', 'is_holiday': False}],
        '25': [{'description': 'روز خانواده و تکریم بازنشستگان', 'is_holiday': False}],
    }
}

