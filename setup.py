# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algdx_py',
    version='0.0.1',
    description="DxSter, the Alzheimer's Algorithmic Diagnostic Helper: Python Library",
    long_description=readme,
    author='Chris Barnes(senrabc@gmail.com), Kevin Hanson(kshanson@ufl.edu)',
    author_email='senrabc@gmail.com',
    url='https://github.com/senrabc/dxster',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
