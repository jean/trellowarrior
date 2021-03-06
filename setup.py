#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'tasklib',
    'py-trello',
]

setup_requirements = [
    'pytest-runner',
    # TODO(jean): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='trellowarrior',
    version='0.1.0',
    description="Syncs Trello boards and Taskwarrior projects.",
    long_description=readme + '\n\n' + history,
    author="Óscar García Amor",
    author_email='ogarcia@...',
    url='https://github.com/ogarcia/trellowarrior',
    packages=find_packages(include=['trellowarrior']),
    entry_points={
        'console_scripts': [
            'trellowarrior=trellowarrior.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='trellowarrior',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
