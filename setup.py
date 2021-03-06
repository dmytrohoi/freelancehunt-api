#!/usr/bin/env python
"""The setup and build script for the freelancehunt-api library."""
from os import path

from setuptools import setup, find_packages
from distutils.util import convert_path


def get_version(package):
    main_ns = {}
    ver_path = convert_path(f'{package}/version.py')
    with open(ver_path) as ver_file:
        exec(ver_file.read(), main_ns)

    return main_ns['__version__']


packages = find_packages(exclude=['tests*'])

readme_path = path.join(path.abspath(path.dirname(__file__)), 'README.rst')
with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='freelancehunt-api',
    version=get_version('freelancehunt'),
    author='Dmytro Hoi',
    author_email='code@dmytrohoi.com',
    license='MIT License',
    url='https://github.com/dmytrohoi/freelancehunt-api',
    keywords='python freelance api wrapper',
    description="FreelanceHunt API Python library",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=packages,
    install_requires=[
        'requests==2.23.0',
        'simplejson==3.17.0'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
