## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame

import helpers,screen
#,player,slot_1,slot_2,slot_3
class Darkness:
    def __init__(self,darkness):
        self.noflashlight=helpers.load_image('Noflashlight1.png',-1)
        self.noflashlightrect=self.noflashlight.get_rect(topleft=((-1),(-1)))
        self.flashlight=helpers.load_image('flashlight.png',-1)
        self.flashlightrect=self.flashlight.get_rect(topleft=((-1),(-1)))
        self.darkness=darkness

    def update(self,flashlight,flashlight_on):
        
        if self.darkness==1:
            if flashlight_on==1:
                if flashlight.energy<1:
                    screen.screen.blit(self.noflashlight,self.noflashlightrect)
                else:
                    screen.screen.blit(self.flashlight,self.flashlightrect)
            else:
                screen.screen.blit(self.noflashlight,self.noflashlightrect)
        else:
            pass
            
