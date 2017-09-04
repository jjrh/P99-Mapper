import pygame
from pygame.locals import *
from mapping import *
import sys



G_RESOLUTION = None
G_SCREEN     = None
G_FILLSURF   = None
G_BACKSURF   = None
G_CLOCK      = None

INIT_RUN     = False


def INIT_PYGAME(RESOLUTION=(800,600)):
    global INIT_RUN
    if(not INIT_RUN):
        pygame.init()
        global G_RESOLUTION,G_SCREEN,G_FILLSURF,G_BACKSURF,G_CLOCK
        G_RESOLUTION = RESOLUTION

        G_SCREEN = pygame.display.set_mode(RESOLUTION)
        G_SCREEN.fill((255,255,255))

        G_FILLSURF = pygame.Surface(G_RESOLUTION)
        G_FILLSURF.fill((255,255,255))
        G_BACKSURF = pygame.Surface((10000,10000))
    
        G_CLOCK = pygame.time.Clock()
        pygame.display.update()

        INIT_RUN=True
    main_loop("")    

def main_loop(imap):
    mapp = []
    pPoints = []
    p2Points = []
    otherPoints = []    
    
    current_map = MAP('maps/gukbottom_1.txt')
    current_map.render(4,False)
    EXIT = False
    RATIO = 1
    MOVE_SPEED = 10
    zoom = False
    X=0
    Y=0
    mouse_pos = 0
    while not EXIT:
            G_CLOCK.tick(60)
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
                                    current_map.render(RATIO,zoom)
                            else:
                                    RATIO = 1
                    if event.type == MOUSEBUTTONDOWN and event.button == 5:
                            RATIO = RATIO + 1
                            current_map.render(RATIO,zoom)
                            
                    
                            
     
                            
                    G_SCREEN.blit(G_FILLSURF,(0,0))
     
                    G_SCREEN.blit(current_map.surface, (X,Y))
                         
                    pygame.display.flip()


    

# mapp = []
# pPoints = []
# p2Points = []
# otherPoints = []    
# fillSurf = pygame.Surface((800,600))
# fillSurf.fill((255,255,255))
# backSurf = pygame.Surface((10000,10000))

# southro = MAP('maps/mistmoore_1.txt')
# southro.render(4,False)
# EXIT = False
# RATIO = 1
# MOVE_SPEED = 10
# zoom = False


# screen.blit(fillSurf,(0,0))

# pygame.display.flip()
# clock = pygame.time.Clock()

# X=0
# Y=0

# mouse_pos = 0
# while not EXIT:
#         clock.tick(60)
#         for event in pygame.event.get():
#                 #print event
#                 if event.type == QUIT:
#                         sys.exit()
#                 if event.type == KEYDOWN:
#                         if event.key == K_ESCAPE:
#                                 #EXIT=True
                                
#                                 sys.exit()
                                
#                         elif event.key == K_UP:
#                                 Y = Y-MOVE_SPEED*RATIO
#                                 print Y
#                         elif event.key == K_DOWN:
#                                 Y = Y+MOVE_SPEED*RATIO
#                                 print Y
#                         elif event.key == K_LEFT:
#                                 X = X+MOVE_SPEED*RATIO
#                                 print X
#                         elif event.key == K_RIGHT:
#                                 X = X-MOVE_SPEED*RATIO
#                                 print X
#                         elif event.key == K_q:
#                                 RATIO = RATIO + 1
                                
#                         elif event.key == K_a:
#                                 if RATIO > 0:
#                                         RATIO = RATIO - 1
#                         elif event.key == K_z:
#                                 if zoom == False:
#                                         zoom = True
#                                 else:
#                                         zoom = False
#                         else:
#                                 pass
#                 if event.type == MOUSEBUTTONDOWN:
#                         print event.button
#                         print pygame.mouse.get_pressed()
                        
#                         mouse_pos = pygame.mouse.get_rel()

#                 if event.type == MOUSEBUTTONUP:
#                         mouse_pos = pygame.mouse.get_rel()
#                         Y = Y + mouse_pos[1]
#                         X = X + mouse_pos[0]
#                 if event.type == MOUSEBUTTONDOWN and event.button == 4:
#                         print RATIO
#                         if RATIO > 1:
#                                 RATIO = RATIO - 1
#                                 southro.render(RATIO,zoom)
#                         else:
#                                 RATIO = 1
#                 if event.type == MOUSEBUTTONDOWN and event.button == 5:
#                         RATIO = RATIO + 1
#                         southro.render(RATIO,zoom)
                        
                
                        

                        
#                 screen.blit(fillSurf,(0,0))

#                 screen.blit(southro.surface, (X,Y))
                     
#                 pygame.display.flip()

