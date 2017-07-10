#!/usr/bin/env python
"""
cc_plugin_eustace.eustace_file_structure

Compliance Test Suite: Check structure of EUSTACE files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "eustace-team"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class EUSTACEFileStructureCheck(BaseNCCheck):
    register_checker = True
    name = 'eustace-file-structure'

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        pass

    
    def check_fs03(self, ds):
        return check_package.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    