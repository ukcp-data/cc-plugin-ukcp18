#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_ls102

Compliance Test Suite: Check LS1.02 UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18LS102Check(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-ls102'
    _cc_spec = 'ukcp18-ls102'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_ls102_001(self, ds):
        return checklib.checks.NetCDFFormatCheck(kwargs={'format': 'NETCDF4_CLASSIC'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_002(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="LOW",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_003(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_004(self, ds):
        return checklib.checks.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_005(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'CF-1\\.5', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_006(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_007(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'UKCP18', 'attribute': 'project'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_008(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'contact'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_009(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'references'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_010(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'v\\d{8}', 'attribute': 'version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_011(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'title'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_012(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'creation_date'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_013(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'institution_id', 'vocab_lookup': 'label'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_014(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'Met Office Hadley Centre \\(MOHC\\), FitzRoy Road, Exeter, Devon, EX1 3PB, UK\\.', 'attribute': 'institution'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_015(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'domain', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_016(self, ds):
        return checklib.checks.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_017(self, ds):
        return checklib.checks.MainVariableAttributeCheck(kwargs={'attr_name': '_FillValue', 'attr_value': '1e20'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_018(self, ds):
        return checklib.checks.MainVariableTypeCheck(kwargs={'dtype': 'float32'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_019(self, ds):
        return checklib.checks.NCMainVariableMetadataCheck(kwargs={'pyessv_namespace': 'variable', 'ignores': ['cmip6_cmor_tables_row_id', 'cmip6_name', 'cmip6_standard_name', 'notes', 'strand', 'time_averaging', 'time_step', 'um_stash']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_020(self, ds):
        return checklib.checks.MainVariableAttributeCheck(kwargs={'attr_name': 'cell_methods', 'attr_value': 'time: mean'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_021(self, ds):
        return checklib.checks.ValidGlobalAttrsMatchFileNameCheck(kwargs={'delimiter': '_', 'order': 'variable~scenario~collection~domain~resolution~coordinate~frequency~regex:^(?:\\d{2}){2,6}(?:$|-(?:\\d{2}){2,6}$)', 'extension': '.nc', 'ignore_attr_checks': ['variable']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_022(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'land-prob', 'attribute': 'collection'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_ls102_023(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'frequency', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ls102_024(self, ds):
        return checklib.checks.NCArrayMatchesVocabTermsCheck(kwargs={'var_id': 'geo_region', 'pyessv_namespace': 'admin_region'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
