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
            'ukcp18-file-info = cc_plugin_ukcp18.ukcp18_file_info:UKCP18FileInfoCheck',
            'ukcp18-file-structure = cc_plugin_ukcp18.ukcp18_file_structure:UKCP18FileStructureCheck',
            'ukcp18-ls101 = cc_plugin_ukcp18.ukcp18_ls101:UKCP18LS101Check',
            'ukcp18-ls102 = cc_plugin_ukcp18.ukcp18_ls102:UKCP18LS102Check',
            'ukcp18-ls103 = cc_plugin_ukcp18.ukcp18_ls103:UKCP18LS103Check',
            'ukcp18-ls104 = cc_plugin_ukcp18.ukcp18_ls104:UKCP18LS104Check',
            'ukcp18-ls201 = cc_plugin_ukcp18.ukcp18_ls201:UKCP18LS201Check',
            'ukcp18-ls202 = cc_plugin_ukcp18.ukcp18_ls202:UKCP18LS202Check',
            'ukcp18-ls203 = cc_plugin_ukcp18.ukcp18_ls203:UKCP18LS203Check',
            'ukcp18-ls204 = cc_plugin_ukcp18.ukcp18_ls204:UKCP18LS204Check',
            'ukcp18-ms401 = cc_plugin_ukcp18.ukcp18_ms401:UKCP18MS401Check',
        ]
    }
)

