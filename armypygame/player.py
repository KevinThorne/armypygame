from pygame.locals import *
import os,sys,random,pygame

## these are the three .py we will need for the player code
import screen,helpers,options,weapons,bullets,mainmenu

import cPickle as pickle

class Player:
    def __init__(self,x,y):
        self.x=x+8
        self.y=y+8

        self.player_down=helpers.load_image('player_down.png',-1)
        self.player_up=helpers.load_image('player_up.png',-1)
        self.player_right=helpers.load_image('player_right.png',-1)
        self.player_left=helpers.load_image('player_left.png',-1)

        self.image=self.player_down
        if self.image==self.player_down:
            self.image1=1
        else:
            self.image1=2
        self.rect=self.image.get_rect(topleft=(self.x,self.y))

        self.speed=options.player_speed

        self.health=100

        self.weapons_slot=[]
        self.pistol=weapons.Pistol(0,0)
        self.pistol_rof=60.00/self.pistol.shoot_rate*options.fps
        self.can_shoot_pistol=0

        self.rifle=weapons.Rifle(0,0)
        self.rifle_rof=60.00/self.rifle.shoot_rate*options.fps
        self.can_shoot_rifle=0

        self.machine_gun=weapons.MachineGun(0,0)
        self.machine_gun_rof=60.00/self.machine_gun.shoot_rate*options.fps
        self.can_shoot_machine_gun=0

        self.flame_thrower=weapons.FlameThrower(0,0)
        self.flame_thrower_rof=60.00/self.flame_thrower.shoot_rate*options.fps
        self.can_shoot_flame_thrower=0

        self.bullets=[]

        self.blinking=0

        self.recover_time=15

        self.shoot1=helpers.load_sound('hgun.wav')
        self.shoot2=helpers.load_sound('hgun.wav')
        self.shoot3=helpers.load_sound('mgun.wav')
        self.shoot4=helpers.load_sound('rl1.wav')

        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))


    def move(self,direction):
        if direction==1:
            self.image=self.player_up

        if direction==2:
            self.image=self.player_down

        if direction==3:
            self.image=self.player_right

        if direction==4:
            self.image=self.player_left


    def check_for_end(self,end):
        pass

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

    def attack(self,direction,active_weapon):
        if active_weapon==0:
            pass

        else:
            if active_weapon==1:
                if self.can_shoot_pistol<0:
                    self.can_shoot_pistol=self.pistol_rof
                    bullet=bullets.PistolBullets(self.x,self.y,direction)
                    self.bullets.append(bullet)
                    if self.sounds==0:
                        self.shoot1.play()
                else:
                    pass
            if active_weapon==2:
                if self.can_shoot_rifle<0:
                    self.can_shoot_rifle=self.rifle_rof
                    bullet=bullets.RifleBullets(self.x,self.y,direction)
                    self.bullets.append(bullet)
                    if self.sounds==0:
                        self.shoot2.play()
                else:
                    pass

            if active_weapon==3:
                if self.can_shoot_machine_gun<0:
                    self.can_shoot_machine_gun=self.machine_gun_rof
                    bullet=bullets.MachineGunBullets(self.x,self.y,direction)
                    self.bullets.append(bullet)
                    if self.sounds==0:
                        self.shoot3.play()
                else:
                    pass
            if active_weapon==4:
                if self.can_shoot_flame_thrower<0:
                    self.can_shoot_flame_thrower=self.flame_thrower_rof
                    bullet=bullets.FlameThrowerBullets(self.x,self.y,direction)
                    self.bullets.append(bullet)
                else:
                    pass


    def die(self,creature):
        pass

    def update(self,walls,baddies):
        self.blinking=self.blinking-1
        x=0
        for item in self.bullets:
            if item.show<1:
                del self.bullets[x]
            else:
                item.update(walls,baddies)
            x=x+1
        for item in baddies:
            if self.rect.colliderect(item):
                if self.blinking<0:
                    self.health=self.health-item.damage
                    self.blinking=self.recover_time
                else:
                    pass
        self.can_shoot_pistol=self.can_shoot_pistol-1
        self.can_shoot_rifle=self.can_shoot_rifle-1
        self.can_shoot_machine_gun=self.can_shoot_machine_gun-1
        self.can_shoot_flame_thrower=self.can_shoot_flame_thrower-1
        screen.screen.blit(self.image,self.rect)


        

        
