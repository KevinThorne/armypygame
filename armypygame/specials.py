from pygame.locals import *
import os,sys,random,pygame

import helpers,screen,options
## for the font we use later
pygame.init()
#,player,slot_1,slot_2,slot_3

class Heart:
    def __init__(self,x,y):
        self.name='heart'

        self.image=helpers.load_image('heart.png',-1)
        self.rect=self.image.get_rect(topleft=(x,y+8))

        self.player_speed=options.player_speed
        self.alive=1

    def pickup(self,player):
        if self.rect.colliderect(player):
            self.show=0
            player.health=player.health+10

    def update(self):
        screen.screen.blit(self.image,self.rect)

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
        self.rect=self.rect.move(x,y)
