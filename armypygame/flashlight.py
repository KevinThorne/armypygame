## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame

import helpers,screen
#,player,slot_1,slot_2,slot_3
class Flashlight:
    def __init__(self,x,y):
        self.image=helpers.load_image('flashlight_picture.png',-1)
        self.rect=self.image.get_rect(topleft=(x+9,y+10))

        self.energy=0
        self.recover_enery_rate=10

        self.show=1


    def pickup(self,player):
        if self.rect.colliderect(player):
            self.energy=100
            self.show=0
            self.image=helpers.load_image('flashlight_picture.png',-1)
            self.rect=self.image.get_rect(topleft=(10,40))
            

    def move(self,direction,speed):
        if self.show==1:
            if direction==1:
                self.rect=self.rect.move(0,speed)
            if direction==2:
                self.rect=self.rect.move(0,-speed)
            if direction==3:
                self.rect=self.rect.move(-speed,0)
            if direction==4:
                self.rect=self.rect.move(speed,0)
        
    def turn_on(self):
        pass

    def update(self):
        screen.screen.blit(self.image,self.rect)

    def update_2(self):
        screen.screen.blit(self.image,self.rect)
