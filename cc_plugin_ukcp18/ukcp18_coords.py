#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_coords

Compliance Test Suite: Check coordinate information in UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class UKCP18CoordinatesCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-coords'


    def setup(self, ds):
        pass

    
    def check_cc01(self, ds):
        return check_package.VariableExistsInFileCheck(kwargs={'var_id': 'lon'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cc02(self, ds):
        return check_package.VariableRangeCheck(kwargs={'var_id': 'lon', 'minimum': -180.0, 'maximum': '180.'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
