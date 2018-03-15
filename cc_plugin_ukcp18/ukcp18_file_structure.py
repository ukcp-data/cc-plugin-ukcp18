#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_file_structure

Compliance Test Suite: Check structure of UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class UKCP18FileStructureCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-file-structure'


    def setup(self, ds):
        pass

    
    def check_fs01(self, ds):
        return check_package.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_fs02(self, ds):
        return check_package.NetCDFFormatCheck(kwargs={'format': 'NETCDF4_CLASSIC'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    