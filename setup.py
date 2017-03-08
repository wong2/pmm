# -*-coding:utf-8-*-

import os
import sys
from setuptools import setup


def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath, 'r') as fp:
        return fp.read()


required = [
    'pip',
    'crayons',
    'blindspin',
    'requests',
    'pick',
]

if sys.version_info < (2, 7):
    required.append('ordereddict')
if sys.version_info < (3, 2):
    required.append('configparser')


setup(
    name='pmm',
    version='0.5.0',
    description='PyPI Mirror and Index Server Manager',
    long_description=fread('README.md'),
    keywords='pypi,mirror',
    url='https://github.com/wong2/pmm',
    author='wong2',
    author_email='wonderfuly@gmail.com',
    license='MIT',
    install_requires=required,
    packages=['pmm'],
    entry_points={
        'console_scripts': ['pmm=pmm.cli:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
