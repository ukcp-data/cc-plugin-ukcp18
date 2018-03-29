#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_river_basin

Compliance Test Suite: Check content of UKCP18 River Basin files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18RiverBasinCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-river-basin'
    _cc_spec = 'ukcp18-river-basin'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_river_001(self, ds):
        return checklib.checks.NCArrayMatchesVocabTermsCheck(kwargs={'var_id': 'geo_region', 'pyessv_namespace': 'river_basin'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    