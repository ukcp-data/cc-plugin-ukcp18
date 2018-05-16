#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_file_structure

Compliance Test Suite: Check UKCP18 file structure
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18FileStructureCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-file-structure'
    _cc_spec = 'ukcp18-file-structure'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_fssc_001(self, ds):
        return checklib.checks.NetCDFFormatCheck(kwargs={'format': 'NETCDF4_CLASSIC'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
