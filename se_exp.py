# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 17:44:42 2018

@author: sudhanshu shukla
"""

import os
import re

os.chdir("C:/Users/sudhanshu shukla/Desktop/TE_DivC_21/TE_DivC_21_MCC/01_Experiments")


def sorted_nicely(l):
    """ Sorts the given iterable in the way that is expected.

    Required arguments:
    l -- The iterable to be sorted.

    """
    def convert(text): return int(text) if text.isdigit() else text

    def alphanum_key(key): return [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


print(os.getcwd())
lidr = os.listdir()
lidr = sorted_nicely(lidr)
i = 2
for f in lidr:
    print(f)
    file_name, file_ext = os.path.splitext(f)
#    new_name = "TE_C_21_Expt_{:02}_MCC{}".format(i, file_ext)
#    os.rename(f, new_name)
#    i += 1