# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       True
#
#

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=['WebTest >= 1.2.3',
               'nose',
               'coverage',
               'wsgiref',
               'repoze.who-testutil >= 1.0.1',
               ]

install_requires=[
    "TurboGears2",
    "Mako",
    "zope.sqlalchemy >= 0.4",
    "repoze.tm2",
    "sqlalchemy",
    #"sqlalchemy-migrate",
    "repoze.what >= 1.0.8",
    "repoze.who-friendlyform >= 1.0.4",
    "repoze.what-pylons >= 1.0",
    "repoze.who",
    #"repoze.what-quickstart",
    "repoze.what.plugins.sql",
    "Pylons",  # This is madness
    "WebOb", # This is also madness
    #"tg.devtools",
    "bunch",
    "kitchen",
    "python-fedora",
    "pycurl",
    "tw2.core",
    #"tw2.jit",
    "tw2.jqplugins.gritter",
    "tw2.jqplugins.ui>=2.0b25",
    "docutils",
    #"tw.forms",     # TODO - What is pulling this in?
    ]

if sys.version_info[:2] == (2,4):
    testpkgs.extend(['hashlib', 'pysqlite'])
    install_requires.extend(['hashlib', 'pysqlite'])

setup(
    name='fedora-tagger',
    version='0.1',
    description='',
    author='',
    author_email='',
    #url='',
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2', 'tg.devtools'],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'fedoratagger': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 #'public/*/*'
                                 ]},
    message_extractors={'fedoratagger': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
            ('public/**', 'ignore', None)]},

    entry_points="""
    [paste.app_factory]
    main = fedoratagger.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [tw2.widgets]
    widgets = fedoratagger.widgets
    """,
    dependency_links=[
        "http://www.turbogears.org/2.1/downloads/current/"
        ],
    zip_safe=False
)
