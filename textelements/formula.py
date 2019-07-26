#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:46:04 2019

@author: dan
"""
import re

from textelements.paragraph import Paragraph

class FormulaParseError(Exception):
    pass

class Formula(Paragraph):
    def __init__(self, *args, **kwargs):
        try:
            par = args[0]
            self.name, self.content = re.findall(r'\w+?\.\s+(.*?)\s(.*)', par[0])[0]
        except (IndexError, ValueError):
            raise FormulaParseError(par)
    
    def __repr__(self):
        return '<p>%s</p>' % self.content
        
#Form. Ф1 y = f(x) = 3 x^3 + 2 x^2 + b

if __name__ == '__main__':
    f1 = Formula(['Form. Ф1 y = f(x) = 3 x^3 + 2 x^2 + b'])
    print(f1)
    f2 = Formula(['Form. y'])
    print(f2)
    