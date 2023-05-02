
import pygame
import game
import map

grass=(183,215,30)
Lightgrass=(183,202,121)
Darkgrass=(103,126,82)
black=(0,0,0)
yellow=(254, 255, 13)


class Units:



    def __init__(self,x,y,size):
        self.X=x
        self.Y=y
        self.df=0
        self.off=0
        self.pl=-1
        self.size=size
        self.type=-1
        self.color=[grass,Lightgrass,Darkgrass]
        self.fort=0
        self.highlight=False

    def __str__(self):
        return "X:"+str(self.X//(self.size+5))+" Y:"+str(self.Y//(self.size+5))+" PL: "+str(self.pl)+" Type: "+str(self.type)+" Off: "+str(self.off)+" Df: "+str(self.df)

    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getDf(self):
        return self.df
    def getOff(self):
        return self.off
    def getPl(self):
        return self.pl
    def getSize(self):
        return self.size
    def getType(self):
        return self.type
    def getColor(self,i):
        return self.color[i]
    def getFort(self):
        return int(self.fort)
    def getHighlight(self):
        return self.highlight

    def setHighlight(self,x):
        self.highlight=x

    def setColor(self,color):
        self.color=color

    def drawcell(self, surface):
        if self.getHighlight():
            pygame.draw.rect(surface, (self.getColor(1)),(self.getX(),self.getY(),self.getSize(),self.getSize() ))
        else:
            pygame.draw.rect(surface, (self.getColor(0)),(self.getX(),self.getY(),self.getSize(),self.getSize() ))
        if self.type==0:
            pygame.draw.circle(surface, black,(self.getX()+(self.getSize()//2),self.getY()+(self.getSize()//2)),self.getSize()//3)
        if self.type==1:
            pygame.draw.circle(surface, black,(self.getX()+(self.getSize()//2),self.getY()+(self.getSize()//2)),self.getSize()//2,4)
        if self.type>=2:
            pygame.draw.circle(surface, black,(self.getX()+(self.getSize()//2),self.getY()+(self.getSize()//2)),self.getSize()//3)
            pygame.draw.rect(surface, black,(self.getX()+(self.getSize()//2)-((self.getSize()//5)//2),self.getY(),self.getSize()//5,self.getSize() ))
        if self.type>=3:
            pygame.draw.rect(surface, black,(self.getX(),self.getY()+(self.getSize()//2)-((self.getSize()//5)//2),self.getSize(),self.getSize()//5 ))
        if self.type>=5:
            pygame.draw.circle(surface, yellow,(self.getX()+(self.getSize()//2),self.getY()+(self.getSize()//2)),self.getSize()//5)

    def upgrade(self,pl):
        if self.type==0:
            self.pl=pl.getPl()
            self.df=1
            self.off=1
        elif self.type==1:
            self.pl=pl.getPl()
            self.df=4
            self.off=0
        elif self.type==2:
            self.pl=pl.getPl()
            self.df=1
            self.off=3
        elif self.type==3:
            self.pl=pl.getPl()
            self.df=8
            self.off=8
        elif self.type==4:
            self.pl=-1
            self.df=0
            self.off=0
            self.type=-1
            self.color=[grass,Lightgrass,Darkgrass]
        elif self.type==5:
            self.pl=pl.getPl()
            self.df=8
            self.off=8
            self.type=5


    def region(self,grid,size,x,y):

        #if xc is over edge set xc to # XXX:

        xc=x-size
        yc=y-size
        ex=x+size+1
        ey=y+size+1

        if xc<0:
            xc=0
        if yc<0:
            yc=0
        if ex>len(grid):
            ex=len(grid)
        if ey>len(grid[1]):
            ex=len(grid[1])


        new=[]
        sli1=grid[xc:ex]
        for l in sli1:
            new.append(l[yc:ey])
        return new




    def checkplacement(self, pl, grid, mx, my,attack,turns):
        c=0
        newgrid = self.region(grid,3,mx,my)

        if self.type>=3:
            return "You've upgraded that one to the Max. Choose Another."

        if pl.getCount(grid)<=0:
            if mx<3 or my<3 or mx>=len(grid)-3 or my>=len(grid[1])-3 :
                return "Too close to the Edge"
            for row in newgrid:
                for cell in row:
                    #cell.setColor((255,0,0))

                    if cell.getPl()!=-1:
                        c+=1
            if c>0:
                return "Too close to the enemy"
            else:
                self.capture(pl,attack,turns)
                return "Claim More Terrain!"

        if grid[mx][my].getPl()==pl.getPl():
            self.capture(pl,attack,turns)
            return "Claim More Terrain!"


        if grid[mx][my].getPl()!=-1:
            return "That is already Taken By the enemy! Try Attacking them!"

        newgrid = self.region(grid,1,mx,my)
        for row in newgrid:
            for cell in row:
                if cell.getPl()==pl.getPl():
                    c+=1
        if c>0:
            self.capture(pl,attack,turns)
            return "Claim More Terrain!"
        else:
            return "Too far to capture!"
        self.capture(pl,attack,turns)
        return "Claim More Terrain!"


    def makefort(self,grid,mx,my,pl):
        if self.getFort()+grid[mx][my-1].getFort()+grid[mx][my+1].getFort()+grid[mx-1][my].getFort()+ grid[mx+1][my].getFort()<=0:
            if self.getType()>=1 and grid[mx][my-1].getType()>=1 and grid[mx][my+1].getType()>=1 and grid[mx-1][my].getType()>=1 and grid[mx+1][my].getType()>=1:
                if grid[mx][my-1].getPl()==self.getPl() and grid[mx][my+1].getPl()==self.getPl() and grid[mx-1][my].getPl()==self.getPl() and grid[mx+1][my].getPl()==self.getPl():
                    if self.fort<2:
                        self.fort=2
                    grid[mx][my-1].fort=1
                    grid[mx][my+1].fort=1
                    grid[mx-1][my].fort=1
                    grid[mx+1][my].fort=1
                    return "You've built a Fort!"
                else:
                    return "Capture more Terrain to Build a Fort Here"
            else:
                return "Upgrade your men to Build a Fort"
        else:
            return "This location already has a Fort"
            #re arrang order to better inform player what is needed in order


    def capture(self,player,attack,turns):


        if turns==1:
            self.type=5
        else:
            self.type+=1
            self.pl=player.getPl()
        if not attack:
            player.subpoint(1)
        self.setColor(player.getColor())
        self.upgrade(player)
        print(str(self))
