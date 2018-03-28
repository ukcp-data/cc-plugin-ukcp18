#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_global_attrs_ls1

Compliance Test Suite: Check core LS1 global attributes in UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18GlobalAttrsLS1Check(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-global-attrs-ls1'
    _cc_spec = 'ukcp18-global-attrs-ls1'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_gatls1_001(self, ds):
        return checklib.checks.ValidGlobalAttrsMatchFileNameCheck(kwargs={'delimiter': '_', 'order': 'variable~scenario~collection~domain~resolution~coordinate~frequency~regex:', 'extension': '.nc', 'ignore_attr_checks': ['variable']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_gatls1_002(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'land-prob', 'attribute': 'collection'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_gatls1_003(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'frequency', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    