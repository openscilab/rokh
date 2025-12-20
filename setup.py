# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires() -> list:
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description() -> str:
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''Rokh provides a unified interface for accessing Iranian calendar events across Jalali, Gregorian, and Hijri date systems. It lets you easily retrieve national holidays, cultural events, and religious occasions by simply passing a date. It automatically converts between calendars and return event's description.
You can use it in your apps, bots, and research tools that rely on Iranian date conversions, holidays, and cultural event data.

In Farsi, Rokh is derived from Rokhdad, meaning "event." Rokh itself also means “face” and even refers to the "rook" piece in chess.'''


setup(
    name='rokh',
    packages=['rokh', 'rokh.events'],
    version='0.3',
    description="Rokh: Iranian Calendar Events Collection",
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Rokh Development Team',
    author_email='rokh@openscilab.com',
    url='https://github.com/openscilab/rokh',
    download_url='https://github.com/openscilab/rokh/tarball/v0.3',
    keywords="events date date-system calendar gregorian hijri jalali",
    project_urls={
            'Source': 'https://github.com/openscilab/rokh',
    },
    install_requires=get_requires(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Natural Language :: Persian',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Topic :: Education',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Utilities',
    ],
    license='MIT',
)
