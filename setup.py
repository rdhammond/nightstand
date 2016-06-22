#!/usr/bin/python

from setuptools import setup

setup(
    name = 'nightstand',
    version = '1.0.0',
    description = 'Clock, Weather, and more for the Raspberry Pi',
    author = 'R. Daniel Hammond',
    author_email = 'viztheman@gmail.com',
    url = 'https://github.com/rdhammond/nightstand.git',
    packages = ['nightstand'],
    package_data = {
        'package': [
            'nightstand/sprites/*',
            'nightstand/fonts/*'
        ]
    },
    install_requires = [
        'datetime',
        'pygame',
        'requests',
        'lxml',
        'cssselect'
    ],
    extra_requires = {
        'gpio': [
            'RPi.GPIO'
        ]
    }
)
