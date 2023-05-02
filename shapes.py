import pygame
import random

white=(255,255,255)
medgrey=(207,207,207)
dargrey=(87,87,87)
black=(0,0,0)
purple=(153,50,204)
fuchia=(255,0,255)
deepskyblue=(0,191,255)
blue=(0,0,255)
dodgerblue=(30,144,255)
yellow=(255,255,0)
gold=(255,215,0)
orange=(255,165,0)
greenyellow=(173,255,47)
green=(0,255,0)
darkolivegreen=(85,107,47)
olivegreen=(107,142,35)
darkgreen=(0,128,0)
lawngreen=(124,252,0)
red=(255,0,0)
maroon=(128,0,0)
darkbrown=(65,43,21)

class Saber:

    def __init__(self,surface,x,y,size,color):
        self.x=int(x)
        self.y=int(y)
        self.color=color
        self.size=int(size)

        pygame.draw.rect(surface, self.color,(self.x+(3*self.size),self.y-(300*self.size),20*self.size ,280*self.size ))

        pygame.draw.rect(surface, dargrey,(self.x+(7*self.size),self.y-(10*self.size) ,10*self.size ,20*self.size))

        pygame.draw.rect(surface, medgrey,(self.x-(5*self.size),self.y-(20*self.size) ,35*self.size ,10*self.size))

        pygame.draw.rect(surface, medgrey,(self.x-(3*self.size),self.y-(7*self.size) ,30*self.size ,5*self.size))

        pygame.draw.rect(surface, medgrey,(self.x,self.y,25*self.size ,100*self.size ))

        pygame.draw.circle(surface, red, (self.x+(12*self.size),self.y+(15*self.size)), 5*self.size)

        pygame.draw.rect(surface, dargrey,(self.x-(2*self.size),self.y+(45*self.size),5*self.size ,50*self.size ))

        pygame.draw.rect(surface, dargrey,(self.x+(10*self.size),self.y+(45*self.size),5*self.size ,50*self.size ))

        pygame.draw.rect(surface, dargrey,(self.x+(22*self.size),self.y++(45*self.size),5*self.size ,50*self.size ))

        return

class Sword:

    def __init__(self,surface,x,y,size,color):
        self.x=int(x)
        self.y=int(y)
        self.color=color
        self.size=int(size)

        pygame.draw.rect(surface, color,(self.x,self.y,12*self.size ,50*self.size ))
        pygame.draw.circle(surface, medgrey, (self.x+(6*self.size),self.y+(50*self.size)), 12*self.size)
        pygame.draw.circle(surface, color, (self.x+(6*self.size),self.y+(50*self.size)), 5*self.size)
        pygame.draw.rect(surface, medgrey,(self.x-(15*self.size),self.y,44*self.size ,7*self.size ))
        pygame.draw.polygon(surface, medgrey, [(self.x-(3*self.size),self.y),(self.x+(13*self.size),self.y),(self.x+(13*self.size),self.y-(140*self.size)),(self.x+(5*self.size),self.y-(150*self.size)),(self.x-(3*self.size),self.y-(140*self.size))])
        pygame.draw.rect(surface, dargrey,(self.x+(5*self.size),self.y-(140*self.size),2*self.size ,140*self.size ))

class Moon:

    def __init__(self,surface,x,y,size):
        self.x=int(x)
        self.y=int(y)
        self.size=int(size)

        pygame.draw.circle(surface, white, (self.x,self.y), 40*self.size)
        pygame.draw.circle(surface, dargrey, (self.x-(20*self.size),self.y-(10*self.size)), 15*self.size)
        pygame.draw.circle(surface, dargrey, (self.x+(25*self.size),self.y), 6*self.size)
        pygame.draw.circle(surface, dargrey, (self.x+(10*self.size),self.y+(18*self.size)), 10*self.size)

class Star:

    def __init__(self,surface,x,y,size):
        self.x=int(x)
        self.y=int(y)
        self.size=int(size)

        pygame.draw.polygon(surface, yellow, [(self.x,self.y),(self.x+(5*self.size),self.y+(20*self.size)),(self.x+(15*self.size),self.y+(25*self.size)),(self.x+(5*self.size),self.y+(30*self.size)),(self.x,self.y+(50*self.size)),(self.x-(5*self.size),self.y+(30*self.size)),(self.x-(15*self.size),self.y+(25*self.size)),(self.x-(5*self.size),self.y+(20*self.size))])
        pygame.draw.circle(surface, white, (self.x+(5*self.size),self.y+(20*self.size)), 5*self.size)
        pygame.draw.circle(surface, white, (self.x+(10*self.size),self.y+(15*self.size)), 3*self.size)
        pygame.draw.circle(surface, white, (self.x+(15*self.size),self.y+(10*self.size)), 1*self.size)

class land:

    def __init__(self,surface,y,size):
        self.x=-200
        self.y=int(y-50)
        self.size=int(size)

        pygame.draw.polygon(surface, darkbrown, [(self.x,self.y),(self.x+(50*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(100*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(160*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(200*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(300*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(370*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(400*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(1000*self.size),self.y-(random.randrange(0,200)*self.size)),(self.x+(1000*self.size),self.y+(1000*self.size))])

class Darth:

    def __init__(self,surface,x,y,size):
        self.x=int(x)
        self.y=int(y)
        self.size=int(size)

        pygame.draw.circle(surface, black, (self.x,self.y), 15*self.size)
        pygame.draw.polygon(surface, black, [(self.x-(15*self.size),self.y),(self.x-(25*self.size),self.y+(20*self.size)),(self.x+(25*self.size),self.y+(20*self.size)),(self.x+(15*self.size),self.y)])
        pygame.draw.circle(surface, dargrey, (self.x+(5*self.size),self.y+(5*self.size)), 4*self.size)
        pygame.draw.circle(surface, dargrey, (self.x-(5*self.size),self.y+(5*self.size)), 4*self.size)
        pygame.draw.polygon(surface, dargrey, [(self.x,self.y+(10*self.size)),(self.x+(10*self.size),self.y+(21*self.size)),(self.x-(10*self.size),self.y+(21*self.size))])
