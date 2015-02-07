import os,sys,random,pygame
from pygame.locals import *
import cPickle as pickle

options=file('data/options','wb')
pickle.dump(str(0),options)
pickle.dump(str(1024),options)
pickle.dump(str(0),options)
