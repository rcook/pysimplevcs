#!/usr/bin/env python
############################################################
#
# pyvcs
# Copyright (C) 2017, Richard Cook
# Release under MIT License
# https://github.com/rcook/pyvcs
#
############################################################

from __future__ import print_function
from setuptools import setup

setup(
    name="pyvcs",
    version="0.1",
    description="Python helpers for interacting with VCSs",
    setup_requires=["setuptools-markdown"],
    long_description_markdown_filename="README.md",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    url="https://github.com/rcook/pyvcs",
    author="Richard Cook",
    author_email="rcook@rcook.org",
    license="MIT",
    packages=["pyvcs"],
    include_package_data=True,
    test_suite="pyvcs.tests.suite",
    zip_safe=False)
