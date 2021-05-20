#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='moarpalettes',
      version='1.0',
      # list folders, not files
      packages=find_packages(),
      install_requires=["matplotlib",
                        "seaborn",
      ],
      )
