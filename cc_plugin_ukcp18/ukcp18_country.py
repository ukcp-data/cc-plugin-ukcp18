#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_country

Compliance Test Suite: Check content of UKCP18 Country files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18CountryCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-country'
    _cc_spec = 'ukcp18-country'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_region_001(self, ds):
        return checklib.checks.NCArrayMatchesVocabTermsCheck(kwargs={'var_id': 'geo_region', 'pyessv_namespace': 'country'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    