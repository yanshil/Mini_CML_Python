import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


name = 'minicmlpy'
version = '0.1.1'
dependencies = []

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'hello = minicmlpy.hello_world:main',
        ],
    },

)