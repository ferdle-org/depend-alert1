#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file for package.
"""

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='lma-elasticsearch-setup',
      version='0.1.0',
      description='Setup and configure a new Elasticsearch Cloud deployment',
      author='LMA Team',
      author_email='lma@metoffice.gov.uk',
      long_description=README,
      packages=find_packages(exclude=["tests", "*test*"]),
      install_requires=[
          'PyYAML'
      ],
      include_package_data=True)
