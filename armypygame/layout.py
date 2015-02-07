
## These are the basic functions you need to import
## from pygame.locals import * imports things needed for sound and pictures
## import os,sys import game quit and game load gfeatures
## import random and pygame are things nessacery for some functions as well
## screen is a nessesity for loading images
from pygame.locals import *
import os,sys,random,pygame,screen


## import our load_image functions and our player functions
## with the weapons classes as well as baddies with the menus
## needed with darkness as well 
import helpers,player,weapons,menu,darkness,flashlight,baddies
## these are the keys and doors that will be used
import options,specials
## A class if a setr of functions oyu can name and call
## for example i have a Robot class
## class Robot:
## i can make a robot instance
## by saying  robot=Robot()
## then inside the class Robot:
## def __init__(self,x,y):
## the sself makes the defenotions in the class cooperate
## the x,y can be used for just about anyhting oyu want them to be
## example
## class Name:
##     def __init__(self,name):
##         print 'hello ',name
## when you called class name like
## name=Name('Theo')
## it would print hello Theo When you ran the program



## level 1
class Layout_1:
    ## the init stands for initialization
    def __init__(self):
        ## our background_color numbers between 0-255
        self.backgroud_color=(0,128,0)## black
        ## these are things that will auto display when
        ## the level starts
        self.message='Finish each mission'
        self.instructions='Use the arrow keys to move.'
        self.tips='Look for the end star.'
        ## this is a list with things added to it
        ## this is the layout list every number/letter is a
        ## object in our world functions later will make them appear
        ## since this is level 1 all we need is the player,walls and the end
        ## p=player
        ## w=walls
        ## e=end
        self.layout=['wwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw5',
                     '0wpw0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     '0w0w0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     '0w1w0000000r00000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     '0w0w0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw4',
                     '00h00000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     'ww000000w9w000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     '9w000000w9w000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     '9w000000www000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw3',
                     'ww000000000000a00000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     'w0000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000wwww0000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     '000000999w0000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000wwww0000000000wwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w0000000000000000000ewbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     'wwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw2',]

        self.pistol_x=1000000000000000000000000000000000
        self.pistol_y=1000000000000000000000000000000000
        self.rifle_x=1000000000000000000000000000000000
        self.rifle_y=1000000000000000000000000000000000
        self.machine_gun_x=1000000000000000000000000000000000
        self.machine_gun_y=1000000000000000000000000000000000
        self.flashlight_x=10000000000000000000000000000
        self.flashlight_y=10000000000000000000000000000

        self.slot_1=0
        self.slot_2=0
        self.slot_3=0
        self.slot_4=0
        self.slot_10=0

        self.darkness_on=options.level_1_darkness

        self.darkness=darkness.Darkness(self.darkness_on)
        self.gotflashlight=0
        self.flashlight_on=0

        self.active_weapon=None
                     
                     

        ## these are the images used for level 1
        self.wall_picture=helpers.load_image('wall.png',0)
        self.floor_picture=helpers.load_image('floor.png',0)
        self.floor1_picture=helpers.load_image('floor1.png',0)
        self.end_picture=helpers.load_image('end.png',0)
        self.ruins1=helpers.load_image('ruins1.png',0)
        self.ruins2=helpers.load_image('ruins2.png',0)
        choose=random.randint(1, 2)
        if choose==1:
            self.ruins=self.ruins1
        elif choose==2:
            self.ruins=self.ruins2

        self.menu=menu.Menu()
                

        ## these are empty lists
        ## these are the lists that will update everything
        ## explained in the later functions
        self.walls=[]
        self.floors=[]
        self.ends=[]
        self.weapons=[]

        self.wall_rects=[]
        self.floor_rects=[]
        self.end_rects=[]
        self.weapon_rects=[]

        ## there are no creatures in this map
        ## in later ones they will be added
        self.creatures=[]

        ##keys
        self.key=[]
        ##doors
        self.doors=[]
        ##others
        self.specials=[]

        ## These next functions are very tempermantal
        ## Dont mess with them unless the changes are approved
        self.height=len(self.layout)
        self.width=len(self.layout[0])

        max_y = self.height-1

        ## variable needed for screen flip
        self.z=0
        self.z=self.z+(32*self.height)-32
        for x in range(self.width):
            
            for y in range(self.height):
                char=self.layout[max_y-y][x]
                ## call the cheate char function
                ## this makes the characters appear
                self.create_char((x,y),char)

        ## past tempermental zone
        
        self.move_x=self.x
        self.move_y=self.y
        self.move_spec_x=0
        self.move_spec_y=0
        ## screen.size is in screen.py look for more info
        while 1:
            if self.move_x<screen.size[0]/2-32:
                self.move_screen(1)
            if self.move_x>screen.size[0]/2-32:
                self.move_screen(2)
            if self.move_y<screen.size[1]/2-32:
                self.move_screen(3)
            if self.move_y>screen.size[1]/2-32:
                self.move_screen(4)

            if self.move_x==screen.size[0]/2-32 and self.move_y==screen.size[1]/2-32:
                self.move_screen(5)
                self.x=screen.size[0]/2+4
                self.y=screen.size[1]/2+4
                self.pistol_x=self.pistol_x+self.move_spec_x
                self.pistol_y=self.pistol_y+self.move_spec_y
                self.rifle_x=self.rifle_x+self.move_spec_x
                self.rifle_y=self.rifle_y+self.move_spec_y
                self.machine_gun_x=self.machine_gun_x+self.move_spec_x
                self.machine_gun_y=self.machine_gun_y+self.move_spec_y
                self.flashlight_x=self.flashlight_x+self.move_spec_x
                self.flashlight_y=self.flashlight_y+self.move_spec_y
                self.flame_thrower_x=self.flame_thrower_x+self.move_spec_x
                self.flame_thrower_y=self.flame_thrower_y+self.move_spec_y
                break

        self.player=player.Player(self.x,self.y)
        self.pistol=weapons.Pistol(self.pistol_x,self.pistol_y)
        self.machine_gun=weapons.MachineGun(self.machine_gun_x,self.machine_gun_y)
        self.rifle=weapons.Rifle(self.rifle_x,self.rifle_y)
        self.flame_thrower=weapons.FlameThrower(self.flame_thrower_x,self.flame_thrower_y)
        self.flashlightx=flashlight.Flashlight(self.flashlight_x,self.flashlight_y)
        self.flashlight_click=0
        self.recharge_flashlight_click=10
        
        




    def create_char(self,point,char):
        ## Try to figure this part out ask questions if nessisary
        (x,y)=point
        x=x*32
        y=y*32
        y=y*(-1)
        y=y+self.z
        if char=='w':
            ## make a sprite
            self.wall=self.wall_picture
            ## add it to the list
            self.walls.append(self.wall)
            ## make the rect
            self.rect=self.wall.get_rect(topleft=(x,y))
            ## add it to the list
            self.wall_rects.append(self.rect)
        if char=='0':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='p':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.x=x
            self.y=y
        if char=='e':
            self.end=self.end_picture
            self.ends.append(self.end)
            self.rect=self.end.get_rect(topleft=(x,y))
            self.end_rects.append(self.rect)
        if char=='1':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.pistol_x=x
            self.pistol_y=y
        if char=='2':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.rifle_x=x
            self.rifle_y=y
        if char=='3':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.machine_gun_x=x
            self.machine_gun_y=y
        if char=='4':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flashlight_x=x
            self.flashlight_y=y
        if char=='5':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flame_thrower_x=x
            self.flame_thrower_y=y
        if char=='9':
            self.floor=self.floor1_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)

        if char=='a':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Enemy_silver(x,y)
            self.creatures.append(baddy)
        if char=='r':
            self.floor=self.ruins
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='h':
            self.special=specials.Heart(x,y)
            self.specials.append(self.special)
        if char=='t':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Tank(x,y)
            self.creatures.append(baddy)
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
    def update(self):
        self.flashlight_click=self.flashlight_click-1
        x=0
        for item in self.creatures:
            if item.health<=0:
                if item.name=='silver':
                    self.special=specials.Heart(item.rect[0],item.rect[1])
                    self.specials.append(self.special)
                del self.creatures[x]
            else:
                item.move(self.wall_rects)
            x=x+1
        if self.pistol.rect.colliderect(self.player):
            self.pistol.pickup(self.player)
            self.slot_1=1
        if self.rifle.rect.colliderect(self.player):
            self.rifle.pickup(self.player)
            self.slot_2=2
        if self.machine_gun.rect.colliderect(self.player):
            self.machine_gun.pickup(self.player)
            self.slot_3=3
        if self.flame_thrower.rect.colliderect(self.player):
            self.flame_thrower.pickup(self.player)
            self.slot_4=4
        if self.flashlightx.rect.colliderect(self.player):
           self.flashlightx.pickup(self.player)
           self.slot_10=10
        x=0
        
        ## make the background the color of our choice
        screen.screen.fill(self.backgroud_color)
        ## define the number
        x=0
        ## call the list
        for item in self.floor_rects:
            ## blit item on the screen
            screen.screen.blit(self.floors[x],item)
            ## increase the number by one
            x=x+1

        x=0
        for item in self.wall_rects:
            screen.screen.blit(self.walls[x],item)
            x=x+1
        x=0
        for item in self.end_rects:
            screen.screen.blit(self.ends[x],item)
            x=x+1

        for item in self.creatures:
            item.update(self.player.bullets)

        

        self.player.update(self.wall_rects,self.creatures)

        self.pistol.update()
        self.rifle.update()
        self.machine_gun.update()
        self.flashlightx.update()
        self.flame_thrower.update()

        self.darkness.update(self.flashlightx,self.flashlight_on)
        
        
        self.menu.update(self.player,self.flashlightx,self.pistol,
                         self.rifle,self.machine_gun,self.flame_thrower,self.active_weapon,
                         self.message,self.instructions,self.tips)


    def player_moves(self,command,direction):
        ## self explanatory
        if command=='move':
            self.player.move(direction)
            if direction==1:
                self.player.bullets_player_move(1)
                self.pistol.move(1,self.player.speed)
                self.rifle.move(1,self.player.speed)
                self.machine_gun.move(1,self.player.speed)
                self.flame_thrower.move(1,self.player.speed)
                self.flashlightx.move(1,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.creatures:
                    item.player_move(1)
            if direction==2:
                self.player.bullets_player_move(2)
                self.pistol.move(2,self.player.speed)
                self.machine_gun.move(2,self.player.speed)
                self.rifle.move(2,self.player.speed)
                self.flashlightx.move(2,self.player.speed)
                self.flame_thrower.move(2,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.creatures:
                    item.player_move(2)
            if direction==3:
                self.player.bullets_player_move(3)
                self.pistol.move(3,self.player.speed)
                self.machine_gun.move(3,self.player.speed)
                self.rifle.move(3,self.player.speed)
                self.flashlightx.move(3,self.player.speed)
                self.flame_thrower.move(3,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.creatures:
                    item.player_move(3)
            if direction==4:
                self.player.bullets_player_move(4)
                self.pistol.move(4,self.player.speed)
                self.rifle.move(4,self.player.speed)
                self.machine_gun.move(4,self.player.speed)
                self.flashlightx.move(4,self.player.speed)
                self.flame_thrower.move(4,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.creatures:
                    item.player_move(4)

            for item in self.wall_rects:
                if self.player.rect.colliderect(item):
                    self.reverse_move(direction)
            x=0
        if command=='attack':
            if self.active_weapon==10:
                self.flashlight_on_off()
            else:
                self.player.attack(direction,self.active_weapon)
        if command=='switch':
            pass

    def reverse_move(self,direction):
        if direction==1:
            self.player.bullets_reverse_move(1)
            self.pistol.move(2,self.player.speed)
            self.rifle.move(2,self.player.speed)
            self.machine_gun.move(2,self.player.speed)
            self.flame_thrower.move(2,self.player.speed)
            self.flashlightx.move(2,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.creatures:
                item.player_move(2)
        if direction==2:
            self.player.bullets_reverse_move(2)
            self.pistol.move(1,self.player.speed)
            self.rifle.move(1,self.player.speed)
            self.flame_thrower.move(1,self.player.speed)
            self.machine_gun.move(1,self.player.speed)
            self.flashlightx.move(1,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.creatures:
                item.player_move(1)
        if direction==3:
            self.player.bullets_reverse_move(3)
            self.pistol.move(4,self.player.speed)
            self.rifle.move(4,self.player.speed)
            self.machine_gun.move(4,self.player.speed)
            self.flashlightx.move(4,self.player.speed)
            self.flame_thrower.move(4,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.creatures:
                item.player_move(4)
        if direction==4:
            self.player.bullets_reverse_move(4)
            self.pistol.move(3,self.player.speed)
            self.rifle.move(3,self.player.speed)
            self.flame_thrower.move(3,self.player.speed)
            self.machine_gun.move(3,self.player.speed)
            self.flashlightx.move(3,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.creatures:
                item.player_move(3)

    def flashlight_on_off(self):
        self.clicked=1
        if self.flashlight_click<0:
            if self.flashlight_on==0 and self.clicked==1:
                self.flashlight_on=1
                self.clicked=0
            if self.flashlight_on==1 and self.clicked==1:
                self.flashlight_on=0
                self.clicked=0
            self.flashlight_click=self.recharge_flashlight_click

    def move_screen(self,x):
        if x==1:
            self.move_x=self.move_x+1
            self.move_spec_x=self.move_spec_x+1
        if x==2:
            self.move_x=self.move_x-1
            self.move_spec_x=self.move_spec_x-1
        if x==3:
            self.move_y=self.move_y+1
            self.move_spec_y=self.move_spec_y+1
        if x==4:
            self.move_y=self.move_y-1
            self.move_spec_y=self.move_spec_y-1
        if x==5:
            self.move_spec_x=self.move_spec_x+36
            self.move_spec_y=self.move_spec_y+42
            for item in self.wall_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.floor_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.end_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.creatures:
                item.move_screen(self.move_spec_x,self.move_spec_y)
class Layout_2:
    def __init__(self):
        ## our background_color numbers between 0-255
        self.backgroud_color=(0,128,0)## black
        ## these are things that will auto display when
        ## the level starts
        self.message='Go and destroy the silver dudes'
        self.instructions='Do the above and then report to base(end star)'
        self.tips='[blank]'
        ## this is a list with things added to it
        ## this is the layout list every number/letter is a
        ## object in our world functions later will make them appear
        ## since this is level 1 all we need is the player,walls and the end
        ## p=player
        ## w=walls
        ## e=end
        self.layout=['wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww0wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw4',
                     'wpw000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
                     'w1w00000000000000ww0000000000000000d000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w9w000000000000009w00000000000d00000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     '09w000000000000009w00000000000000000000wwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000www0000000ww000000000d000000wwwwwwewbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000099w0000000000000000000000000waaaww9wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000099w000000www0000000d00000000waaaww9wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000www00000099w0000000000000000wwaaww9wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000000000000www00000000000000009999aa9wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000wwwwww000000000000000000d000000wwaawwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000w2395w0000000000000000000000000waaawbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000waaa9w0000000d00000d00000000000waaawbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00099999w0000000000000000000000000waaawbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
        self.pistol_x=1000000000000000000000000000000000
        self.pistol_y=1000000000000000000000000000000000
        self.rifle_x=1000000000000000000000000000000000
        self.rifle_y=1000000000000000000000000000000000
        self.machine_gun_x=1000000000000000000000000000000000
        self.machine_gun_y=1000000000000000000000000000000000
        self.flashlight_x=10000000000000000000000000000
        self.flashlight_y=10000000000000000000000000000

        self.slot_1=0
        self.slot_2=0
        self.slot_3=0
        self.slot_4=0
        self.slot_10=0

        self.darkness_on=options.level_1_darkness

        self.darkness=darkness.Darkness(self.darkness_on)
        self.gotflashlight=0
        self.flashlight_on=0

        self.active_weapon=None
                     
                     

        ## these are the images used for level 1
        self.wall_picture=helpers.load_image('wall.png',0)
        self.floor_picture=helpers.load_image('floor.png',0)
        self.floor1_picture=helpers.load_image('floor1.png',0)
        self.end_picture=helpers.load_image('end.png',0)
        self.ruins1=helpers.load_image('ruins1.png',0)
        self.ruins2=helpers.load_image('ruins2.png',0)
        self.dead=helpers.load_image('dead.png',0)
        choose=random.randint(1, 2)
        if choose==1:
            self.ruins=self.ruins1
        elif choose==2:
            self.ruins=self.ruins2

        self.menu=menu.Menu()
                

        ## these are empty lists
        ## these are the lists that will update everything
        ## explained in the later functions
        self.walls=[]
        self.floors=[]
        self.ends=[]
        self.weapons=[]

        self.wall_rects=[]
        self.floor_rects=[]
        self.end_rects=[]
        self.weapon_rects=[]

        ## there are no creatures in this map
        ## in later ones they will be added
        self.creatures=[]

        ##keys
        self.key=[]
        ##doors
        self.doors=[]
        ##others
        self.specials=[]

        ## These next functions are very tempermantal
        ## Dont mess with them unless the changes are approved
        self.height=len(self.layout)
        self.width=len(self.layout[0])

        max_y = self.height-1

        ## variable needed for screen flip
        self.z=0
        self.z=self.z+(32*self.height)-32
        for x in range(self.width):
            
            for y in range(self.height):
                char=self.layout[max_y-y][x]
                ## call the cheate char function
                ## this makes the characters appear
                self.create_char((x,y),char)

        ## past tempermental zone
        
        self.move_x=self.x
        self.move_y=self.y
        self.move_spec_x=0
        self.move_spec_y=0
        ## screen.size is in screen.py look for more info
        while 1:
            if self.move_x<screen.size[0]/2-32:
                self.move_screen(1)
            if self.move_x>screen.size[0]/2-32:
                self.move_screen(2)
            if self.move_y<screen.size[1]/2-32:
                self.move_screen(3)
            if self.move_y>screen.size[1]/2-32:
                self.move_screen(4)

            if self.move_x==screen.size[0]/2-32 and self.move_y==screen.size[1]/2-32:
                self.move_screen(5)
                self.x=screen.size[0]/2+4
                self.y=screen.size[1]/2+4
                self.pistol_x=self.pistol_x+self.move_spec_x
                self.pistol_y=self.pistol_y+self.move_spec_y
                self.rifle_x=self.rifle_x+self.move_spec_x
                self.rifle_y=self.rifle_y+self.move_spec_y
                self.machine_gun_x=self.machine_gun_x+self.move_spec_x
                self.machine_gun_y=self.machine_gun_y+self.move_spec_y
                self.flashlight_x=self.flashlight_x+self.move_spec_x
                self.flashlight_y=self.flashlight_y+self.move_spec_y
                self.flame_thrower_x=self.flame_thrower_x+self.move_spec_x
                self.flame_thrower_y=self.flame_thrower_y+self.move_spec_y
                break

        self.player=player.Player(self.x,self.y)
        self.pistol=weapons.Pistol(self.pistol_x,self.pistol_y)
        self.machine_gun=weapons.MachineGun(self.machine_gun_x,self.machine_gun_y)
        self.rifle=weapons.Rifle(self.rifle_x,self.rifle_y)
        self.flame_thrower=weapons.FlameThrower(self.flame_thrower_x,self.flame_thrower_y)
        self.flashlightx=flashlight.Flashlight(self.flashlight_x,self.flashlight_y)
        self.flashlight_click=0
        self.recharge_flashlight_click=10
        
        




    def create_char(self,point,char):
        ## Try to figure this part out ask questions if nessisary
        (x,y)=point
        x=x*32
        y=y*32
        y=y*(-1)
        y=y+self.z
        if char=='w':
            ## make a sprite
            self.wall=self.wall_picture
            ## add it to the list
            self.walls.append(self.wall)
            ## make the rect
            self.rect=self.wall.get_rect(topleft=(x,y))
            ## add it to the list
            self.wall_rects.append(self.rect)
        if char=='0':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='p':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.x=x
            self.y=y
        if char=='e':
            self.end=self.end_picture
            self.ends.append(self.end)
            self.rect=self.end.get_rect(topleft=(x,y))
            self.end_rects.append(self.rect)
        if char=='1':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.pistol_x=x
            self.pistol_y=y
        if char=='2':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.rifle_x=x
            self.rifle_y=y
        if char=='3':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.machine_gun_x=x
            self.machine_gun_y=y
        if char=='4':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flashlight_x=x
            self.flashlight_y=y
        if char=='5':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flame_thrower_x=x
            self.flame_thrower_y=y
        if char=='9':
            self.floor=self.floor1_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)

        if char=='a':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Enemy_silver(x,y)
            self.creatures.append(baddy)
        if char=='r':
            self.floor=self.ruins
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='d':
            self.floor=self.dead
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='t':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Tank(x,y)
            self.creatures.append(baddy)
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
    def update(self):
        self.flashlight_click=self.flashlight_click-1
        x=0
        for item in self.creatures:
            if item.health<=0:
                if item.name=='silver':
                    self.heart=specials.Heart(item.rect[0],item.rect[1])
                    self.specials.append(self.heart)
                del self.creatures[x]
            else:
                item.move(self.wall_rects)
            x=x+1
        if self.pistol.rect.colliderect(self.player):
            self.pistol.pickup(self.player)
            self.slot_1=1
        if self.rifle.rect.colliderect(self.player):
            self.rifle.pickup(self.player)
            self.slot_2=2
        if self.machine_gun.rect.colliderect(self.player):
            self.machine_gun.pickup(self.player)
            self.slot_3=3
        if self.flame_thrower.rect.colliderect(self.player):
            self.flame_thrower.pickup(self.player)
            self.slot_4=4
        if self.flashlightx.rect.colliderect(self.player):
           self.flashlightx.pickup(self.player)
           self.slot_10=10
        x=0
        
        ## make the background the color of our choice
        screen.screen.fill(self.backgroud_color)
        ## define the number
        x=0
        ## call the list
        for item in self.floor_rects:
            ## blit item on the screen
            screen.screen.blit(self.floors[x],item)
            ## increase the number by one
            x=x+1

        x=0
        for item in self.wall_rects:
            screen.screen.blit(self.walls[x],item)
            x=x+1
        x=0
        for item in self.end_rects:
            screen.screen.blit(self.ends[x],item)
            x=x+1

        for item in self.creatures:
            item.update(self.player.bullets)

        

        self.player.update(self.wall_rects,self.creatures)

        self.pistol.update()
        self.rifle.update()
        self.machine_gun.update()
        self.flashlightx.update()
        self.flame_thrower.update()

        self.darkness.update(self.flashlightx,self.flashlight_on)
        
        
        self.menu.update(self.player,self.flashlightx,self.pistol,
                         self.rifle,self.machine_gun,self.flame_thrower,self.active_weapon,
                         self.message,self.instructions,self.tips)


    def player_moves(self,command,direction):
        ## self explanatory
        if command=='move':
            self.player.move(direction)
            if direction==1:
                self.player.bullets_player_move(1)
                self.pistol.move(1,self.player.speed)
                self.rifle.move(1,self.player.speed)
                self.machine_gun.move(1,self.player.speed)
                self.flame_thrower.move(1,self.player.speed)
                self.flashlightx.move(1,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.creatures:
                    item.player_move(1)
            if direction==2:
                self.player.bullets_player_move(2)
                self.pistol.move(2,self.player.speed)
                self.machine_gun.move(2,self.player.speed)
                self.rifle.move(2,self.player.speed)
                self.flashlightx.move(2,self.player.speed)
                self.flame_thrower.move(2,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.creatures:
                    item.player_move(2)
            if direction==3:
                self.player.bullets_player_move(3)
                self.pistol.move(3,self.player.speed)
                self.machine_gun.move(3,self.player.speed)
                self.rifle.move(3,self.player.speed)
                self.flashlightx.move(3,self.player.speed)
                self.flame_thrower.move(3,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.creatures:
                    item.player_move(3)
            if direction==4:
                self.player.bullets_player_move(4)
                self.pistol.move(4,self.player.speed)
                self.rifle.move(4,self.player.speed)
                self.machine_gun.move(4,self.player.speed)
                self.flashlightx.move(4,self.player.speed)
                self.flame_thrower.move(4,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.creatures:
                    item.player_move(4)

            for item in self.wall_rects:
                if self.player.rect.colliderect(item):
                    self.reverse_move(direction)
            x=0
        if command=='attack':
            if self.active_weapon==10:
                self.flashlight_on_off()
            else:
                self.player.attack(direction,self.active_weapon)
        if command=='switch':
            pass

    def reverse_move(self,direction):
        if direction==1:
            self.player.bullets_reverse_move(1)
            self.pistol.move(2,self.player.speed)
            self.rifle.move(2,self.player.speed)
            self.machine_gun.move(2,self.player.speed)
            self.flame_thrower.move(2,self.player.speed)
            self.flashlightx.move(2,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.creatures:
                item.player_move(2)
        if direction==2:
            self.player.bullets_reverse_move(2)
            self.pistol.move(1,self.player.speed)
            self.rifle.move(1,self.player.speed)
            self.flame_thrower.move(1,self.player.speed)
            self.machine_gun.move(1,self.player.speed)
            self.flashlightx.move(1,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.creatures:
                item.player_move(1)
        if direction==3:
            self.player.bullets_reverse_move(3)
            self.pistol.move(4,self.player.speed)
            self.rifle.move(4,self.player.speed)
            self.machine_gun.move(4,self.player.speed)
            self.flashlightx.move(4,self.player.speed)
            self.flame_thrower.move(4,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.creatures:
                item.player_move(4)
        if direction==4:
            self.player.bullets_reverse_move(4)
            self.pistol.move(3,self.player.speed)
            self.rifle.move(3,self.player.speed)
            self.flame_thrower.move(3,self.player.speed)
            self.machine_gun.move(3,self.player.speed)
            self.flashlightx.move(3,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.creatures:
                item.player_move(3)

    def flashlight_on_off(self):
        self.clicked=1
        if self.flashlight_click<0:
            if self.flashlight_on==0 and self.clicked==1:
                self.flashlight_on=1
                self.clicked=0
            if self.flashlight_on==1 and self.clicked==1:
                self.flashlight_on=0
                self.clicked=0
            self.flashlight_click=self.recharge_flashlight_click

    def move_screen(self,x):
        if x==1:
            self.move_x=self.move_x+1
            self.move_spec_x=self.move_spec_x+1
        if x==2:
            self.move_x=self.move_x-1
            self.move_spec_x=self.move_spec_x-1
        if x==3:
            self.move_y=self.move_y+1
            self.move_spec_y=self.move_spec_y+1
        if x==4:
            self.move_y=self.move_y-1
            self.move_spec_y=self.move_spec_y-1
        if x==5:
            self.move_spec_x=self.move_spec_x+36
            self.move_spec_y=self.move_spec_y+42
            for item in self.wall_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.floor_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.end_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.creatures:
                item.move_screen(self.move_spec_x,self.move_spec_y)

class Layout_3:
    def __init__(self):
        ## our background_color numbers between 0-255
        self.backgroud_color=(0,128,0)## black
        ## these are things that will auto display when
        ## the level starts
        self.message='Sometimes you have to do night missions'
        self.instructions='Report to base(end star)'
        self.tips='You can steal the enemys flashlight.  Its quite guarded'
        ## this is a list with things added to it
        ## this is the layout list every number/letter is a
        ## object in our world functions later will make them appear
        ## since this is level 1 all we need is the player,walls and the end
        ## p=player
        ## w=walls
        ## e=end
        self.layout=['wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'wpwwaaa000000000000000000000000000000000wewbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb5',
                     'w3wwaaawwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww0w0wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w1wwaaa0000000000000000000000000000000w0w0wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w2ww0000000000000000000000000000000000w000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'whwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww0wwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000000c0000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000000c0000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w000000000c0000000000000t00000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000040wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'w00000000000000000000000000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                     'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
        self.pistol_x=1000000000000000000000000000000000
        self.pistol_y=1000000000000000000000000000000000
        self.rifle_x=1000000000000000000000000000000000
        self.rifle_y=1000000000000000000000000000000000
        self.machine_gun_x=1000000000000000000000000000000000
        self.machine_gun_y=1000000000000000000000000000000000
        self.flashlight_x=10000000000000000000000000000
        self.flashlight_y=10000000000000000000000000000
        self.heart_x=10000000000000000000000000000
        self.heart_y=10000000000000000000000000000

        self.slot_1=0
        self.slot_2=0
        self.slot_3=0
        self.slot_4=0
        self.slot_10=0

        self.darkness_on=options.level_3_darkness

        self.darkness=darkness.Darkness(self.darkness_on)
        self.gotflashlight=0
        self.flashlight_on=0

        self.active_weapon=None
                     
                     

        ## these are the images used for level 1
        self.wall_picture=helpers.load_image('wall.png',0)
        self.floor_picture=helpers.load_image('floor.png',0)
        self.floor1_picture=helpers.load_image('floor1.png',0)
        self.end_picture=helpers.load_image('end.png',0)
        self.ruins1=helpers.load_image('ruins1.png',0)
        self.ruins2=helpers.load_image('ruins2.png',0)
        self.dead=helpers.load_image('dead.png',0)
        choose=random.randint(1, 2)
        if choose==1:
            self.ruins=self.ruins1
        elif choose==2:
            self.ruins=self.ruins2

        self.menu=menu.Menu()
                

        ## these are empty lists
        ## these are the lists that will update everything
        ## explained in the later functions
        self.walls=[]
        self.floors=[]
        self.ends=[]
        self.weapons=[]

        self.wall_rects=[]
        self.floor_rects=[]
        self.end_rects=[]
        self.weapon_rects=[]

        ## there are no creatures in this map
        ## in later ones they will be added
        self.creatures=[]

        ##keys
        self.key=[]
        ##doors
        self.doors=[]
        ##others
        self.specials=[]

        ## These next functions are very tempermantal
        ## Dont mess with them unless the changes are approved
        self.height=len(self.layout)
        self.width=len(self.layout[0])

        max_y = self.height-1

        ## variable needed for screen flip
        self.z=0
        self.z=self.z+(32*self.height)-32
        for x in range(self.width):
            
            for y in range(self.height):
                char=self.layout[max_y-y][x]
                ## call the cheate char function
                ## this makes the characters appear
                self.create_char((x,y),char)

        ## past tempermental zone
        
        self.move_x=self.x
        self.move_y=self.y
        self.move_spec_x=0
        self.move_spec_y=0
        ## screen.size is in screen.py look for more info
        while 1:
            if self.move_x<screen.size[0]/2-32:
                self.move_screen(1)
            if self.move_x>screen.size[0]/2-32:
                self.move_screen(2)
            if self.move_y<screen.size[1]/2-32:
                self.move_screen(3)
            if self.move_y>screen.size[1]/2-32:
                self.move_screen(4)

            if self.move_x==screen.size[0]/2-32 and self.move_y==screen.size[1]/2-32:
                self.move_screen(5)
                self.x=screen.size[0]/2+4
                self.y=screen.size[1]/2+4
                self.pistol_x=self.pistol_x+self.move_spec_x
                self.pistol_y=self.pistol_y+self.move_spec_y
                self.rifle_x=self.rifle_x+self.move_spec_x
                self.rifle_y=self.rifle_y+self.move_spec_y
                self.machine_gun_x=self.machine_gun_x+self.move_spec_x
                self.machine_gun_y=self.machine_gun_y+self.move_spec_y
                self.flashlight_x=self.flashlight_x+self.move_spec_x
                self.flashlight_y=self.flashlight_y+self.move_spec_y
                self.flame_thrower_x=self.flame_thrower_x+self.move_spec_x
                self.flame_thrower_y=self.flame_thrower_y+self.move_spec_y
                break

        self.player=player.Player(self.x,self.y)
        self.pistol=weapons.Pistol(self.pistol_x,self.pistol_y)
        self.machine_gun=weapons.MachineGun(self.machine_gun_x,self.machine_gun_y)
        self.rifle=weapons.Rifle(self.rifle_x,self.rifle_y)
        self.flame_thrower=weapons.FlameThrower(self.flame_thrower_x,self.flame_thrower_y)
        self.flashlightx=flashlight.Flashlight(self.flashlight_x,self.flashlight_y)
        self.flashlight_click=0
        self.recharge_flashlight_click=10
        
        




    def create_char(self,point,char):
        ## Try to figure this part out ask questions if nessisary
        (x,y)=point
        x=x*32
        y=y*32
        y=y*(-1)
        y=y+self.z
        if char=='w':
            ## make a sprite
            self.wall=self.wall_picture
            ## add it to the list
            self.walls.append(self.wall)
            ## make the rect
            self.rect=self.wall.get_rect(topleft=(x,y))
            ## add it to the list
            self.wall_rects.append(self.rect)
        if char=='0':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='p':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.x=x
            self.y=y
        if char=='e':
            self.end=self.end_picture
            self.ends.append(self.end)
            self.rect=self.end.get_rect(topleft=(x,y))
            self.end_rects.append(self.rect)
        if char=='1':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.pistol_x=x
            self.pistol_y=y
        if char=='2':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.rifle_x=x
            self.rifle_y=y
        if char=='3':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.machine_gun_x=x
            self.machine_gun_y=y
        if char=='4':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flashlight_x=x
            self.flashlight_y=y
        if char=='5':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.flame_thrower_x=x
            self.flame_thrower_y=y
        if char=='9':
            self.floor=self.floor1_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)

        if char=='a':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Enemy_silver(x,y)
            self.creatures.append(baddy)
        if char=='c':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            baddy=baddies.Enemy_blue(x,y)
            self.creatures.append(baddy)
        if char=='r':
            self.floor=self.ruins
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='d':
            self.floor=self.dead
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
        if char=='h':
            self.floor=self.floor
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            self.heart_x=x
            self.heart_y=y
        if char=='t':
            self.floor=self.floor_picture
            self.floors.append(self.floor)
            self.rect=self.floor.get_rect(topleft=(x,y))
            self.floor_rects.append(self.rect)
            baddy=baddies.Tank(x,y)
            self.creatures.append(baddy)
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
            ##############################################################33
    def update(self):
        self.flashlight_click=self.flashlight_click-1
        x=0
        for item in self.creatures:
            if item.health<=0:
                if item.name=='silver':
                    self.heart=specials.Heart(item.rect[0],item.rect[1])
                    self.specials.append(self.heart)
                del self.creatures[x]
            else:
                item.move(self.wall_rects)
            x=x+1
        if self.pistol.rect.colliderect(self.player):
            self.pistol.pickup(self.player)
            self.slot_1=1
        if self.rifle.rect.colliderect(self.player):
            self.rifle.pickup(self.player)
            self.slot_2=2
        if self.machine_gun.rect.colliderect(self.player):
            self.machine_gun.pickup(self.player)
            self.slot_3=3
        if self.flame_thrower.rect.colliderect(self.player):
            self.flame_thrower.pickup(self.player)
            self.slot_4=4
        if self.flashlightx.rect.colliderect(self.player):
           self.flashlightx.pickup(self.player)
           self.slot_10=10
        x=0
        
        ## make the background the color of our choice
        screen.screen.fill(self.backgroud_color)
        ## define the number
        x=0
        ## call the list
        for item in self.floor_rects:
            ## blit item on the screen
            screen.screen.blit(self.floors[x],item)
            ## increase the number by one
            x=x+1

        x=0
        for item in self.wall_rects:
            screen.screen.blit(self.walls[x],item)
            x=x+1
        x=0
        for item in self.end_rects:
            screen.screen.blit(self.ends[x],item)
            x=x+1

        for item in self.creatures:
            item.update(self.player.bullets)

        

        self.player.update(self.wall_rects,self.creatures)

        self.pistol.update()
        self.rifle.update()
        self.machine_gun.update()
        self.flashlightx.update()
        self.flame_thrower.update()

        self.darkness.update(self.flashlightx,self.flashlight_on)
        
        
        self.menu.update(self.player,self.flashlightx,self.pistol,
                         self.rifle,self.machine_gun,self.flame_thrower,self.active_weapon,
                         self.message,self.instructions,self.tips)


    def player_moves(self,command,direction):
        ## self explanatory
        if command=='move':
            self.player.move(direction)
            if direction==1:
                self.player.bullets_player_move(1)
                self.pistol.move(1,self.player.speed)
                self.rifle.move(1,self.player.speed)
                self.machine_gun.move(1,self.player.speed)
                self.flame_thrower.move(1,self.player.speed)
                self.flashlightx.move(1,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,self.player.speed)
                for item in self.creatures:
                    item.player_move(1)
            if direction==2:
                self.player.bullets_player_move(2)
                self.pistol.move(2,self.player.speed)
                self.machine_gun.move(2,self.player.speed)
                self.rifle.move(2,self.player.speed)
                self.flashlightx.move(2,self.player.speed)
                self.flame_thrower.move(2,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.floor_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.end_rects:
                    item=item.move_ip(0,-self.player.speed)
                for item in self.creatures:
                    item.player_move(2)
            if direction==3:
                self.player.bullets_player_move(3)
                self.pistol.move(3,self.player.speed)
                self.machine_gun.move(3,self.player.speed)
                self.rifle.move(3,self.player.speed)
                self.flashlightx.move(3,self.player.speed)
                self.flame_thrower.move(3,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(-self.player.speed,0)
                for item in self.creatures:
                    item.player_move(3)
            if direction==4:
                self.player.bullets_player_move(4)
                self.pistol.move(4,self.player.speed)
                self.rifle.move(4,self.player.speed)
                self.machine_gun.move(4,self.player.speed)
                self.flashlightx.move(4,self.player.speed)
                self.flame_thrower.move(4,self.player.speed)
                for item in self.wall_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.floor_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.end_rects:
                    item=item.move_ip(self.player.speed,0)
                for item in self.creatures:
                    item.player_move(4)

            for item in self.wall_rects:
                if self.player.rect.colliderect(item):
                    self.reverse_move(direction)
            x=0
        if command=='attack':
            if self.active_weapon==10:
                self.flashlight_on_off()
            else:
                self.player.attack(direction,self.active_weapon)
        if command=='switch':
            pass

    def reverse_move(self,direction):
        if direction==1:
            self.player.bullets_reverse_move(1)
            self.pistol.move(2,self.player.speed)
            self.rifle.move(2,self.player.speed)
            self.machine_gun.move(2,self.player.speed)
            self.flame_thrower.move(2,self.player.speed)
            self.flashlightx.move(2,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,-self.player.speed)
            for item in self.creatures:
                item.player_move(2)
        if direction==2:
            self.player.bullets_reverse_move(2)
            self.pistol.move(1,self.player.speed)
            self.rifle.move(1,self.player.speed)
            self.flame_thrower.move(1,self.player.speed)
            self.machine_gun.move(1,self.player.speed)
            self.flashlightx.move(1,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.floor_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.end_rects:
                item=item.move_ip(0,self.player.speed)
            for item in self.creatures:
                item.player_move(1)
        if direction==3:
            self.player.bullets_reverse_move(3)
            self.pistol.move(4,self.player.speed)
            self.rifle.move(4,self.player.speed)
            self.machine_gun.move(4,self.player.speed)
            self.flashlightx.move(4,self.player.speed)
            self.flame_thrower.move(4,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(self.player.speed,0)
            for item in self.creatures:
                item.player_move(4)
        if direction==4:
            self.player.bullets_reverse_move(4)
            self.pistol.move(3,self.player.speed)
            self.rifle.move(3,self.player.speed)
            self.flame_thrower.move(3,self.player.speed)
            self.machine_gun.move(3,self.player.speed)
            self.flashlightx.move(3,self.player.speed)
            for item in self.wall_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.floor_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.end_rects:
                item=item.move_ip(-self.player.speed,0)
            for item in self.creatures:
                item.player_move(3)

    def flashlight_on_off(self):
        self.clicked=1
        if self.flashlight_click<0:
            if self.flashlight_on==0 and self.clicked==1:
                self.flashlight_on=1
                self.clicked=0
            if self.flashlight_on==1 and self.clicked==1:
                self.flashlight_on=0
                self.clicked=0
            self.flashlight_click=self.recharge_flashlight_click

    def move_screen(self,x):
        if x==1:
            self.move_x=self.move_x+1
            self.move_spec_x=self.move_spec_x+1
        if x==2:
            self.move_x=self.move_x-1
            self.move_spec_x=self.move_spec_x-1
        if x==3:
            self.move_y=self.move_y+1
            self.move_spec_y=self.move_spec_y+1
        if x==4:
            self.move_y=self.move_y-1
            self.move_spec_y=self.move_spec_y-1
        if x==5:
            self.move_spec_x=self.move_spec_x+36
            self.move_spec_y=self.move_spec_y+42
            for item in self.wall_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.floor_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.end_rects:
                item=item.move_ip(self.move_spec_x,self.move_spec_y)
            for item in self.creatures:
                item.move_screen(self.move_spec_x,self.move_spec_y)
