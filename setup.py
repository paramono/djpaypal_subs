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
    version='0.1.0',
    python_requires='==3.*,>=3.5.0',
    author='paramono',
    author_email='alex@paramono.com',
    packages=['djpaypal_subs'],
    package_dir={"": "."},
    package_data={},
    install_requires=['attrs==19.*,>=19.3.0'],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
