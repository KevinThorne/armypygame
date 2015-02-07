import os,sys,random,pygame
from pygame.locals import *
import cPickle as pickle

import screen,layout,player,baddies

def load_image(name,colorkey):
    fullname = os.path.join('data/pictures',name)
    i=pygame.image.load(fullname)
    if colorkey==0:
        colorkey=None
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

class MainMenu:
    def __init__(self):
        self.screen=screen.screen

        self.deaths=0
        self.wins=0

        self.mainmenuimage=load_image('mmenu.png',0)
        self.mainmenurect=self.mainmenuimage.get_rect(topleft=(0,0))

        self.optionsimage=load_image('options.png',0)
        self.optionsrect=self.optionsimage.get_rect(topleft=(0,0))

        self.guy1image=load_image('player1_down.png',-1)
        self.guy1rect=self.guy1image.get_rect(topleft=(147,362))
        self.guy2image=load_image('enemy1_down.png',-1)
        self.guy2rect=self.guy2image.get_rect(topleft=(662,359))
        self.speed=4
        self.direction=random.randint(1,4)
        self.direction1=random.randint(1,4)

        self.deathimage=load_image('die.png',-1)
        self.deathrect=self.deathimage.get_rect(topleft=(0,0))

        self.mouse_pos = pygame.mouse.get_pos()

        self.winsound=load_sound('win.wav')
        self.diesound=load_sound('die.wav')
        self.titlemusic=load_sound('title.wav')
        self.play=load_sound('play.wav')
        x=file('data/options','rb')
        y=pickle.load(x)
        z=pickle.load(x)
        self.sounds=int(pickle.load(x))

        self.restarted=0
        self.startinglevel=1
        self.workinglevel=2

        self.shoot1=load_sound('hgun.wav')
        self.shoot2=load_sound('hgun.wav')
        self.shoot3=load_sound('mgun.wav')
        self.shoot4=load_sound('rl1.wav')

    def game(self):
        on=1
        while on:
            playing=1
            x=self.mainmenu()
            if x==1: #new
                self.win=0
                self.deaths=0
                level=self.startinglevel
                while playing==1:
                    nextlevel=self.playlevel(level)
                    if self.win==(-1):
                        playing=0
                    if nextlevel==level+1:
                        level+=1
            if x==2: #prefs
                y=self.options()
                if y==0:
                    os.startfile('ARMY.py')
                    on=0
            if x==3:#quit
                on=0
                raise SystemExit()
    def mainmenu(self):
        option=1
        pygame.mixer.stop()
        if self.sounds==0:
            self.titlemusic.play()
        while 1:
            pygame.time.Clock().tick(60)
            self.screen.fill((0,0,0))
            self.screen.blit(self.mainmenuimage,self.mainmenurect)
            # little dudes running around
            self.screen.blit(self.guy1image,self.guy1rect)
            self.screen.blit(self.guy2image,self.guy2rect)
            self.new_dir=random.randint(1,100)
            if self.new_dir<10:
                self.direction=random.randint(1,4)
            if self.direction==1:
                self.guy2rect=self.guy2rect.move(0,self.speed)
            if self.direction==2:
                self.guy2rect=self.guy2rect.move(0,-self.speed)
            if self.direction==3:
                self.guy2rect=self.guy2rect.move(-self.speed,0)
            if self.direction==4:
                self.guy2rect=self.guy2rect.move(self.speed,0)
            if self.new_dir<10:
                self.direction1=random.randint(1,4)
            if self.direction1==1:
                self.guy1rect=self.guy1rect.move(0,self.speed)
            if self.direction1==2:
                self.guy1rect=self.guy1rect.move(0,-self.speed)
            if self.direction1==3:
                self.guy1rect=self.guy1rect.move(-self.speed,0)
            if self.direction1==4:
                self.guy1rect=self.guy1rect.move(self.speed,0)
            # other stuff
            if option==1:
                self.screen.blit((pygame.font.Font(None, 60).render('New Game',1,(255,0,0))),((300,350)))
                self.screen.blit((pygame.font.Font(None, 60).render('Options',1,(0,0,0))),   ((300,450)))
                self.screen.blit((pygame.font.Font(None, 60).render('Exit',1,(0,0,0))),      ((300,550)))
            if option==2:
                self.screen.blit((pygame.font.Font(None, 60).render('New Game',1,(0,0,0))),((300,350)))
                self.screen.blit((pygame.font.Font(None, 60).render('Options',1,(255,0,0))),   ((300,450)))
                self.screen.blit((pygame.font.Font(None, 60).render('Exit',1,(0,0,0))),      ((300,550)))
            if option==3:
                self.screen.blit((pygame.font.Font(None, 60).render('New Game',1,(0,0,0))),((300,350)))
                self.screen.blit((pygame.font.Font(None, 60).render('Options',1,(0,0,0))),   ((300,450)))
                self.screen.blit((pygame.font.Font(None, 60).render('Exit',1,(255,0,0))),      ((300,550)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==QUIT:
                    raise SystemExit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        raise SystemExit()
                    if event.key==K_UP:
                        option-=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_DOWN:
                        option+=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_RETURN:
                        if option==1:
                            return 1
                        if option==2:
                            return 2
                        if option==3:
                            return 3
    def options(self):
        option=1
        loadfile=file('data/options','rb')
        fullscreen=int(pickle.load(loadfile))
        screenres1=int(pickle.load(loadfile))
        sound=int(pickle.load(loadfile))
        choice=0
        while 1:
            pygame.time.Clock().tick(60)
            self.screen.fill((0,0,0))
            self.screen.blit(self.optionsimage,self.optionsrect)
            self.screen.blit((pygame.font.Font(None, 60).render('Fullscreen = ',1,(0,0,0))),((300,350)))
            self.screen.blit((pygame.font.Font(None, 60).render('Sound: ',1,(0,0,0))),   ((300,450)))
            
            if option==1:
                if fullscreen==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(255,0,0))),((580,350)))
                if fullscreen==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(255,0,0))),((580,350)))

                if sound==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(0,0,0))),   ((450,450)))
                if sound==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(0,0,0))),   ((450,450)))
                    
                self.screen.blit((pygame.font.Font(None, 60).render('Ok',1,(0,0,0))),   ((300,550)))
                self.screen.blit((pygame.font.Font(None, 60).render('Cancel',1,(0,0,0))),   ((450,550)))

            if option==2:
                if fullscreen==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(0,0,0))),((580,350)))
                if fullscreen==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(0,0,0))),((580,350)))

                if sound==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(255,0,0))),   ((450,450)))
                if sound==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(255,0,0))),   ((450,450)))
                    
                self.screen.blit((pygame.font.Font(None, 60).render('Ok',1,(0,0,0))),   ((300,550)))
                self.screen.blit((pygame.font.Font(None, 60).render('Cancel',1,(0,0,0))),   ((450,550)))

            if option==3:
                if fullscreen==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(0,0,0))),((580,350)))
                if fullscreen==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(0,0,0))),((580,350)))

                if sound==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('on',1,(0,0,0))),   ((450,450)))
                if sound==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('off',1,(0,0,0))),   ((450,450)))

                if choice==0:
                    self.screen.blit((pygame.font.Font(None, 60).render('Ok',1,(255,0,0))),   ((300,550)))
                    self.screen.blit((pygame.font.Font(None, 60).render('Cancel',1,(0,0,0))),      ((450,550)))
                if choice==1:
                    self.screen.blit((pygame.font.Font(None, 60).render('Ok',1,(0,0,0))),   ((300,550)))
                    self.screen.blit((pygame.font.Font(None, 60).render('Cancel',1,(255,0,0))),      ((450,550)))

            

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==QUIT:
                    raise SystemExit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        raise SystemExit()
                    if event.key==K_UP:
                        option-=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_DOWN:
                        option+=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_RIGHT:
                        if option==1:
                            if fullscreen==1:
                                fullscreen=0
                            elif fullscreen==0:
                                fullscreen=1
                        if option==2:
                            if sound==0:
                                sound=1
                            elif sound==1:
                                sound=0
                        if option==3:
                            if choice==0:
                                choice=1
                            elif choice==1:
                                choice=0
                    if event.key==K_LEFT:
                        if option==1:
                            if fullscreen==1:
                                fullscreen=0
                            elif fullscreen==0:
                                fullscreen=1
                        if option==2:
                            if sound==0:
                                sound=1
                            elif sound==1:
                                sound=0
                        if option==3:
                            if choice==0:
                                choice=1
                            elif choice==1:
                                choice=0
                    if event.key==K_RETURN:
                        if option==3:
                            if choice==0:
                                loadfile=file('data/options','wb')
                                pickle.dump(str(fullscreen),loadfile)
                                pickle.dump(str(screenres1),loadfile)
                                pickle.dump(str(sound),loadfile)
                                return 0
                            if choice==1:
                                return 1
                    if event.key==K_g:
                        self.graphics()
    def graphics(self):
        self.imagea=0
        self.imageb=0
        cr=1
        ap=2
        self.player=player.Player(cr,ap)
        self.baddies=baddies.Enemy_silver(cr,ap)
        self.image1=load_image('player_down.png',-1)
        self.image2=load_image('enemy_down.png',-1)
        self.image3=load_image('enemyb_down.png',-1)
        option=1
        pygame.mixer.stop()
        while 1:
            pygame.time.Clock().tick(3)
            self.screen.fill((0,0,0))
            self.screen.blit(self.optionsimage,self.optionsrect)
            self.screen.blit((pygame.font.Font(None, 60).render('Player image =',1,(0,0,0))),((300,350)))
            self.screen.blit((pygame.font.Font(None, 60).render('Baddies image = ',1,(0,0,0))),   ((300,450)))

            if option==1:
                self.screen.blit((pygame.font.Font(None, 60).render('Player image =',1,(255,0,0))),((300,350)))
                self.screen.blit((pygame.font.Font(None, 60).render('Baddies image = ',1,(0,0,0))),   ((300,450)))
                if self.player.image1==1:
                    self.imageb=1
                    self.screen.blit(self.image1,(700,350))
                elif self.player.image1==2:
                    self.imageb=2
                    self.screen.blit(self.image2,(700,350))
            if option==2:
                self.screen.blit((pygame.font.Font(None, 60).render('Player image =',1,(0,0,0))),((300,350)))
                self.screen.blit((pygame.font.Font(None, 60).render('Baddies image = ',1,(255,0,0))),   ((300,450)))
                if self.baddies.image1==1:
                    self.imagea=1
                    self.screen.blit(self.image2,(700,450))
                elif self.baddies.image1==2:
                    self.imagea=2
                    self.screen.blit(self.image2,(700,450))

            if self.imageb==1:
                self.screen.blit(self.image1,(700,350))
            elif self.imageb==2:
                self.screen.blit(self.image2,(700,350))

            if self.imagea==1:
                self.screen.blit(self.image2,(700,450))
            elif self.imagea==2:
                self.screen.blit(self.image3,(700,450))

            pygame.display.flip()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==QUIT:
                    raise SystemExit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        raise SystemExit()
                    if event.key==K_UP:
                        option-=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_DOWN:
                        option+=1
                        if option==4:
                            option=1
                        if option==0:
                            option=3
                    if event.key==K_RIGHT:
                        if option==1:
                            if self.imageb==2:
                                self.imageb=1
                            elif self.imageb==2:
                                self.imageb=1
                        if option==2:
                            if self.imagea==1:
                                self.imagea=2
                            elif self.imagea==2:
                                self.imagea=1
                    if event.key==K_LEFT:
                        if option==1:
                            if self.imageb==2:
                                self.imageb=1
                            elif self.imageb==1:
                                self.imageb=2
                        if option==2:
                            if self.imagea==2:
                                self.imagea=1
                            elif self.imagea==2:
                                self.imagea=1
    def playlevel(self,level):
        if self.sounds==0:
            self.titlemusic.stop()
            self.play.play()
        level_1=layout.Layout_1()
        level_2=layout.Layout_2()
        level_3=layout.Layout_3()
        level_4=layout.Layout_3()
        level_5=layout.Layout_3()
        level_6=layout.Layout_3()

        level=level_1
        level_count=1
        level_counter=0
        
        slot_number_1=None
        slot_number_2=None
        slot_number_3=None

        while 1:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                ## check event type
                if event.type==QUIT:
                ## quit the game
                    raise SystemExit()
                if event.type==KEYDOWN:
                ## if key is x do this
                    if event.key==K_ESCAPE:
                        raise SystemExit()
                    if event.key==K_q:
                        level.active_weapon=level.slot_1
                    if event.key==K_w:
                        level.active_weapon=level.slot_2
                    if event.key==K_e:
                        level.active_weapon=level.slot_3
                    if event.key==K_r:
                        level.active_weapon=level.slot_4
                    if event.key==K_c:
                        pass
                    if event.key==K_s:
                        pass
                    if event.key==K_d:
                        pass
                    if event.key==K_f:
                        pass
                    if event.key==K_x:
                        pass
                    if event.key==K_a:
                        level.active_weapon=level.slot_10
                    if event.key==K_1:
                        level_count=level_count+1
                        level_counter=1
                    if event.key==K_END:
                        self.game()
                    if event.key==K_PAUSE:
                        self.pausemenu(layout)

            if pygame.key.get_pressed()[K_UP]:
                level.player_moves('move',1)
                direction=1

            if pygame.key.get_pressed()[K_DOWN]:
                level.player_moves('move',2)
                direction=2

            if pygame.key.get_pressed()[K_RIGHT]:
                level.player_moves('move',3)
                direction=3

            if pygame.key.get_pressed()[K_LEFT]:
                level.player_moves('move',4)
                direction=4
                

            if pygame.key.get_pressed()[K_z]:
                level.player_moves('attack',direction)

            level.update()
            for item in level.end_rects:
                if level.player.rect.colliderect(item):
                    level_count=level_count+1
                    level_counter=1
                    if self.sounds==0:
                        self.winsound.play()

            if level_counter==1:
                if level_count==2:
                    level=level_2
                if level_count==3:
                    level=level_3
                if level_count==4:
                    level=level_4
                if level_count==5:
                    level=level_5
                if level_count==6:
                    level=level_6
                if level_count==7:
                    self.game()
                level_counter=0

            ## refresh the screen
            pygame.display.flip()

            if level.player.health<1:
                if self.sounds==0:
                    self.diesound.play()
                self.screen.blit(self.deathimage,self.deathrect)
                pygame.display.flip()
                pygame.time.Clock().tick(3)
                pygame.time.Clock().tick(3)
                pygame.time.Clock().tick(3)
                pygame.time.Clock().tick(3)
                pygame.time.Clock().tick(3)
                self.game()
                
