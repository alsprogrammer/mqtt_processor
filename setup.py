#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pydantic==1.9.0",
    "paho-mqtt==1.6.1",
    "git+https://github.com/alsprogrammer/custom_logger.git",
]

test_requirements = [ ]

setup(
    author="Aleksandr Saiapin",
    author_email='alstutor@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An MQTT wrapper",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mqtt_processor',
    name='mqtt_processor',
    packages=find_packages(include=['mqtt_processor', 'mqtt_processor.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/alstutor/mqtt_processor',
    version='0.1.0',
    zip_safe=False,
)
