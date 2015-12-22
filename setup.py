#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-',
    version='0.1',
    description='A django otp plugin for google authenticator support',
    long_description=open('README.rst').read(),
    author='Bryan Haakman',
    author_email='bryan@zimmermanzimmerman.nl',
    packages=find_packages(),
    include_package_data=True,
    url='http://www.example.com',
    license='BSD',
    install_requires=[
        'django-otp >= 0.3.3',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)
