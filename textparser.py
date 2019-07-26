#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:29:41 2019

@author: dan
"""
from textelements.formula import Formula
from textelements.picture import Picture
from textelements.paragraph import Paragraph

FORMULA = ['форм.', 'form.']
PICTURE = ['рис.', 'fig,']
HEADING = ['@']
HEADING1 = ['#']
HEADING2 = ['##']
HEADING3 = ['###']

def get_par_type(_in_par):
    try:
        first_word = _in_par[0].split()[0].lower()
        if first_word in FORMULA:
            return Formula
        elif first_word in PICTURE:
            return Picture
        else:
            return Paragraph
    except IndexError:
        return Paragraph

def get_paragraphs(_in = 'a\ns\n\nd\nf\n'):
    _in = _in.strip('\n') + '\n'
    line = []
    for l in [ v for v in _in.split('\n') ]:
        if not l:
            yield line
            line = []
        else:
            line += [l.rstrip()]


def parse(_in):
    text = []
    for par in get_paragraphs(_in):
        ClassOfTheElement = get_par_type(par)
        text += [ClassOfTheElement(par)]
    return text


if __name__ == '__main__':
    print(list(get_paragraphs()))
    print(parse('a\ns\n\nd\nf\n'))