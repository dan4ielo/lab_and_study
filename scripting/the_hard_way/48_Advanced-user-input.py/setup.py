# This file is used to install our project at a later stage

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':      'Advanced user input',
    'author':           'My name',
    'url':              'URL to get it at.',
    'download_url':     'Where to download it from',
    'author_email':     'My email',
    'version':          '0.1',
    'install_requires': ['nose'],
    'packages':         ['user_input']
    'scripts':          [],
    'name':             'projectname'
}

setup(**config)
