import pygame


import pygame
from pygame.locals import *

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
        
                
                

f = open('southro.txt')
fail=0


otherFlag = False
for line in f.readlines():
        l = line.rstrip('\n')
        l = l.rstrip('\r')   
        pt = l[1:].split(',')
        l = l.split(',')
        if( 'L' in l[0]):
                if otherFlag == False:
                        mapp.append(pt)
                else:
                        p2Points.append(pt)
        elif('P' in l[0]):
                otherFlag = True
                pPoints.append(pt)
        else:
                otherFlag = True
                otherPoints.append(l)
                print l[0]
                
#        print pt
        
#        print type(pt[0]),pt[1]
largest_point = 0
for line in mapp:
        for p in line:
                try:
                        if float(p) < 0 and float(p)*-1 > largest_point:
                                largest_point = float(p)*-1
                except:
                        pass
                            
def plotCoreMap(ratio):
        backSurf.fill((255,255,255))
        fail = 0
        for pt in mapp:
                try:
                        
                        x1 = float(pt[0])
                        y1 = float(pt[1])
                        x2 = float(pt[3])
                        y2 = float(pt[4])
                        x1=x1+largest_point
                        y1=y1+largest_point
                        x2 = x2+largest_point
                        y2 = y2+largest_point
                        x1 = x1/ratio
                        x2 = x2/ratio
                        y1 = y1/ratio
                        y2 = y2/ratio
                 
                
                 #       print x1,y1,x2,y2
                        pygame.draw.line(backSurf,(255,0,0),(x1,y1),(x2,y2)) 

                except:
                        fail += 1       

print "failed:", fail
print "largest point:",largest_point

X = 0
Y = 0
EXIT = False
RATIO = 0
MOVE_SPEED = 10


plotCoreMap(RATIO)
screen.blit(fillSurf,(0,0))
screen.blit(backSurf,(X,Y))
pygame.display.flip()
clock = pygame.time.Clock()




while not EXIT:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                EXIT=True
                                
                        elif event.key == K_UP:
                                Y = Y-MOVE_SPEED*RATIO
                        elif event.key == K_DOWN:
                                Y = Y+MOVE_SPEED*RATIO
                        elif event.key == K_LEFT:
                                X = X+MOVE_SPEED*RATIO
                        elif event.key == K_RIGHT:
                                X = X-MOVE_SPEED*RATIO
                        elif event.key == K_q:
                                RATIO = RATIO + 1
                                plotCoreMap(RATIO)
                        elif event.key == K_a:
                                if RATIO > 0:
                                        RATIO = RATIO - 1
                                plotCoreMap(RATIO)
                        else:
                                pass
        
                        screen.blit(fillSurf,(0,0))
                        screen.blit(backSurf,(X,Y))
                        pygame.display.flip()


        
        




