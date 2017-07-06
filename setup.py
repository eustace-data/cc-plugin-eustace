from __future__ import with_statement
import sys

from setuptools import setup, find_packages

from cc_plugin_eustace import __version__

def readme():
    with open('README.md') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(name                 = "cc-plugin-eustace",
    version              = __version__,
    description          = "Compliance Checker EUSTACE plugin",
    long_description     = readme(),
    license              = 'BSD License',
    author               = "Ag Stephens",
    author_email         = "ag.stephens@stfc.ac.uk",
    url                  = "https://github.com/eustace-test/cc-plugin-eustace",
    packages             = find_packages(),
    install_requires     = reqs,
    classifiers          = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
    entry_points         = {
        'compliance_checker.suites': [
            'eustace-core = cc_plugin_eustace.eustace_core:EUSTACECoreCheck',
            'eustace-file-info = cc_plugin_eustace.eustace_file_info:EUSTACEFileInfoCheck'
        ]
    }
)

