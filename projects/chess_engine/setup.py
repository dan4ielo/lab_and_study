# This file is used to install our project at a later stage

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':      'Chess Engine',
    'author':           'dan4ielo',
    'url':              'github.com/dan4ielo/lab_and_study',
    'download_url':     'N/A',
    'author_email':     'dan4ielo@protonmail.com',
    'version':          '0.1',
    'install_requires': ['nose'],
    'packages':         ['chess'],
    'scripts':          [],
    'name':             'chess'
}

setup(**config)
