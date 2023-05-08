#imports
import pygame , sys
from pygame.locals import *
#create button class
class Button():
    def __init__(self,i,j,size,color,function,type):
        self.x=None
        self.y=None 
        self.i=i 
        self.j=j
        self.size=size 
        self.function=function 
        self.type=type 
        
        self.clicked=False 
        self.color=color
        self.clicked_color=(color[0]/2,color[1]/2,color[2]/2)
    #create function to run the button
    def run_it(self,screen):
        #draw the button
        if self.clicked:
            pygame.draw.rect(screen,self.clicked_color,(self.x,self.y,self.size[0],self.size[1]))
        elif not self.clicked:
            pygame.draw.rect(screen,self.color,(self.x,self.y,self.size[0],self.size[1]))
        
        xb=self.x
        xe=xb+self.size[0]
        yb=self.y
        ye=yb+self.size[1]
        #one press   
        if self.type==0:
            pos=pygame.mouse.get_pos()
            press=pygame.mouse.get_pressed()[0]
            if (xb<pos[0]<xe)&(yb<pos[1]<ye):
                if (press==1)&(not self.clicked):
                    self.function()
                    self.clicked=True
            if press==0:
                self.clicked=False
        #multi press  
        elif self.type==1:
            pos=pygame.mouse.get_pos()
            press=pygame.mouse.get_pressed()[0]
            if (xb<pos[0]<xe)&(yb<pos[1]<ye):
                if press==1:
                    self.function()
                    self.clicked=True
            if press==0:
                self.clicked=False