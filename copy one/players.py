purple=(153,50,204)
Lightpurple=(186, 139, 217)
Darkpurple=(73, 70, 166)

orange=(240, 160, 8)
Lightorange=(249, 194, 34)
Darkorange=(218, 123, 3)

red=( 191, 4, 38)
Lightred=(241,51, 19)
Darkred=(140, 3, 28)

blue=(5, 219, 242)
Lightblue=(5, 242, 242)
darkblue=(3, 120, 166)

startmax=5


class Players:
    def __init__(self,pl,name):
        self.name=str(name)
        self.maxpoints=startmax
        self.points=0
        self.pl=pl
        self.count=0
        self.color=self.checkcolor()


    def getName(self):
        return self.name
    def getPoints(self):
        return self.points
    def getPl(self):
        return self.pl
    def getCount(self,grid):
        count=0
        for row in grid:
            for cell in row:
                if cell.getPl()==self.getPl():
                    count+=1
        self.count=count
        return self.count
    def getColor(self):
        return self.color
    def setMaxPoints(self):
        self.points=self.maxpoints
    def setPoints(self,num):
        self.points=num

    def subpoint(self,am):
        self.points=self.points-am

    def checkforts(self,grid,size,margin):
        self.maxpoints=startmax
        for row in grid:
            for item in row:
                if item.getFort()==2 and item.getPl()==self.getPl():
                    mx= item.getX()//(size+margin)
                    my= item.getY()//(size+margin)
                    if grid[mx][my-1].getPl()==self.getPl() and grid[mx][my+1].getPl()==self.getPl() and grid[mx-1][my].getPl()==self.getPl() and grid[mx+1][my].getPl()==self.getPl():
                        self.maxpoints+=1
                    else:
                        grid[mx][my].fort=0
                        grid[mx][my-1].fort=0
                        grid[mx][my+1].fort=0
                        grid[mx-1][my].fort=0
                        grid[mx+1][my].fort=0

    def checkcastle(self,grid):
        check=0
        for row in grid:
            for item in row:
                if item.getType()>=5 and item.getPl()==self.getPl():
                    check+=1
        if check<1:
            return False
        else:
            return True





    def checkcolor(self):
        if self.pl==1:
            return [purple,Lightpurple,Darkpurple]
        elif self.pl==2:
            return [orange,Lightorange,Darkorange]
        elif self.pl==3:
            return[blue,Lightblue,darkblue]
        elif self.pl==4:
            return [red,Lightred,Darkred]



    def checkpoints(self):
        if self.getPoints()>0:
            return True
        else:
            return False

    def attackdirection(self,mx,my,mx2,my2):
        if my==my2:
            if mx>mx2:
                return 0 #left
            else:
                return 1 #Right"
        elif mx==mx2:
            if my>my2:
                return 2 #Up"
            else:
                return 3 #Down"
        elif my>my2:
            if mx<mx2:
                return 4 #Rightup"
            else:
                return 5 #Leftup"
        else:
            if mx<mx2:
                return 6 #rightdown"
            else:
                return 7 #leftdown"

    def checkattackrange(self,dir,grid,mx,my):
        if dir==0: #left
            if grid[mx-1][my].getPl()>=0 and grid[mx-1][my].getPl()!=grid[mx][my].getPl():
                #grid[mx-1][my].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==1: #Right"
            if grid[mx+1][my].getPl()>=0 and grid[mx+1][my].getPl()!=grid[mx][my].getPl():
                #grid[mx+1][my].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==2: #Up"
            if grid[mx][my-1].getPl()>=0 and grid[mx][my-1].getPl()!=grid[mx][my].getPl():
                #grid[mx][my-1].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==3: #Down"
            if grid[mx][my+1].getPl()>=0 and grid[mx][my+1].getPl()!=grid[mx][my].getPl():
                #grid[mx][my+1].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==4: #Rightup"
            if grid[mx+1][my-1].getPl()>=0 and grid[mx+1][my-1].getPl()!=grid[mx][my].getPl():
                #grid[mx+1][my-1].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==5: #Leftup"
            if grid[mx-1][my-1].getPl()>=0 and grid[mx-1][my-1].getPl()!=grid[mx][my].getPl():
                #grid[mx-1][my-1].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==6: #rightdown"
            if grid[mx+1][my+1].getPl()>=0 and grid[mx+1][my+1].getPl()!=grid[mx][my].getPl():
                #grid[mx+1][my+1].setColor((255,0,0))
                return True
            else:
                return False
        elif dir==7: #leftdown"
            if grid[mx-1][my+1].getPl()>=0 and grid[mx-1][my+1].getPl()!=grid[mx][my].getPl():
                #grid[mx-1][my+1].setColor((255,0,0))
                return True
            else:
                return False
        else:
            return False

    def opositedir(self,dir):
        if dir==0: #left" [mx-1][my]
            return 1

        elif dir==1: #Right" [mx+1][my]
            return 0

        elif dir==2: #Up" [mx][my-1]
            return 3

        elif dir==3: #Down" [mx][my+1]
            return 2

        elif dir==4: #Rightup" [mx+1][my-1]
            return 7

        elif dir==5: #Leftup" [mx-1][my-1]
            return 6

        elif dir==6: #rightdown" [mx+1][my+1]
            return 5

        elif dir==7: #leftdown" [mx-1][my+1]
            return 4


    def attacklist(self,dir,grid,mx,my,good):
        line=[]
        i=1
        if dir==0: #left" [mx-1][my]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx-1][my].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx-i][my].getPl()==select:
                    line.append(grid[mx-i][my])
                else:
                    break
                i+=1

        elif dir==1: #Right" [mx+1][my]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx+1][my].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx+i][my].getPl()==select:
                    line.append(grid[mx+i][my])
                else:
                    break
                i+=1

        elif dir==2: #Up" [mx][my-1]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx][my-1].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx][my-i].getPl()==select:
                    line.append(grid[mx][my-i])
                else:
                    break
                i+=1

        elif dir==3: #Down" [mx][my+1]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx][my+1].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx][my+i].getPl()==select:
                    line.append(grid[mx][my+i])
                else:
                    break
                i+=1

        elif dir==4: #Rightup" [mx+1][my-1]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx+1][my-1].getPl()

            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx+i][my-i].getPl()==select:
                    line.append(grid[mx+i][my-i])
                else:
                    break
                i+=1

        elif dir==5: #Leftup" [mx-1][my-1]
            i=1
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx-1][my-1].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx-i][my-i].getPl()==select:
                    line.append(grid[mx-i][my-i])
                else:
                    break
                i+=1

        elif dir==6: #rightdown" [mx+1][my+1]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx+1][my+1].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx+i][my+i].getPl()==select:
                    line.append(grid[mx+i][my+i])
                else:
                    break
                i+=1

        elif dir==7: #leftdown" [mx-1][my+1]
            if good:
                select=grid[mx][my].getPl()
            else:
                select=grid[mx-1][my+1].getPl()
            if grid[mx][my].getPl()==select:
                line.append(grid[mx][my])
            while True:
                if grid[mx-i][my+i].getPl()==select:
                    line.append(grid[mx-i][my+i])
                else:
                    break
                i+=1
        return line

    def addDf(self,lst):
        total=0
        for item in lst:
            total+=item.getDf()
        return total

    def addOff(self,lst):
        total=0
        for item in lst:
            total+=item.getOff()
        return total

    def capturelist(self,lst):
        for item in lst:
            item.capture(self,True,10)


    def attack(self,mx,my,mx2,my2,grid):
            dir=self.attackdirection(mx,my,mx2,my2)
            print(dir)
            odir=self.opositedir(dir)
            if self.checkattackrange(dir,grid,mx,my):
                enemy=self.attacklist(dir,grid,mx,my,False)
                good=self.attacklist(odir,grid,mx,my,True)
                enDf=self.addDf(enemy)
                goodOff=self.addOff(good)
                if goodOff>=enDf*2:
                    self.capturelist(enemy)
                    print('attack')
                else:
                    print("you wouldn't win that attack")
            else:
                print ("too far")
