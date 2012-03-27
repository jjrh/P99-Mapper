import sys

import pygame
from pygame.locals import *

        
                

class MAP:
        def __init__(self, filename):
                self.mapFull     = []	# The entire map raw.
                self.L_Points    = []	# L type (line points)
                self.P_Points    = []	# P type points
                self.Grid_Points = []	# grid lines, special in that they create a grid when plotted.
                
                self.filename = filename

                self.surface = pygame.Surface((1,1))	# set to 1,1 as default. More there to say this is a surface
                
                self.LargestPosX = 0
                self.LargestPosY = 0
                self.LargestPosZ = 0
                
                self.LargestNegX = 0
                self.LargestNegY = 0
                self.LargestNegZ = 0

                self.color = (255,0,0)

                self.load()
        def load(self):
	        """
	        big function, basically it goes:
	        load file.
	        for loop of the lines in the file, for each line we remove the \n, \r tags.
	        we then find out what type it is (L or P)
	        if it's L, we find the largest X and Y, and the smallest X and Y.
	        Create a dictionary of the points then add it to it's respective list.
	        finally we set the class global largestX, largestY, lowestX, lowestY variables. (saves typing self. by doing this once)
        
        	"""
                f = open(self.filename)
                
                print "trying to open:", self.filename

                fail = 0
                otherFlag = False # when we encounter something unexpected
                LargestX = 0	# these two are the longest lines, we use this to create a surface that is exactly the right size.
                LargestY = 0
                LargestZ = 0	# probably don't actually need this, but might as well calculate it anyways.

                LargestNegX = 0
                LargestNegY = 0
                LargestNegZ = 0

                gridPoints = []
                for line in f.readlines():

                        # get rid of the \n and \r stuff that is in the text file. 
                        processedLine = line.rstrip('\n')
                        processedLine = processedLine.rstrip('\r')
                        
                        LineType = processedLine.split(',')
                        try:
                                LineType = processedLine[0] # keep track of the type.
                                processedLine = processedLine[1:].split(',') # there isn't a comma between the type and the first value.
                        except:
                                print processedLine
                        # we found a line type. 
                        if('L' in LineType):
 #                               print processedLine
#                                xxx = raw_input("break")
                                
                                try:
                                        fX1 = float(processedLine[0])
                                        fY1 = float(processedLine[1])
                                        fZ1 = float(processedLine[2])
                                        fX2 = float(processedLine[3])
                                        fY2 = float(processedLine[4])
                                        fZ2 = float(processedLine[5])
                                except:
                                        print "error, probably a issue with conversion to float", processedLine

                                # These checks have to do with creating a perfect sized surface.
                                # we need to find the upper X,Y bounds for when we create the surface. 
                                if fX1 > LargestX:
                                        LargestX = fX1
                                if fX2 > LargestX:
                                        LargestX = fX2

                                if fY1 > LargestY:
                                        LargestY = fY2
                                if fY2 > LargestY:
                                        LargestY = fY2

                                if fZ1 > LargestZ:
                                        LargestZ = fZ1
                                if fZ2 > LargestZ:
                                        LargestZ = fZ2

                                # I should explain why we are doing this:
                                #	When we are plotting, we need to plot positive numbers.
                                #	Thus, we need to find what the largest negative value is, then when we draw the map,
                                #	we add this to what ever we are drawing. 
                                if fX1 < 0 and fX1*-1 > LargestNegX:
                                        LargestNegX = fX1*-1
                                if fX2 < 0 and fX2*-1 > LargestNegX:
                                        LargestNegX = fX2*-1

                                if fY1 < 0 and fY1*-1 > LargestNegY:
                                        LargestNegY = fY1*-1
                                if fY2 < 0 and fY2*-1 > LargestNegY:
                                        LargestNegY = fY1*-1

                                if fZ1 < 0 and fZ1*-1 > LargestNegZ:
                                        LargestNegZ = fZ1*-1
                                if fZ2 < 0 and fZ2*-1 > LargestNegZ:
                                        LargestNegZ = fZ2*-1
                                

                                vectorLine = {'X1': fX1, 'Y1': fY1, 'Z1': fZ1 , 'X2': fX2, 'Y2': fY2, 'Z2': fZ2}

                                # For now we just assume gridlines are after the first P type instead of calculating the slope.
                                # if otherFlag is ture, it means we are done the map data and line points there after are grid ones.
                                
                                if otherFlag == True:
                                        gridPoints.append(vectorLine)
                                else:                                       
                                        self.L_Points.append(vectorLine)                        


                        if ('P' in LineType):
                                otherFlag = True 
                                self.P_Points.append(processedLine[1:]) # no functionality for these types of points yet.

                        self.LargestPosX = LargestX
                        self.LargestPosY = LargestY
                        self.LargestPosZ = LargestZ

                        self.LargestNegX = LargestNegX
                        self.LargestNegY = LargestNegY
                        self.LargestNegZ = LargestNegZ
                f.close()

                
        def findGrid(self, x1,y1,x2,y2):
                # slope = y2-y1 / x2-x1
                # If slope is undefined (x2-x1 == 0) we have a vertical line. 
                # if slope is is a whole number then it's a horizontal line. 
                if(x2-x1) == 0:
                      # print "vertical line"
                        return True
                elif ((y2-y1)/(x2-x1))%1 == 0:
                        # whole number
                       #print "horizontal line"
                        return True
                else:
                        return False


        def render(self, ratio=1, smaller=True):
                print "largest pos: (", self.LargestPosX , "," , self.LargestPosY, ")"
                print "largets neg: (", self.LargestNegX, ",", self.LargestNegY, ")"
                if ratio == 0:
                        print "** error in MAP render(), ratio of 0 would result in dividing by 0. **"
                        return False
                else:
                        x = (self.LargestPosX+self.LargestNegX)/ratio
                        y = (self.LargestPosY+self.LargestNegY)/ratio
                        self.surface = pygame.Surface((10000,10000))
                        self.surface.fill((0,0,0))
                        #self.LargestNegY = self.LargestNegX
                        
                        # draw the lines, we add the values their respective largest negative cords, then divide by the ratio.
                        error = 0
                        length = len(self.L_Points)
                        for vectorLine in self.L_Points:

                                x1 = vectorLine['X1']
                                y1 = vectorLine['Y1']
                                z1 = vectorLine['Z1']
                                
                                x2 = vectorLine['X2']
                                y2 = vectorLine['Y2']
                                z2 = vectorLine['Z2']
                                if(smaller):
                                        x1 = (x1+self.LargestNegX)/ratio
                                        x2 = (x2+self.LargestNegX)/ratio
                                
                                        
                                        y1 = (y1+self.LargestNegY)/ratio
                                        y2 = (y2+self.LargestNegY)/ratio
                                        
                                        z1 = (z1+self.LargestNegZ)/ratio
                                        z2 = (z2+self.LargestNegZ)/ratio
                                else:
                                        x1 = (x1+self.LargestNegX)*ratio
                                        x2 = (x2+self.LargestNegX)*ratio
                                
                                        
                                        y1 = (y1+self.LargestNegY)*ratio
                                        y2 = (y2+self.LargestNegY)*ratio
                                        
                                        z1 = (z1+self.LargestNegZ)*ratio
                                        z2 = (z2+self.LargestNegZ)*ratio
                                        
                                if x1 == x2 and y1 == y2:
                                        error+=1
                                    
                                pygame.draw.line(self.surface,self.color,(x1,y1),(x2,y2))

                                xz1 = x1 + z1
                                xz2 = x2 + z2
                                yz1 = y1 + z1
                                yz2 = y2 + z2
                                
                                #pygame.draw.line(self.surface,(0,255,0),(xz1,yz1),(xz2,yz2))
                                #pygame.draw.line(self.surface,(0,0,255),(xz1,yz1),(x2,y2))
                                #pygame.draw.line(self.surface,(255,0,255),(xz2,yz2),(x1,y1))
                                
                                
                        
                        print "equalvalues:", error, "vs point list length", length
                        return True
                
                
                
        
                

                

#################################################################################################################################################################



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


        
        




