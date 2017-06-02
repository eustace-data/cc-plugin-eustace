#!/usr/bin/env python
"""
compliance_checker.primavera

Compliance Test Suite for the PRIMAVERA project
"""

import os
from compliance_checker.base import BaseCheck, BaseNCCheck, Result, TestCtx

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "eustace-team"

# Import library to interact with Controlled Vocabularies
from compliance_checker.cvs.ess_vocabs import ESSVocabs


class EUSTACECoreCheck(BaseNCCheck):
    register_checker = True
    name = 'eustace-core'

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        self._load_controlled_vocabularies()


    def _load_controlled_vocabularies(self):
        """
        Loads controlled vocabularies once and caches them.
        """
        self.vocabs = ESSVocabs('eustace-team', 'eustace')


    def check_global_attributes(self, ds):
        """
        Verifies the base metadata in the global attributes.
        """
        attrs_to_check = [('source', 'label'),
                          ('frequency', 'name'),
                          ('institution_id', 'label')
                         ]

        level = BaseCheck.MEDIUM
        out_of = 0
        score = 0
        messages = []

        for attr, property in attrs_to_check:
            # NOTE: the `property` refers to which part of the CV we want to check against.
            value = self.vocabs.check_global_attribute(ds, attr, property=property)
        
            score += value
            out_of += 2

            if value == 0:
                messages.append('{} global attribute is missing'.format(attr))
            elif value == 1:
                messages.append('{} global attribute found but invalid value'.format(attr))  

        return self.make_result(level, score, out_of, 'Required Global Attributes', messages)



