import os
import sys

from distutils.core import setup
from setuptools.command.test import test


class PyTest(test):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='hosts',
    version='0.1',
    packages=['hosts'],
    package_dir={'hosts': 'hosts'},
    url='https://github.com/manojklm/hosts',
    license='The MIT License (MIT)',
    author='manojklm',
    author_email='',
    description='Python wrapper to manage hosts file',
    keywords='hosts hostsfile hostfile pyhosts',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
