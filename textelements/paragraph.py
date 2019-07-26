#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:46:04 2019

@author: dan
"""

class Paragraph:
    def __init__(self, *args, **kwargs):
        self.strings = args[0]
    
    def __repr__(self):
        return "<p>%s</p>\n" % "\n".join(self.strings)