#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:46:04 2019

@author: dan
"""
import re

from textelements.paragraph import Paragraph

FORMULA_N = 1

class FormulaParseError(Exception):
    pass

class Formula(Paragraph):
    def __init__(self, *args, **kwargs):
        global FORMULA_N
        try:
            par = kwargs['par']
            self.name, self.content = re.findall(r'\w+?\.\s+(.*?)\s(.*)', par[0])[0]
            self.no = FORMULA_N
            FORMULA_N += 1
        except (IndexError, KeyError, ValueError):
            raise FormulaParseError(str(kwargs))
    
    def __repr__(self):
        return '<p>%s<tab/>%s</p>' % (self.content, self.no)
        
#Form. Ф1 y = f(x) = 3 x^3 + 2 x^2 + b

if __name__ == '__main__':
    f1 = Formula(['Form. Ф1 y = f(x) = 3 x^3 + 2 x^2 + b'])
    print(f1)
    f2 = Formula(['Form. y'])
    print(f2)
    