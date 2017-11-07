#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup script for building, distributing and installing."""

from setuptools import setup, find_packages


with open("README.md") as readme, open("CHANGELOG.md") as changelog:
    LONG_DESCRIPTION = readme.read() + 2 * '\n' + changelog.read()

setup(
    name='meneadata',
    description="Meneame Data",
    long_description=LONG_DESCRIPTION,
    author="Efraín Lima Miranda",
    author_email='efrain70@gmail.com',
    url='https://github.com/efrain70/meneadata',
    packages=find_packages(),
    include_package_data=True,
    use_scm_version={'write_to': 'meneadata/version.py'},
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'bs4',
        'requests',
        'six',
    ],
    entry_points={
        "console_scripts": ['meneadata = meneadata.meneadata:main']
    },
    license="GNU Affero General Public License",
    zip_safe=False,
    keywords=['meneadata'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
