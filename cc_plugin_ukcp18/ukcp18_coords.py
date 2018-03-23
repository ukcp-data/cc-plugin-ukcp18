#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_coords

Compliance Test Suite: Check lat, lon coordinate information in UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class UKCP18CoordinatesLatLonCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-coords'


    def setup(self, ds):
        pass

    
    def check_cllc_001(self, ds):
        return check_package.VariableExistsInFileCheck(kwargs={'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cllc_002(self, ds):
        return check_package.VariableRangeCheck(kwargs={'var_id': 'longitude', 'minimum': -180.0, 'maximum': '180.'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cllc_003(self, ds):
        return check_package.VariableExistsInFileCheck(kwargs={'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cllc_004(self, ds):
        return check_package.VariableRangeCheck(kwargs={'var_id': 'latitude', 'minimum': -90.0, 'maximum': '90.'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    