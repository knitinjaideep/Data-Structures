#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 08:29:29 2019

@author: nitinkotcherlakota
"""

import os
def find_files(suffix, path=[]):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """


    if suffix == '':
        return []
    if len(os.listdir(path)) == 0:  
        return []
    paths = os.listdir(path)
    files = [file for file in paths if '.' + suffix in file]
    folders = [file for file in paths if '.' not in file]

    for folder in folders:
        files.extend(find_files(suffix=suffix, path=path + '/' + folder))

    return files


path1 = os.getcwd() + '/testdir/subdir1'
path2 = os.getcwd() + '/testdir/subdir3'
path3 = os.getcwd() + '/testdir'
path4 = os.getcwd() + '/testdir/subdir3/subsubdir1'
print(find_files(suffix='c', path=path1))
print(find_files(suffix='h', path=path2))
print(find_files(suffix='c', path=path3))
print(find_files(suffix='c', path=path4))

# Edge Case
print(find_files(suffix='z', path=path1))
print(find_files(suffix='', path=path2))