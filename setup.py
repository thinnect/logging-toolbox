from os import path
from codecs import open

from setuptools import setup, find_packages

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'logging_toolbox/version.py')) as f:
    exec(f.read())

setup(
    name='logging-toolbox',
    version=__version__,
    description='logging-toolbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thinnect/logging-toolbox',
    license='MIT',

    author='Kaarel Ratas',
    author_email='kaarel@thinnect.com',

    packages=find_packages(),
    include_package_data=True, # Use MANIFEST.in for data files
    install_requires=['six'],
    tests_require=['nose'],
)