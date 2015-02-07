import os,sys,random,pygame
from pygame.locals import *
import time,math
import cPickle as pickle

pygame.init()
pygame.display.get_init()
pygame.display.init()
pygame.display.get_driver()

pygame.mixer.set_num_channels(1000)
options=file('data/options','rb')

fullscreen=pickle.load(options)
fullscreen=int(fullscreen)
size=(1024,768)
if fullscreen==0:
    screen=pygame.display.set_mode(size)
if fullscreen==1:
    screen=pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.flip()
