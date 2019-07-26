#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:45:19 2019

@author: dan
"""

from textparser import parse
import os

if __name__ == '__main__':
    import sys
    try:
        fname = sys.argv[1]
        documentroot = os.path.dirname(fname)
        data = open(fname).read()
        print(parse(data, documentroot))
    except IndexError:
        print('usage: %s [input file]' % sys.argv[0])
    except FileNotFoundError:
        print('file %s was not found' % fname)
        