#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:46:04 2019

@author: dan
"""
import re

from textelements.paragraph import Paragraph
from PIL import Image

PICTURE_N = 1

class PictureParseError(Exception):
    pass

class Picture(Paragraph):
    
    def __find_image(self, name, root):
        _vars = []
        for suff in ['jpeg','png','jpg']:
            imname = '%s/img/%s.%s' % (root, name, suff)
            _vars += [imname]
            try:
                img = Image.open(imname)
                break
            except FileNotFoundError:
                pass
        try:
            return img
        except NameError:
            raise PictureParseError('Image not found %s' % str(_vars))
            
    def __get_img_params(self, img):
        
        return _name, _w, _h, _quote, _format 
            
    def __init__(self, *args, **kwargs):
        global PICTURE_N
        try:
            par = kwargs['par']
            self.documentroot = kwargs['root']
            self.name = re.findall(r'\w+\.?\s+?(.*)', par[0])[0]
            _name, _w, _h, _quote, _format = self.__get_img_params(
                self.__find_image(self.name, self.documentroot)
            )
            self.no = PICTURE_N
            self.draw_name
            self.svg_width = "16cm"
            self.svg_height = "%scm" % round(h * 16 / w, 2)
            PICTURE_N += 1
        except (IndexError, KeyError, ValueError):
            raise PictureParseError(str(kwargs))
    
    def __repr__(self):
        return '<p>Рис. %s --- %s, %s</p>' % (self.no, self.name, self.content)
        
#Рис. Пример рисунка png


if __name__ == '__main__':
    p1 = Picture(['Рис. Пример рисунка png'], '')
    print(p1)
    p2 = Picture(['Рис. Пример рисунка jpg'])
    print(p2)
    p3 = Picture(['Рис. Пример рисунка pngjpg'])
    print(p3)
    