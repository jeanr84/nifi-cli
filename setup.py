import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='NiFi CLI',
    version='0.1.0',
    author='Robin Jean, Adrien Lacroix',
    packages=['nifi'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
    ],
    entry_points={
        'console_scripts': [
            'nifi-cli = nifi.main:main',
        ],
    }
)