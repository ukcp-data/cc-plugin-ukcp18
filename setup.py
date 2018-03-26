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
            'ukcp18-coordinates-lat-lon = cc_plugin_ukcp18.ukcp18_coordinates_lat_lon:UKCP18CoordinatesLatLonCheck',
            'ukcp18-file-info = cc_plugin_ukcp18.ukcp18_file_info:UKCP18FileInfoCheck',
            'ukcp18-file-structure = cc_plugin_ukcp18.ukcp18_file_structure:UKCP18FileStructureCheck',
            'ukcp18-global-attrs = cc_plugin_ukcp18.ukcp18_global_attrs:UKCP18GlobalAttrsCheck',
            'ukcp18-global-attrs-ls1 = cc_plugin_ukcp18.ukcp18_global_attrs_ls1:UKCP18GlobalAttrsLS1Check',
            'ukcp18-land-main-variable = cc_plugin_ukcp18.ukcp18_land_main_variable:UKCP18LandMainVariableCheck',
            'ukcp18-lat-lon-file = cc_plugin_ukcp18.ukcp18_lat_lon_file:UKCP18LatLonFileCheck',
            'ukcp18-osgb-file = cc_plugin_ukcp18.ukcp18_osgb_file:UKCP18OSGBFileCheck',
            'ukcp18-percentile-file = cc_plugin_ukcp18.ukcp18_percentile_file:UKCP18PercentileFileCheck',
            'ukcp18-sample-file = cc_plugin_ukcp18.ukcp18_sample_file:UKCP18SampleFileCheck',
        ]
    }
)

