#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.0.1"

setup(
    name="django-producer",
    version=version,
    description=("Can reproduce a new django app from yaml."),
    author="Dmitry Gerasimenko",
    author_email="kiddima@gmail.com",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
)
