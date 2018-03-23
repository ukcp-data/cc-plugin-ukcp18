#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_sample_file

Compliance Test Suite: Check content of UKCP18 sample files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.nc_coords_checks_register as check_package


class UKCP18SampleFileCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-sample-file'


    def setup(self, ds):
        pass

    
    def check_sample_001(self, ds):
        return check_package.NCCoordVarHasLengthInVocabCheck(kwargs={'var_id': 'sample'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    