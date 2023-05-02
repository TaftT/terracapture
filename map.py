import pygame
import shapes
import random
import units

class Map:

    def __init__( self, width, height,surface ):
        self.mWidth = int(width)
        self.mHeight = int(height)
        self.Csize = int()
        self.surface=surface

        return

    def texttoscreen(self,surface,msg,color,x,y, size=75):
        font = pygame.font.SysFont(None, size)
        screentext = font.render(msg,True,color)
        surface.blit(screentext,[x,y])


    # draws the current state of the system
    def draw( self, surface, cellgrid, pl, msg="", msg2=""):
        Darkgrass=(103,126,82)


        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, Darkgrass, rect, 0 )

        for row in cellgrid:
            for cell in row:
                cell.drawcell(surface)
        for row in cellgrid:
            for cell in row:
                if cell.getFort()==2:
                    pygame.draw.circle(surface, (0,0,0),(cell.getX()+(cell.getSize()//2),cell.getY()+(cell.getSize()//2)),cell.getSize()+(cell.getSize()-(cell.getSize()))//2,5)

        pygame.draw.rect(surface, (pl.getColor()[0]),(25,self.mHeight-95,200,75 ))
        pygame.draw.rect(surface, ( 211, 211, 211),(250,self.mHeight-95,75,75 ))
        pygame.draw.rect(surface, ( 255, 255, 255),(350,self.mHeight-95,500,75 ))
        self.texttoscreen(surface,str(pl.getName()),(255,255,255),25+5,self.mHeight-(95-12))
        self.texttoscreen(surface,str(pl.getPoints()),(0,0,0),270,self.mHeight-(95-12))
        self.texttoscreen(surface,msg,(255,0,0),360,self.mHeight-(95-12),25)
        self.texttoscreen(surface,msg2,(255,0,0),360,self.mHeight-(95-12),25)

        return
