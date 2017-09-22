#!/usr/bin/env python
"""
cc_plugin_eustace.eustace_global_attrs

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


class EUSTACEGlobalAttrsCheck(BaseNCCheck):
    register_checker = True
    name = 'eustace-global-attrs'


    def setup(self, ds):
        pass

    
    def check_cr01(self, ds):
        return check_package.ValidGlobalAttrsMatchFileNameCheck(kwargs={'delimiter': '_', 'order': 'institution_id,realm,frequency', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="eustace-team:eustace")(ds)
    
    def check_cr02(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'CF-1\\.6', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr03(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr04(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'EUSTACE', 'attribute': 'project_id'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr05(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'contact'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr06(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'history'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_cr07(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'references'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    
    def check_cr08(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{1,}', 'attribute': 'product_version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr09(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'title'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr10(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{20,}', 'attribute': 'summary'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr11(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'creator_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr12(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.+@.+\\..+', 'attribute': 'creator_email'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_cr13(self, ds):
        return check_package.GlobalAttrVocabCheck(kwargs={'attribute': 'frequency', 'vocab_lookup': 'canonical_name'},
                                                    level="LOW",
                                                    vocabulary_ref="eustace-team:eustace")(ds)
    
    def check_cr14(self, ds):
        return check_package.GlobalAttrVocabCheck(kwargs={'attribute': 'institution_id', 'vocab_lookup': 'canonical_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="eustace-team:eustace")(ds)
    
    def check_cr15(self, ds):
        return check_package.GlobalAttrVocabCheck(kwargs={'attribute': 'institution', 'vocab_lookup': 'description'},
                                                    level="HIGH",
                                                    vocabulary_ref="eustace-team:eustace")(ds)
    
    def check_cr16(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'creation_date'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds)
    