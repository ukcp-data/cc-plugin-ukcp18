#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_ms401

Compliance Test Suite: Check MS4.01 UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18MS401Check(BaseNCCheck):
    register_checker = True
    name = 'ukcp18-ms401'
    _cc_spec = 'ukcp18-ms401'
    _cc_spec_version = '0.2'


    def setup(self, ds):
        pass

    
    def check_ms401_001(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="LOW",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_002(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_003(self, ds):
        return checklib.checks.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_004(self, ds):
        return checklib.checks.NetCDFFormatCheck(kwargs={'format': 'NETCDF4_CLASSIC'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_005(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'CF-1\\.5', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_006(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_007(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'UKCP18', 'attribute': 'project'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_008(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'contact'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_009(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'references'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_010(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'v\\d{8}', 'attribute': 'version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_011(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'title'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_012(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'creation_date'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_013(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'institution_id', 'vocab_lookup': 'label'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_014(self, ds):
        return checklib.checks.GlobalAttrRegexCheck(kwargs={'regex': 'Met Office Hadley Centre \\(MOHC\\), FitzRoy Road, Exeter, Devon, EX1 3PB, UK\\.', 'attribute': 'institution'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_015(self, ds):
        return checklib.checks.GlobalAttrVocabCheck(kwargs={'attribute': 'domain', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_016(self, ds):
        return checklib.checks.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_017(self, ds):
        return checklib.checks.MainVariableAttributeCheck(kwargs={'attr_name': '_FillValue', 'attr_value': '1e20'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_018(self, ds):
        return checklib.checks.MainVariableTypeCheck(kwargs={'dtype': 'float32'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_019(self, ds):
        return checklib.checks.NCMainVariableMetadataCheck(kwargs={'pyessv_namespace': 'variable', 'ignores': ['cmip6_cmor_tables_row_id', 'cmip6_name', 'cmip6_standard_name', 'notes', 'strand', 'time_averaging', 'time_step', 'um_stash']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_020(self, ds):
        return checklib.checks.VariableExistsInFileCheck(kwargs={'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_021(self, ds):
        return checklib.checks.VariableRangeCheck(kwargs={'var_id': 'longitude', 'minimum': -180.0, 'maximum': '180.'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_022(self, ds):
        return checklib.checks.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_023(self, ds):
        return checklib.checks.VariableExistsInFileCheck(kwargs={'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_024(self, ds):
        return checklib.checks.VariableRangeCheck(kwargs={'var_id': 'latitude', 'minimum': -90.0, 'maximum': '90.'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_025(self, ds):
        return checklib.checks.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_026(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_027(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_028(self, ds):
        return checklib.checks.NCCoordVarHasBoundsCheck(kwargs={'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_ms401_029(self, ds):
        return checklib.checks.NetCDFDimensionCheck(kwargs={'dim_id': 'time', 'pyessv_namespace': 'coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_030(self, ds):
        return checklib.checks.NetCDFDimensionCheck(kwargs={'dim_id': 'latitude', 'pyessv_namespace': 'coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_031(self, ds):
        return checklib.checks.NetCDFDimensionCheck(kwargs={'dim_id': 'longitude', 'pyessv_namespace': 'coordinate'},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
    def check_ms401_032(self, ds):
        return checklib.checks.ValidGlobalAttrsMatchFileNameCheck(kwargs={'delimiter': '_', 'order': 'variable~regex:marine-sim~regex:(timeseries|CNRM-CM5|EC-EARTH|HadGEM2-ES|IPSL-CM5A-MR|MPI-ESM-LR)~regex:hist~regex:^\\d{4}060100-\\d{4}053023$', 'extension': '.nc', 'ignore_attr_checks': ['variable']},
                                                    level="HIGH",
                                                    vocabulary_ref="ukcp:ukcp18")(ds)
    
