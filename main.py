import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import map
import units
import players

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Terra Capture"
# frames per second
DESIRED_RATE  = 15

Csize = 30

cellsAccross = 35 #45

cellsDown = 15 #25

margin = 5

# pixels width
WINDOW_WIDTH  = (cellsAccross*Csize)+((cellsAccross-1)*margin)
# pixels high
WINDOW_HEIGHT = (cellsDown*Csize)+((cellsDown-1)*margin)+150



class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate, Csize, cellsAccross, cellsDown, players ):

        game.Game.__init__( self, title, width, height, frame_rate,Csize, players  )

        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = map.Map( width, height,self.screen)
        self.createcells(cellsAccross, cellsDown)

        return

    def createcells(self, cellsAccross, cellsDown):
        new=[]
        for x in range(int(cellsAccross)+1):
            row=[]
            for y in range(cellsDown+1):
                row.append(units.Units(x*(self.Csize+5),y*(self.Csize+5),self.Csize))
            new.append(row)

        self.setcellgrid(new)




    def paint( self, surface, pl,msg, msg2 ):
        # Draw the current state of the game instance
        self.mGame.draw( surface, self.getcellgrid(), pl, msg,msg2 )
        return

def createplayers(plnum):
    new=[]

    for i in range(plnum):
        pl= players.Players(i+1,"Player"+str(i+1))
        new.append(pl)
    return new


def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE, Csize, cellsAccross, cellsDown, createplayers(2))
    game.main_loop( )


if __name__ == "__main__":
    main( )
