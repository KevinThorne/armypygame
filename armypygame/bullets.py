## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame

## basic imports
import helpers,screen,options

class PistolBullets:
    def __init__(self,x,y,direction):
        self.image=helpers.load_image('black bullet.png',-1)
        self.rect=self.image.get_rect(topleft=(x+5,y+10))
        self.sound=helpers.load_sound('hgun.wav')

        self.direction=direction
        
        self.player_speed=options.player_speed

        self.speed=self.player_speed + 5

        

        self.show=1

        self.damage=3
        
    def update(self,walls,baddies):
        if self.direction==1:
            self.rect=self.rect.move(0,-self.speed)
        if self.direction==2:
            self.rect=self.rect.move(0,self.speed)
        if self.direction==3:
            self.rect=self.rect.move(self.speed,0)
        if self.direction==4:
            self.rect=self.rect.move(-self.speed,0)

        screen.screen.blit(self.image,self.rect)
        for item in walls:
            if item.colliderect(self.rect):
                self.show=0
        for item in baddies:
            if item.rect.colliderect(self.rect):
                self.show=0

    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)
            
class RifleBullets:
    def __init__(self,x,y,direction):
        self.image=helpers.load_image('black bullet.png',-1)
        self.rect=self.image.get_rect(topleft=(x+5,y+10))

        self.direction=direction
        self.player_speed=options.player_speed

        self.speed=self.player_speed + 7

        self.show=1

        self.damage=5
        
    def update(self,walls,baddies):
        if self.direction==1:
            self.rect=self.rect.move(0,-self.speed)
        if self.direction==2:
            self.rect=self.rect.move(0,self.speed)
        if self.direction==3:
            self.rect=self.rect.move(self.speed,0)
        if self.direction==4:
            self.rect=self.rect.move(-self.speed,0)

        screen.screen.blit(self.image,self.rect)
        for item in walls:
            if item.colliderect(self.rect):
                self.show=0
        for item in baddies:
            if item.rect.colliderect(self.rect):
                self.show=0

    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)

class MachineGunBullets:
    def __init__(self,x,y,direction):
        self.image=helpers.load_image('black bullet.png',-1)
        self.rect=self.image.get_rect(topleft=(x+5,y+10))

        self.direction=direction

        self.player_speed=options.player_speed

        self.speed=options.player_speed+3

        

        self.show=1

        self.damage=5
        
    def update(self,walls,baddies):
        if self.direction==1:
            self.rect=self.rect.move(0,-self.speed)
        if self.direction==2:
            self.rect=self.rect.move(0,self.speed)
        if self.direction==3:
            self.rect=self.rect.move(self.speed,0)
        if self.direction==4:
            self.rect=self.rect.move(-self.speed,0)

        screen.screen.blit(self.image,self.rect)
        for item in walls:
            if item.colliderect(self.rect):
                self.show=0
        for item in baddies:
            if item.rect.colliderect(self.rect):
                self.show=0

    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)

class FlameThrowerBullets:
    def __init__(self,x,y,direction):
        self.image=helpers.load_image('flame.png',-1)
        self.rect=self.image.get_rect(topleft=(x+5,y+10))

        self.direction=direction

        self.speed=options.player_speed+1

        self.player_speed=options.player_speed

        self.show=1

        self.damage=20

        self.life=options.fps*.1
        
    def update(self,walls,baddies):
        
        if self.direction==1:
            self.rect=self.rect.move(0,-self.speed)
        if self.direction==2:
            self.rect=self.rect.move(0,self.speed)
        if self.direction==3:
            self.rect=self.rect.move(self.speed,0)
        if self.direction==4:
            self.rect=self.rect.move(-self.speed,0)

        screen.screen.blit(self.image,self.rect)
        for item in walls:
            if item.colliderect(self.rect):
                self.show=0

        self.life=self.life-1
        if self.life==0:
            self.show=0

    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)
        
