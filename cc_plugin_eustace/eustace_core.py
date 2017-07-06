#!/usr/bin/env python
"""
cc_plugin_eustace.eustace_core

Compliance Test Suite: Check core global attributes in EUSTACE files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "eustace-team"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class EUSTACECoreCheck(BaseNCCheck):
    register_checker = True
    name = 'eustace-core'

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        pass

    
    def check_cr01(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'CF-\\d+\\.\\d+', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr02(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '\\w+', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr03(self, ds):
        return check_package.OneMainVariablePerFileCheck(kwargs={},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr04(self, ds):
        return check_package.ValidGlobalAttrsMatchFileNameCheck(kwargs={'delimiter': '_', 'order': 'institution_id,realm,frequency', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="eustace-team:eustace")(ds)
    