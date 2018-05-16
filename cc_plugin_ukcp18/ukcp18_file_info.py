#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_file_info

Compliance Test Suite: Check UKCP18 file info
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, GenericFile

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.checks


class UKCP18FileInfoCheck(object):
    register_checker = True
    name = 'ukcp18-file-info'
    _cc_spec = 'ukcp18-file-info'
    _cc_spec_version = '0.2'
    supported_ds = [GenericFile, Dataset]


    def setup(self, fpath):
        pass

    
    def check_fsic_001(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="LOW",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fsic_002(self, ds):
        return checklib.checks.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fsic_003(self, ds):
        return checklib.checks.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
