from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import uniconfig

install_requires = [
    'toml',
]

tests_require = [
    'coverage',
    'pytest',
    'pytest-cov',
]

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Operating System :: POSIX',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


def read(filename):
    with open(filename, 'r') as fh:
        return fh.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(name='uniconfig',
      version=uniconfig.__version__,
      description="Python library for unifying configuration handling",
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      classifiers=classifiers,
      platforms=["POSIX"],
      author="Kai Blin",
      author_email="kblin@biosustain.dtu.dk",
      url="https://github.com/kblin/uniconfig",
      license="Apache Software License",
      packages=find_packages(exclude=["tests"]),
      install_requires=install_requires,
      tests_require=tests_require,
      cmdclass={'test': PyTest},
      include_package_data=True,
      extras_require={
        'testing': tests_require,
        'shipping': ['twine'],
      },
)
