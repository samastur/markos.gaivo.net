#!/usr/bin/env python
from setuptools import setup

requires = ['feedgenerator >= 1.6', 'jinja2 >= 2.7', 'pygments', 'docutils',
            'pytz >= 0a', 'blinker', 'unidecode', 'six >= 1.4',
            'python-dateutil']

entry_points = {
    'console_scripts': [
        'wp2pelican = wp2pelican.wpimport:main'
    ]
}


README = ""
CHANGELOG = ""
DESCRIPTION = "A tool to import WordPress content into Pelican",


setup(
    name="wp2pelican",
    version="0.9",
    author='Marko Samastur, Alexis Metaireau',
    author_email='markos@gaivo.net',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    packages=['wp2pelican'],
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
         'Environment :: Console',
         'License :: OSI Approved :: GNU Affero General Public License v3',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.3',
         'Programming Language :: Python :: 3.4',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
