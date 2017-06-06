from __future__ import with_statement
import sys

from setuptools import setup, find_packages

from cc_plugin_ukcp18 import __version__

def readme():
    with open('README.md') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(name                 = "cc-plugin-ukcp18",
    version              = __version__,
    description          = "Compliance Checker UKCP18 plugin",
    long_description     = readme(),
    license              = 'BSD License',
    author               = "Ag Stephens",
    author_email         = "ag.stephens@stfc.ac.uk",
    url                  = "https://github.com/ukcp-data/cc-plugin-ukcp18",
    packages             = find_packages(),
    install_requires     = reqs,
    classifiers          = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
    entry_points         = {
        'compliance_checker.suites': [
            'ukcp18-core = cc_plugin_ukcp18.ukcp18_core:UKCP18CoreCheck',
            'ukcp18-station = cc_plugin_ukcp18.ukcp18_station:UKCP18StationCheck'
        ]
    }
)

