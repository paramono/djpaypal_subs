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
    name='djpaypal_subs',
    version='0.3.3',
    python_requires='==3.*,>=3.5.0',
    author='paramono',
    author_email='alex@paramono.com',
    packages=[
        'djpaypal_subs', 'djpaypal_subs.management',
        'djpaypal_subs.management.commands', 'djpaypal_subs.migrations',
        'djpaypal_subs.models'
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=['paypalrestsdk==1.*,>=1.13.1'],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
