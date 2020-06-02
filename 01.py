#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
from horse import Horse
pygame.init()
screen=pygame.display.set_mode([800,600])
img_bg=pygame.image.load("d:/test1/bk.jpg")
h1=[Horse("小兔",5,"d:/test1/u33.jpg",100),
    Horse("laotu",5,"d:/test1/u33.jpg",200),
    Horse("lao",5,"d:/test1/u33.jpg",300)]
while True:
    screen.blit(img_bg, (0, 0))
    for h in h1:
        screen.blit(h.get_image(), h.get_location())
        h.run()
    pygame.display.update()
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()










