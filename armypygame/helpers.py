## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame


## This is the load screen function
## import the helpers by calling
## import helpers
## then with helpers.load_image you can load images into the game
## example helpers.load_image('wall.bmp',0)
## the zero is used for walls and floors -1 is used for creatures and player
## pictures
## -1 removes the color that is in the top right corler from the entire image
def load_image(name,colorkey):
    fullname = os.path.join('data','pictures',name)
    i=pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = i.get_at((0,0))
        i.set_colorkey(colorkey, RLEACCEL)
    return i.convert()

def load_sound(name):
    """loads a sound file (.wav) in memory"""
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data/sounds',name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound
