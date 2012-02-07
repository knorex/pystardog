#!/usr/bin/env python

from distutils.core import setup

# Install yardflib
from pystardog import __version__

setup(
    name = 'pystardog',
    version = __version__,
    description = "pystardog - Python client library for Stardog",
    author = "Knorex",
    author_email = "info@knorex.com",
    maintainer = "Huy Phan",
    maintainer_email = "dachuy@gmail.com",
    url = "http://github.com/knorex/pystardog",
    license = "MPL License",
    platforms = ["any"],
    classifiers = ["Programming Language :: Python",
                   "License :: MPL License",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Operating System :: OS Independent",
                   "Natural Language :: English",
                   ],
    long_description = \
    """
    """,
    download_url = "",

    py_modules=['pystardog']

    )
