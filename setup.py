#!/usr/bin/env python
from setuptools import setup, find_packages
import sys
import os

version = '0.0.3'

with open("README.md", "r") as f:
    long_description = f.read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='pysendyit',
    version=version,
    author='Rodney Osodo',
    author_email='blackd0t@protonmail.com',
    description='Un-Official Sendyit Python wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/0x6f736f646f/sendit-python',
    # download_url='https://codeload.github.com/AfricasTalkingLtd/africastalking-python/tar.gz/' + version,
    # download_url='http://pypi.python.org/pypi/pysendy/',
    zip_safe=True,
    py_modules=[],
    keywords='pysendyit sendy wrapper api',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)