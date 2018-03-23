#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_land_main_variable

Compliance Test Suite: Check structure of UKCP18 main variables
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class UKCP18LandMainVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-land-main-variable'


    def setup(self, ds):
        pass

    
    def check_lmvc_001(self, ds):
        return check_package.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_lmvc_002(self, ds):
        return check_package.MainVariableAttributeCheck(kwargs={'attr_name': 'cell_methods', 'attr_value': 'time: mean'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_lmvc_003(self, ds):
        return check_package.MainVariableAttributeCheck(kwargs={'attr_name': '_FillValue', 'attr_value': '1e20'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    