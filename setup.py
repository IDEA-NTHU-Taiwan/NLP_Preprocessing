# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NLP_Preprocessing',
    version='0.0.1',
    description='Preprocessing module for NLP',
    long_description=readme,
    author='IDEA Lab - NTHU',
    url='https://github.com/IDEALAB',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
