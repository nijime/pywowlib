#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='pywowlib',
    version='1.0',
    description="pywowlib",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='https://github.com/wowdev/pywowlib',
    license='LGPL3',
    packages=find_packages(exclude=('tests', 'docs', 'venv'))
)
