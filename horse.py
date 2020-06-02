#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
import pygame
class Horse:
    def __init__(self,n,s,img_file,y):
        self.name=n
        self.speed=s
        self.__image=pygame.image.load(img_file)
        self._y=y
        self._x=0
    def run(self):
        self._x+=round(self.speed*random.random())
    def get_image(self):
        return self.__image
    def get_location(self):
        return (self._x,self._y)