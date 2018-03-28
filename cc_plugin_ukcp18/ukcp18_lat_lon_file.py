#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_lat_lon_file

Compliance Test Suite: Check content of UKCP18 Lat/Lon files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18LatLonFileCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-lat-lon-file'
    _cc_spec = 'ukcp18-lat-lon-file'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_latlonf_001(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_latlonf_002(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_latlonf_003(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    