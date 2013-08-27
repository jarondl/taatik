#!/usr/bin/env python3

from distutils.core import setup

setup(name = 'taatik',
      version = '1.0',
      description = 'translitertion of filenames from Herbrew letters to Latin letters',
      long_description = (open('README.md').read()),
      author = 'Yaron de Leeuw',
      author_email = 'jdlmail at gmail com',
      url = 'https://github.com/jarondl/taatik',
      scripts = ['taatik'],
      license = 'GPLv3+',
      classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Information Technology",
            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
            "Natural Language :: Hebrew",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3"
                ]
     )
