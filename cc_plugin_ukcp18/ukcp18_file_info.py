#!/usr/bin/env python
"""
cc_plugin_ukcp18.ukcp18_file_info

Compliance Test Suite: Check file names and external information about UKCP18 files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, GenericFile

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ukcp"

# Import checklib
import checklib.register.file_checks_register as check_package

class UKCP18FileInfoCheck(object):
    register_checker = True
    name = 'ukcp18-file-info'
    supported_ds = [GenericFile, Dataset]


    def setup(self, fpath):
        pass

    
    def check_fi01(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi02(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi03(self, ds):
        return check_package.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
