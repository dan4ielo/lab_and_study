# This file is used to install our project at a later stage

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':      'gothon web',
    'author':           'My name',
    'url':              'URL to get it at.',
    'download_url':     'Where to download it from',
    'author_email':     'My email',
    'version':          '0.1',
    'install_requires': ['nose'],
    'packages':         ['gothonweb'],
    'scripts':          [],
    'name':             'gothonweb'
}

setup(**config)
