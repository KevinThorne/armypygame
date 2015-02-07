## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame

## basic imports
import helpers,screen,options

import cPickle as pickle

class Pistol:
    def __init__(self,x,y):
        self.image=helpers.load_image('Pistol.png',-1)
        self.rect=self.image.get_rect(topleft=(x+9,y+10))
        self.sound=helpers.load_sound('pickup.wav')
        self.sound1=helpers.load_sound('hgun.wav')

        ## shots per minute
        self.shoot_rate=120

        ## how much dmg it does
        self.damage=30000000000000

        ## what slot the weapon goes
        self.slot_number=1

        ## show the pistol on screen or not to
        self.show=1

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))
        
    def pickup(self,player):
        if self.rect.colliderect(player):
            self.show=0
            self.image=helpers.load_image('Pistol.png',-1)
            self.rect=self.image.get_rect(topleft=(10,10))
            if self.sounds==0:
                self.sound.play()

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
        
    def shoot(self):
        pass

    def update(self):
        screen.screen.blit(self.image,self.rect)

    def update_2(self):
        screen.screen.blit(self.image,self.rect)
        


class Rifle:
    def __init__(self,x,y):
        self.image=helpers.load_image('rifle.png',-1)
        self.rect=self.image.get_rect(topleft=(x,y+11))
        self.sound=helpers.load_sound('reload.wav')

        ## shots per minute
        self.shoot_rate=160

        ## how much dmg it does
        self.damage=30000000000000

        ## what slot the weapon goes
        self.slot_number=2

        self.show=1

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))

    def pickup(self,player):
        if self.rect.colliderect(player):
            self.show=0
            self.image=helpers.load_image('rifle.png',-1)
            self.rect=self.image.get_rect(topleft=(35,10))
            if self.sounds==0:
                self.sound.play()

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
        
    def shoot(self):
        pass

    def update(self):
        screen.screen.blit(self.image,self.rect)

    def update_2(self):
        screen.screen.blit(self.image,self.rect)


class MachineGun:
    def __init__(self,x,y):
        self.image=helpers.load_image('Machine Gun.png',-1)
        self.rect=self.image.get_rect(topleft=(x,y+10))
        self.sound=helpers.load_sound('pickup.wav')

        ## shots per minute
        self.shoot_rate=480

        ## how much dmg it does
        self.damage=4

        ## what slot the weapon goes
        self.slot_number=1

        ## show the pistol on screen or not to
        self.show=1

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))
        
    def pickup(self,player):
        if self.rect.colliderect(player):
            self.show=0
            self.image=helpers.load_image('Machine Gun.png',-1)
            self.rect=self.image.get_rect(topleft=(65,10))
            if self.sounds==0:
                self.sound.play()
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
        
    def shoot(self):
        pass

    def update(self):
        screen.screen.blit(self.image,self.rect)

    def update_2(self):
        screen.screen.blit(self.image,self.rect)

class FlameThrower:
    def __init__(self,x,y):
        self.image=helpers.load_image('Machine Gun.png',-1)
        self.rect=self.image.get_rect(topleft=(x,y+10))
        self.sound=helpers.load_sound('rl1.wav')

        ## shots per minute
        self.shoot_rate=480*10

        ## how much dmg it does
        self.damage=4

        ## what slot the weapon goes
        self.slot_number=1

        ## show the pistol on screen or not to
        self.show=1

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))
        
    def pickup(self,player):
        if self.rect.colliderect(player):
            self.show=0
            self.image=helpers.load_image('Machine Gun.png',-1)
            self.rect=self.image.get_rect(topleft=(95,10))
            if self.sounds==0:
                self.sound.play()

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
        
    def shoot(self):
        pass

    def update(self):
        screen.screen.blit(self.image,self.rect)

    def update_2(self):
        screen.screen.blit(self.image,self.rect)
