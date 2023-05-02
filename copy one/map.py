import pygame
import shapes
import random
import units

class Map:

    def __init__( self, width, height ):
        self.mWidth = int(width)
        self.mHeight = int(height)
        self.Csize = int()

        return


    # draws the current state of the system
    def draw( self, surface, cellgrid ):
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
                    pygame.draw.circle(surface, (0,0,0),(cell.getX()+(cell.getSize()//2),cell.getY()+(cell.getSize()//2)),cell.getSize()+(cell.getSize()-(cell.getSize()//3))//2,5)



        return
