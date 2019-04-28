#!/bin/env python3

import os
os.system('mv .git/ .git_temp/')             # No git repo, no cry - commenting this line in/out solves/reintroduces the problem
os.system('rm -rf dist/ Package.egg-info/')  # Make 'really clean'


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

os.system('mv .git_temp/ .git/')  # Reinstate git repo

print("\nPython and Fortran source files included in tarball:")
os.system('tar tfz dist/Package-0.0.1.tar.gz |grep -E "\.py|\.f90"')
