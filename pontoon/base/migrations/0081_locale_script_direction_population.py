# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 12:22
from __future__ import unicode_literals

from bulk_update.helper import bulk_update

from django.db import migrations


def add_locale_data(apps, schema_editor):
    Locale = apps.get_model('base', 'Locale')
    locales = Locale.objects.all()

    for l in locales:
        try:
            data = LOCALES[l.code]
            l.script = data.get('script')
            l.direction = data.get('direction', 'ltr')
            l.population = int(round(data.get('population') / 1000)) * 1000
        except KeyError:
            pass

    if locales:
        bulk_update(locales)


def remove_locale_data(apps, schema_editor):
    Locale = apps.get_model('base', 'Locale')
    locales = Locale.objects.all()

    for l in locales:
        l.script = 'Latin'
        l.direction = 'ltr'
        l.population = 0

    if locales:
        bulk_update(locales)


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0080_auto_20170127_0159'),
    ]

    operations = [
        migrations.RunPython(add_locale_data, remove_locale_data),
    ]


"""
Data taken from CLDR
https://github.com/unicode-cldr/cldr-core

for l in LOCALES:
  if '-' not in l:
    population = 0
    locale = l
    if l == "bm":
      locale = "bm_Latn"
    elif l == "bs":
      locale = "bs_Latn"
    elif l == "ha":
      locale = "ha_Latn"
    elif l == "uz":
      locale = "uz_Latn"
    elif l == "mn":
      locale = "mn_Cyrl"
    elif l == "ms":
      locale = "ms_Latn"
    elif l == "az":
      locale = "az_Latn"
    elif l == "sr":
      locale = "sr_Cyrl"
    elif l == "kk":
      locale = "kk_Cyrl"
    elif l == "ku":
      locale = "ku_Latn"
    for country in DATA:
      citizens = DATA[country]["_population"]
      try:
        percent = DATA[country]["languagePopulation"][locale]["_populationPercent"]
      except KeyError:
        percent = 0.0
      population += int(citizens) * float(percent) * 0.01
  else:
    population = 0
    country = l.split('-')[1]
    locale = l.split('-')[0]
    if country == "CN":
      locale = "zh_Hans"
    elif country == "TW":
      locale = "zh_Hant"
    elif country == "IN":
      locale = "pa_Guru"
    citizens = DATA[country]["_population"]
    try:
      percent = DATA[country]["languagePopulation"][locale]["_populationPercent"]
    except KeyError:
      percent = 0.0
    population += int(citizens) * float(percent) * 0.01
  # l['population'] = int(round(population))
  print l + ': ' + str(int(round(population)))
"""
LOCALES = {
    'pa-IN': {
        'population': 35047600,
        'script': 'Gurmukh??'
    },
    'gd': {
        'population': 63447,
        'script': 'Latin'
    },
    'gn': {
        'population': 5495633,
        'script': 'Latin'
    },
    'gl': {
        'population': 3385382,
        'script': 'Latin'
    },
    'ne-NP': {
        'population': 13882572,
        'script': 'Devanagari'
    },
    'en-GB': {
        'population': 63447318,
        'script': 'Latin'
    },
    'lg': {
        'population': 4823221,
        'script': 'Latin'
    },
    'ln': {
        'population': 2719180,
        'script': 'Latin'
    },
    'lo': {
        'population': 4768963,
        'script': 'Lao'
    },
    'tr': {
        'population': 77783465,
        'script': 'Latin'
    },
    'lv': {
        'population': 1211893,
        'script': 'Latin'
    },
    'tl': {
        'population': 28000000,
        'script': 'Latin'
    },
    'tsz': {
        'population': 125000,
        'script': 'Latin'
    },
    'th': {
        'population': 54381120,
        'script': 'Thai'
    },
    'te': {
        'population': 90122400,
        'script': 'Telugu'
    },
    'ta': {
        'population': 78710702,
        'script': 'Tamil'
    },
    'yo': {
        'population': 24303116,
        'script': 'Latin'
    },
    'bn': {
        'population': 200626440,
        'script': 'Bengali'
    },
    'bn-BD': {
        'population': 165578840,
        'script': 'Bengali'
    },
    'bn-IN': {
        'population': 35047600,
        'script': 'Bengali'
    },
    'de': {
        'population': 107183291,
        'script': 'Latin'
    },
    'ko': {
        'population': 74818637,
        'script': 'Korean'
    },
    'da': {
        'population': 6818223,
        'script': 'Latin'
    },
    'pt-BR': {
        'population': 185876600,
        'script': 'Latin'
    },
    'nb-NO': {
        'population': 5207690,
        'script': 'Latin'
    },
    'gu-IN': {
        'population': 35047600,
        'script': 'Gujarati'
    },
    'ga-IE': {
        'population': 538154,
        'script': 'Latin'
    },
    'es-CL': {
        'population': 17158134,
        'script': 'Latin'
    },
    'ilo': {
        'population': 9695808,
        'script': 'Latin'
    },
    'el': {
        'population': 12233270,
        'script': 'Greek'
    },
    'eo': {
        'population': 100000,
        'script': 'Latin'
    },
    'en': {
        'population': 1522575906,
        'script': 'Latin'
    },
    'ee': {
        'population': 4179930,
        'script': 'Latin'
    },
    'eu': {
        'population': 1049442,
        'script': 'Latin'
    },
    'et': {
        'population': 904473,
        'script': 'Latin'
    },
    'es': {
        'population': 454306855,
        'script': 'Latin'
    },
    'ru': {
        'population': 184764822,
        'script': 'Cyrillic'
    },
    'rm': {
        'population': 40609,
        'script': 'Latin'
    },
    'ro': {
        'population': 22511832,
        'script': 'Latin'
    },
    'dsb': {
        'population': 7034,
        'script': 'Latin'
    },
    'hsb': {
        'population': 12937,
        'script': 'Latin'
    },
    'be': {
        'population': 10182116,
        'script': 'Cyrillic'
    },
    'bg': {
        'population': 8107349,
        'script': 'Cyrillic'
    },
    'uk': {
        'population': 29629582,
        'script': 'Cyrillic'
    },
    'ast': {
        'population': 625899,
        'script': 'Latin'
    },
    'wo': {
        'population': 9793131,
        'script': 'Latin'
    },
    'bm': {
        'population': 7799530,
        'script': 'Latin'
    },
    'br': {
        'population': 552397,
        'script': 'Latin'
    },
    'bs': {
        'population': 3828389,
        'script': 'Latin'
    },
    'ja': {
        'population': 121002946,
        'script': 'Japanese'
    },
    'hy-AM': {
        'population': 2995252,
        'script': 'Armenian'
    },
    'pt-PT': {
        'population': 10392288,
        'script': 'Latin'
    },
    'es-AR': {
        'population': 43431900,
        'script': 'Latin'
    },
    'ach': {
        'population': 1372763,
        'script': 'Latin'
    },
    'oc': {
        'population': 1996614,
        'script': 'Latin'
    },
    'nn-NO': {
        'population': 1301923,
        'script': 'Latin'
    },
    'ltg': {
        'population': 176817,
        'script': 'Latin'
    },
    'fy-NL': {
        'population': 728760,
        'script': 'Latin'
    },
    'or': {
        'population': 40054400,
        'script': 'Odia'
    },
    'xh': {
        'population': 9680890,
        'script': 'Latin'
    },
    'nso': {
        'population': 5045506,
        'script': 'Latin'
    },
    'ta-LK': {
        'population': 3308025,
        'script': 'Tamil'
    },
    'ca': {
        'population': 8363274,
        'script': 'Latin'
    },
    'son': {
        'population': 4000000,
        'script': 'Latin'
    },
    'cy': {
        'population': 522144,
        'script': 'Latin'
    },
    'cs': {
        'population': 10431904,
        'script': 'Latin'
    },
    'lt': {
        'population': 2488708,
        'script': 'Latin'
    },
    'hi-IN': {
        'population': 35047600,
        'script': 'Devanagari'
    },
    'ak': {
        'population': 10267764,
        'script': 'Latin'
    },
    'pl': {
        'population': 38546852,
        'script': 'Latin'
    },
    'hr': {
        'population': 5728917,
        'script': 'Latin'
    },
    'en-US': {
        'population': 308514240,
        'script': 'Latin'
    },
    'ht': {
        'population': 8189100,
        'script': 'Latin'
    },
    'hu': {
        'population': 12548563,
        'script': 'Latin'
    },
    'ha': {
        'population': 31230847,
        'script': 'Latin'
    },
    'he': {
        'direction': 'rtl',
        'population': 8049310,
        'script': 'Hebrew'
    },
    'mg': {
        'population': 21431430,
        'script': 'Latin'
    },
    'fur': {
        'population': 37113,
        'script': 'Latin'
    },
    'uz': {
        'population': 25292728,
        'script': 'Latin'
    },
    'ml': {
        'population': 40596390,
        'script': 'Malayalam'
    },
    'mn': {
        'population': 2785543,
        'script': 'Cyrillic'
    },
    'mk': {
        'population': 1590981,
        'script': 'Cyrillic'
    },
    'ur': {
        'direction': 'rtl',
        'population': 251786371,
        'script': 'Arabic'
    },
    'cak': {
        'population': 450000,
        'script': 'Latin'
    },
    'zh-CN': {
        'population': 1230741000,
        'script': 'Simplified Chinese'
    },
    'zh-HK': {
        'population': 6784055,
        'script': 'Traditional Chinese'
    },
    'zh-TW': {
        'population': 22244345,
        'script': 'Traditional Chinese'
    },
    'en-ZA': {
        'population': 16639436,
        'script': 'Latin'
    },
    'ms': {
        'population': 24079347,
        'script': 'Latin'
    },
    'mr': {
        'population': 87619000,
        'script': 'Devanagari'
    },
    'my': {
        'population': 36399740,
        'script': 'Myanmar'
    },
    'af': {
        'population': 8642954,
        'script': 'Latin'
    },
    'vi': {
        'population': 82239460,
        'script': 'Latin'
    },
    'is': {
        'population': 331918,
        'script': 'Latin'
    },
    'it': {
        'population': 69025171,
        'script': 'Latin'
    },
    'an': {
        'population': 54000,
        'script': 'Latin'
    },
    'as': {
        'population': 16272100,
        'script': 'Bengali'
    },
    'ar': {
        'direction': 'rtl',
        'population': 304854166,
        'script': 'Arabic'
    },
    'sv-SE': {
        'population': 9311539,
        'script': 'Latin'
    },
    'az': {
        'population': 9292560,
        'script': 'Latin'
    },
    'es-ES': {
        'population': 47664639,
        'script': 'Latin'
    },
    'id': {
        'population': 164141222,
        'script': 'Latin'
    },
    'ig': {
        'population': 23603060,
        'script': 'Latin'
    },
    'sr': {
        'population': 7617631,
        'script': 'Cyrillic'
    },
    'nl': {
        'population': 31184917,
        'script': 'Latin'
    },
    'lij': {
        'population': 531954,
        'script': 'Latin'
    },
    'csb': {
        'population': 50131,
        'script': 'Latin'
    },
    'zu': {
        'population': 13313524,
        'script': 'Latin'
    },
    'kab': {
        'population': 3084292,
        'script': 'Latin'
    },
    'fr': {
        'population': 231632800,
        'script': 'Latin'
    },
    'fa': {
        'direction': 'rtl',
        'population': 79732772,
        'script': 'Arabic'
    },
    'ff': {
        'population': 7057393,
        'script': 'Latin'
    },
    'mai': {
        'population': 18491043,
        'script': 'Devanagari'
    },
    'fi': {
        'population': 5381031,
        'script': 'Latin'
    },
    'ka': {
        'population': 4343425,
        'script': 'Georgian'
    },
    'kk': {
        'population': 11621179,
        'script': 'Cyrillic'
    },
    'sq': {
        'population': 6715994,
        'script': 'Latin'
    },
    'sw': {
        'population': 143997344,
        'script': 'Latin'
    },
    'kn': {
        'population': 46312900,
        'script': 'Kannada'
    },
    'km': {
        'population': 13980832,
        'script': 'Khmer'
    },
    'es-MX': {
        'population': 101041710,
        'script': 'Latin'
    },
    'sk': {
        'population': 4972417,
        'script': 'Latin'
    },
    'si': {
        'population': 14996380,
        'script': 'Sinhalese'
    },
    'ku': {
        'population': 6456289,
        'script': 'Latin'
    },
    'sl': {
        'population': 1867732,
        'script': 'Latin'
    },
    'am': {
        'population': 37572806,
        'script': 'Ethiopic'
    }
}
