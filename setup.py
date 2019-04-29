#!/bin/env python3

import os
#os.system('rm -rf *.egg-info/')        # Make 'really clean'


# Prevent the setuptools_scm plugin from adding (only) the contents of the git repo to the tarball:
from setuptools_scm import integration
integration.find_files = lambda p: []


from setuptools import setup  #, find_packages
setup(
    name='Package',
    description='A Python package',
    author='AF',
    author_email='AF@mail.org',
    url='https://hitgub.org/AF/package',
    
    packages=['package'],  # Only include Python code in the package/ subdir - works, when no git repo present
    #py_modules=['package/module1','package/module2'],  # Error prone - works, when no git repo present
    #package_dir={'package':'*.py'},
    #use_scm_version=False,
    
    version='0.0.1',
    license='GPL',
    keywords=['package']
)

print("\nPython and Fortran source files included in tarball:")
os.system('tar tfz dist/Package-0.0.1.tar.gz |grep -E "\.py|\.f90"')
