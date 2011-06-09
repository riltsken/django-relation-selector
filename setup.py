#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-relation-selector',
    version="0.0",
    author='Samuel Toriel',
    author_email='samueltoriel@gmail.com',
    description='Select fields / relations given an app label and model label',
    url='http://github.com/riltsken/django-relation-selector',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
