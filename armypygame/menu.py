## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame

import helpers,screen
## for the font we use later
pygame.init()
#,player,slot_1,slot_2,slot_3
class Menu:
    def __init__(self):
        self.image=helpers.load_image('white bottom.png',0)
        self.rect=self.image.get_rect(topleft=(0,0))

        self.arrow=helpers.load_image('arrow.png',-1)
        self.arrow_rect=self.arrow.get_rect(topleft=(1000,1000))
        

    def update(self,player,flashlight,pistol,rifle,machine_gun,flame_thrower,active,message,instructions,tips):
        screen.screen.blit(self.image,self.rect)
        screen.screen.blit((pygame.font.Font(None, 30).render('HP: '+str(player.health),1,(0,0,0))),((10,75)))
        screen.screen.blit((pygame.font.Font(None, 25).render(message,1,(0,0,0))),((100,40)))
        screen.screen.blit((pygame.font.Font(None, 25).render('Instructions - '+instructions,1,(0,0,0))),((100,60)))
        screen.screen.blit((pygame.font.Font(None, 25).render('Tips - '+tips,1,(0,0,0))),((100,80)))
        if pistol.show==0:
            pistol.update_2()
        if rifle.show==0:
            rifle.update_2()
        if machine_gun.show==0:
            machine_gun.update_2()
        if flame_thrower.show==0:
            flame_thrower.update_2()
        if flashlight.show==0:
            flashlight.update_2()
        if active==1:
            self.arrow_rect=self.arrow.get_rect(topleft=(10,25))
            screen.screen.blit(self.arrow,self.arrow_rect)
        if active==2:
            self.arrow_rect=self.arrow.get_rect(topleft=(40,25))
            screen.screen.blit(self.arrow,self.arrow_rect)
        if active==3:
            self.arrow_rect=self.arrow.get_rect(topleft=(80,25))
            screen.screen.blit(self.arrow,self.arrow_rect)
        if active==4:
            self.arrow_rect=self.arrow.get_rect(topleft=(105,25))
            screen.screen.blit(self.arrow,self.arrow_rect)
        if active==10:
            self.arrow_rect=self.arrow.get_rect(topleft=(10,55))
            screen.screen.blit(self.arrow,self.arrow_rect)
