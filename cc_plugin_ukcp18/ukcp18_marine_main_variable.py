#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_marine_main_variable

Compliance Test Suite: Check structure of UKCP18 main marine variables
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18MarineMainVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-marine-main-variable'
    _cc_spec = 'ukcp18-marine-main-variable'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_mmvc_001(self, ds):
        return checklib.checks.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_mmvc_002(self, ds):
        return checklib.checks.MainVariableAttributeCheck(kwargs={'attr_name': '_FillValue', 'attr_value': '1e20'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_mmvc_003(self, ds):
        return checklib.checks.MainVariableTypeCheck(kwargs={'dtype': 'float32'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_mmvc_004(self, ds):
        return checklib.checks.NCMainVariableMetadataCheck(kwargs={'pyessv_namespace': 'variable', 'ignores': ['cmip6_cmor_tables_row_id', 'cmip6_name', 'cmip6_standard_name', 'notes', 'strand', 'time_averaging', 'time_step', 'um_stash']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    