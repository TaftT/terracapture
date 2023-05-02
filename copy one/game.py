#
# You should not need to edit this file.
#
import pygame
import pygame.locals
margin=5
class Game:
    def __init__( self, name, width, height, frames_per_second, Csize, players ):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True
        self.Csize = Csize
        self.cellgrid=[]
        self.players=players

        self.screen = pygame.display.set_mode(
                # set the size
                ( width, height ),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption( name )

        # set time tracking
        self.clock = pygame.time.Clock( )
        self.this_frame_time = pygame.time.get_ticks( ) / 1000.
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_time( self ):
        return self.this_frame_time

    def get_delta_time( self ):
        return self.delta_time

    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        raise NotImplementedError( )
        return

    def getcellgrid(self):
        return self.cellgrid

    def setcellgrid(self,cellgrid):
        self.cellgrid=cellgrid

    def paint(self, surface):
        raise NotImplementedError( )
        return

    def turns(self):
        pass



    def main_loop( self ):
        keys = set( )
        buttons = set( )
        mouse_position = ( 1, 1 )
        self.last_frame_time = pygame.time.get_ticks() / 1000.
        turns=0

        while True:
            grid = self.getcellgrid()
            turns+=1

            for player in self.players:
                print(player.getName())
                if turns==1:
                    player.setPoints(1)
                else:
                    if player.checkcastle(grid):
                        player.setMaxPoints()
                    else:
                        player.setPoints(0)


                player.checkforts(grid,self.Csize,5)


                while  player.checkpoints():
                    self.clock.tick( self.frames_per_second )


                    for e in pygame.event.get( ):
                        # did the user try to close the window?
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            return

                        # did the user just press the escape key?
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                            pygame.quit()
                            return

                        if self.on:
                            self.paint( self.screen )

                        pygame.display.flip( )

                        if e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                            print("1 right click")
                            mx,my= pygame.mouse.get_pos()
                            mx= mx//(self.Csize+margin)
                            my= my//(self.Csize+margin)
                            secclick= True
                            grid[mx][my].setHighlight(True)
                            if grid[mx][my].getPl()== player.getPl():
                                while secclick:
                                    self.clock.tick( self.frames_per_second )
                                    print("loop")

                                    for e in pygame.event.get( ):
                                        # did the user try to close the window?
                                        if e.type == pygame.QUIT:
                                            pygame.quit()
                                            return

                                        # did the user just press the escape key?
                                        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                                            pygame.quit()
                                            return

                                        if self.on:
                                            self.paint( self.screen )

                                        pygame.display.flip( )


                                        if (e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]) or (e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]):

                                            print("1 right 1 left clicks")
                                            mx2,my2= pygame.mouse.get_pos()
                                            mx2= mx2//(self.Csize+5)
                                            my2= my2//(self.Csize+5)
                                            grid[mx][my].setHighlight(False)
                                            if grid[mx2][my2].getPl()!= player.getPl() and grid[mx2][my2].getPl()>=0:
                                                player.attack(mx,my,mx2,my2,grid)
                                                secclick= False
                                                grid[mx][my].setHighlight(False)

                                            elif grid[mx2][my2].getPl()== player.getPl():
                                                grid[mx][my].makefort(grid,mx,my,player)==False
                                                secclick= False
                                                grid[mx][my].setHighlight(False)

                                            else:
                                                print("not Valid")
                                                secclick= False
                                                grid[mx][my].setHighlight(False)

                                        elif (e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]) or (e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]) :
                                            print("not Valid")
                                            secclick= False
                                            grid[mx][my].setHighlight(False)
                            else:
                                grid[mx][my].setHighlight(False)






                        elif e.type== pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                            mx,my= pygame.mouse.get_pos()
                            mx= mx//(self.Csize+5)
                            my= my//(self.Csize+5)

                            if grid[mx][my].checkplacement(player, grid, mx, my):
                                grid[mx][my].capture(player,False,turns)
                                print(player.getPoints())


            for e in pygame.event.get( ):
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                if self.on:
                    self.paint( self.screen )



            #print("loop")

        return
