#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_global_attrs

Compliance Test Suite: Check core global attributes in UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18GlobalAttrsCheck(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-global-attrs'



    def setup(self, ds):
        pass

    
    def check_gatc_001(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'CF-1\\.5', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_002(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_003(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'UKCP18', 'attribute': 'project'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_004(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'contact'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_005(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'references'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_006(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'v\\d{8}', 'attribute': 'version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_007(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'title'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_008(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'creation_date'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_gatc_009(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'institution_id', 'vocab_lookup': 'label'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_gatc_010(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'Met Office Hadley Centre \\(MOHC\\), FitzRoy Road, Exeter, Devon, EX1 3PB, UK\\.', 'attribute': 'institution'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_gatc_011(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'domain', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    