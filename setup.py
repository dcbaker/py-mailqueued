from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='msmtpqd',
    version='0.1.3',
    description='A queueing daemon for emails',
    long_description=long_description,
    url='https://github.com/dcbaker/msmtpqd',
    author='Dylan Baker',
    author_email='dylan@pnwbakers.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Topic :: Communications :: Email :: Mail Transport Agents',
    ],
    install_requires=[
        'attr',
        'appdirs',
        'pydbus',
    ],
    keywords='email',
    scripts=[
        'scripts/msmtpqd',
        'scripts/msmtp-queue',
    ],
    data_files=[
        ('/usr/lib/systemd/user/', ['systemd/msmtpqd.service']),
    ],
)
