#!/usr/bin/env python
"""
cc_plugin_eustace.eustace_file_info

Compliance Test Suite: Check file names and external information about EUSTACE files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, GenericFile

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "eustace-team"

# Import checklib
import checklib.register.file_checks_register as check_package

class EUSTACEFileInfoCheck(object):
    register_checker = True
    name = 'eustace-file-info'
    _cc_spec = 'eustace-file-info'
    _cc_spec_version = '0.2'
    supported_ds = [GenericFile, Dataset]
    _cc_display_headers = {
        3: 'Required',
        2: 'Recommended',
        1: 'Suggested'
    }

    def setup(self, fpath):
        pass

    
    def check_fi01(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="LOW",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi02(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi03(self, ds):
        return check_package.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
