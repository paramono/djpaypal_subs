# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='djpp',
    version='0.3.9',
    python_requires='==3.*,>=3.5.0',
    author='paramono',
    author_email='alex@paramono.com',
    packages=[
        'djpp', 'djpp.management', 'djpp.management.commands',
        'djpp.migrations', 'djpp.models'
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=['paypalrestsdk==1.*,>=1.13.1'],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
