import sys
import os
import threading
from Queue import Queue
import pygame
from pygame.locals import *
from mapping import *

pygame.init()

screen = pygame.display.set_mode((800,600))

screen.fill((255,255,255))
pygame.display.update()

mapp = []
pPoints = []
p2Points = []
otherPoints = []    
fillSurf = pygame.Surface((800,600))
fillSurf.fill((255,255,255))
backSurf = pygame.Surface((10000,10000))


INPT ="DEFAULT"
class IOFace(threading.Thread):
        def run(self):
                print "ioface run!"
                global INPT
                try:
                        INPT = input(">")
                        print INPT
                except:
                        print "bad!"
                
                



MAP_LIST = []
def loadMaps(location):
        try:
                for f in os.listdir(location):
                        
                        m = MAP(location+'/'+f)
                        MAP_LIST.append(m)
        except:
                print "DOH!"


loadMaps('maps')

southro = MAP('maps/mistmoore_1.txt')
southro.render(4,False)
EXIT = False
RATIO = 1
MOVE_SPEED = 10
zoom = False


screen.blit(fillSurf,(0,0))

pygame.display.flip()
clock = pygame.time.Clock()

X=0
Y=0




mouse_pos = 0


class MAIN(threading.Thread):
        def run(self):
                global X,Y,RATIO,MOVE_SPEED,zoom,clock

                while not EXIT:
                        clock.tick(60)

                        for event in pygame.event.get():
                                #print event
                                if event.type == QUIT:
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                #EXIT=True

                                                sys.exit()

                                        elif event.key == K_UP:
                                                Y = Y-MOVE_SPEED*RATIO
                                                print Y
                                        elif event.key == K_DOWN:
                                                Y = Y+MOVE_SPEED*RATIO
                                                print Y
                                        elif event.key == K_LEFT:
                                                X = X+MOVE_SPEED*RATIO
                                                print X
                                        elif event.key == K_RIGHT:
                                                X = X-MOVE_SPEED*RATIO
                                                print X
                                        elif event.key == K_q:
                                                RATIO = RATIO + 1

                                        elif event.key == K_a:
                                                if RATIO > 0:
                                                        RATIO = RATIO - 1
                                        elif event.key == K_z:
                                                if zoom == False:
                                                        zoom = True
                                                else:
                                                        zoom = False
                                        else:
                                                pass
                                if event.type == MOUSEBUTTONDOWN:
                                        print event.button
                                        print pygame.mouse.get_pressed()

                                        mouse_pos = pygame.mouse.get_rel()

                                if event.type == MOUSEBUTTONUP:
                                        mouse_pos = pygame.mouse.get_rel()
                                        Y = Y + mouse_pos[1]
                                        X = X + mouse_pos[0]
                                if event.type == MOUSEBUTTONDOWN and event.button == 4:
                                        print RATIO
                                        if RATIO > 1:
                                                RATIO = RATIO - 1
                                                southro.render(RATIO,zoom)
                                        else:
                                                RATIO = 1
                                if event.type == MOUSEBUTTONDOWN and event.button == 5:
                                        RATIO = RATIO + 1
                                        southro.render(RATIO,zoom)




                                
                                screen.blit(fillSurf,(0,0))

                                screen.blit(southro.surface, (X,Y))

                                pygame.display.flip()
                               



q = Queue(2)

INP = IOFace()
M = MAIN()
INP.start()
M.start()
INP.join()
M.join(0.01)




