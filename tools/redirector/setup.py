#!/usr/bin/env python
from setuptools import setup

entry_points = {
    'console_scripts': [
        'redirector = redirector.redirector:main'
    ]
}


README = ""
CHANGELOG = ""
DESCRIPTION = "A tool to generate .htaccess redirects file for ID based site",


setup(
    name="redirector",
    version="0.9",
    author='Marko Samastur, Alexis Metaireau',
    author_email='markos@gaivo.net',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    packages=['redirector'],
    include_package_data=True,
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
