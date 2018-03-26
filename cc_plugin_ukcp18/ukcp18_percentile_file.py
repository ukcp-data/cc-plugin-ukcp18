#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_percentile_file

Compliance Test Suite: Check content of UKCP18 percentile files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18PercentileFileCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-percentile-file'



    def setup(self, ds):
        pass

    
    def check_perc_001(self, ds):
        return checklib.checks.NCCoordVarHasValuesInVocabCheck(kwargs={'var_id': 'percentile'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    