## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
from pygame.locals import *
import os,sys,random,pygame,player
import cPickle as pickle

import screen,helpers,options,specials,weapons,bullets
pygame.init()

class Enemy_silver:
    def __init__(self,x,y):
        self.enemy_down=helpers.load_image('enemy_down.png',-1)
        self.enemy_up=helpers.load_image('enemy_down.png',-1)
        self.enemy_left=helpers.load_image('enemy_down.png',-1)
        self.enemy_right=helpers.load_image('enemy_down.png',-1)

        self.image=self.enemy_down
        if self.image==self.enemy_down:
            self.image1=1

        self.rect=self.image.get_rect(topleft=(x+8,y+8))

        self.health=5

        self.name='silver'

        self.attack_area=0
        self.attack_area_rect=0

        self.damage=15

        self.player_speed=options.player_speed
        self.speed=3
        self.direction=random.randint(1,4)
        self.move_type='random'

    def move(self,walls):
        if self.move_type=='random':
            self.new_dir=random.randint(1,100)
            if self.new_dir<10:
                self.direction=random.randint(1,4)
            if self.direction==1:
                self.rect=self.rect.move(0,self.speed)
                self.image=self.enemy_down
            if self.direction==2:
                self.rect=self.rect.move(0,-self.speed)
                self.image=self.enemy_up
            if self.direction==3:
                self.rect=self.rect.move(-self.speed,0)
                self.image=self.enemy_left
            if self.direction==4:
                self.rect=self.rect.move(self.speed,0)
                self.image=self.enemy_right
            for item in walls:
                if self.rect.colliderect(item):
                    if self.direction==1:
                        self.rect=self.rect.move(0,-self.speed)
                    if self.direction==2:
                        self.rect=self.rect.move(0,self.speed)
                    if self.direction==3:
                        self.rect=self.rect.move(self.speed,0)
                    if self.direction==4:
                        self.rect=self.rect.move(-self.speed,0)

                    self.direction=random.randint(1,4)
        else:
            pass
    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)

    def move_screen(self,x,y):
        self.rect.move_ip(x,y)

    def update(self,bullets):
        for item in bullets:
            if self.rect.colliderect(item):
                self.health=self.health-item.damage
                item.show=item.show-1
        screen.screen.blit(self.image,self.rect)

class Enemy_blue:
    def __init__(self,x,y):
        self.player=player.Player(x,y)
        self.enemy_down=helpers.load_image('enemyb_down.png',-1)
        self.enemy_up=helpers.load_image('enemyb_down.png',-1)
        self.enemy_left=helpers.load_image('enemyb_down.png',-1)
        self.enemy_right=helpers.load_image('enemyb_down.png',-1)

        self.image=self.enemy_down

        self.rect=self.image.get_rect(topleft=(x+8,y+8))

        self.health=50

        self.name='blue'

        self.attack_area=0
        self.attack_area_rect=0

        self.weapons_slot=[]
        self.pistol=weapons.Pistol(0,0)
        self.pistol_rof=60.00/self.pistol.shoot_rate*options.fps
        self.can_shoot_pistol=1

        self.bullets=[]

        self.damage=15

        self.player_speed=options.player_speed
        self.speed=3
        self.direction=random.randint(1,4)
        self.move_type='random'

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))
        
        self.shoot1=helpers.load_sound('hgun.wav')

        self.weapon=1


    def move(self,walls):
        if self.move_type=='random':
            self.new_dir=random.randint(1,100)
            if self.new_dir<10:
                self.direction=random.randint(1,4)
                self.player.attack(self.direction,self.weapon)
            if self.direction==1:
                self.rect=self.rect.move(0,self.speed)
                self.image=self.enemy_down
            if self.direction==2:
                self.rect=self.rect.move(0,-self.speed)
                self.image=self.enemy_up
            if self.direction==3:
                self.rect=self.rect.move(-self.speed,0)
                self.image=self.enemy_left
            if self.direction==4:
                self.rect=self.rect.move(self.speed,0)
                self.image=self.enemy_right
            for item in walls:
                if self.rect.colliderect(item):
                    if self.direction==1:
                        self.rect=self.rect.move(0,-self.speed)
                    if self.direction==2:
                        self.rect=self.rect.move(0,self.speed)
                    if self.direction==3:
                        self.rect=self.rect.move(self.speed,0)
                    if self.direction==4:
                        self.rect=self.rect.move(-self.speed,0)

                    self.direction=random.randint(1,4)
        else:
            pass
    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)

    def bullets_reverse_move(self,direction):
        if direction==1:
            for item in self.bullets:
                item.player_move(2)
        if direction==2:
            for item in self.bullets:
                item.player_move(1)
        if direction==3:
            for item in self.bullets:
                item.player_move(4)
        if direction==4:
            for item in self.bullets:
                item.player_move(3)

    def bullets_player_move(self,direction):
        if direction==1:
            for item in self.bullets:
                item.player_move(1)
        if direction==2:
            for item in self.bullets:
                item.player_move(2)
        if direction==3:
            for item in self.bullets:
                item.player_move(3)
        if direction==4:
            for item in self.bullets:
                item.player_move(4)

    def move_screen(self,x,y):
        self.rect.move_ip(x,y)

    def update(self,bullets):
        for item in bullets:
            if self.rect.colliderect(item):
                self.health=self.health-item.damage
                item.show=item.show-1
        x=0
        for item in self.bullets:
            if item.show<1:
                del self.bullets[x]
            else:
                item.update(walls,baddies)
            x=x+1
        screen.screen.blit(self.image,self.rect)

class Tank:
    def __init__(self,x,y):
        self.tank_down=helpers.load_image('tank_down.png',-1)
        self.tank_up=helpers.load_image('tank_up.png',-1)
        self.tank_left=helpers.load_image('tank_left.png',-1)
        self.tank_right=helpers.load_image('tank_right.png',-1)

        self.image=self.tank_down

        self.rect=self.image.get_rect(topleft=(x+8,y+8))

        self.health=100

        self.name='tank'

        self.attack_area=0
        self.attack_area_rect=0

        self.bullets=[]

        self.damage=100

        self.player_speed=options.player_speed
        self.speed=3
        self.direction=random.randint(1,4)
        self.move_type='random'

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))
        
        self.shoot1=helpers.load_sound('hgun.wav')

        self.weapon=1

    def move(self,walls):
        if self.move_type=='random':
            self.new_dir=random.randint(1,100)
            if self.new_dir<10:
                self.direction=random.randint(1,4)
            if self.direction==1:
                self.rect=self.rect.move(0,self.speed)
                self.image=self.tank_down
            if self.direction==2:
                self.rect=self.rect.move(0,-self.speed)
                self.image=self.tank_up
            if self.direction==3:
                self.rect=self.rect.move(-self.speed,0)
                self.image=self.tank_left
            if self.direction==4:
                self.rect=self.rect.move(self.speed,0)
                self.image=self.tank_right
            for item in walls:
                if self.rect.colliderect(item):
                    if self.direction==1:
                        self.rect=self.rect.move(0,-self.speed)
                    if self.direction==2:
                        self.rect=self.rect.move(0,self.speed)
                    if self.direction==3:
                        self.rect=self.rect.move(self.speed,0)
                    if self.direction==4:
                        self.rect=self.rect.move(-self.speed,0)

                    self.direction=random.randint(1,4)
                    
        else:
            pass
    def player_move(self,direction):
        if direction==1:
            self.rect=self.rect.move(0,self.player_speed)
        if direction==2:
            self.rect=self.rect.move(0,-self.player_speed)
        if direction==3:
            self.rect=self.rect.move(-self.player_speed,0)
        if direction==4:
            self.rect=self.rect.move(self.player_speed,0)

    def move_screen(self,x,y):
        self.rect.move_ip(x,y)

    def update(self,bullets):
        for item in bullets:
            if self.rect.colliderect(item):
                self.health=self.health-item.damage
                item.show=item.show-1
        screen.screen.blit(self.image,self.rect)
