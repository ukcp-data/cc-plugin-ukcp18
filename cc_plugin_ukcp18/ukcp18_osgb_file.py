#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_osgb_file

Compliance Test Suite: Check content of UKCP18 OSGB files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18OSGBFileCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-osgb-file'
    _cc_spec = 'ukcp18-osgb-file'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_osgbf_001(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'projection_x_coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_osgbf_002(self, ds):
        return checklib.checks.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'projection_x_coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_osgbf_003(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'projection_y_coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_osgbf_004(self, ds):
        return checklib.checks.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'projection_y_coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_osgbf_005(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_osgbf_006(self, ds):
        return checklib.checks.NCVariableMetadataCheck(kwargs={'var_id': 'transverse_mercator', 'pyessv_namespace': 'variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
