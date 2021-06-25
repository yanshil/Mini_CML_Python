import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


name = 'pyserializer_kdrobian'
version = '0.1'
dependencies = []

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hello = src.hello_world:main',
        ],
    },

)