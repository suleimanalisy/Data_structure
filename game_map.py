#imports
import pygame , sys 
from pygame.locals import *
#create game map class 
class Game_map():
    def __init__(self,x,y,size,color,scale,i=None,j=None):
        self.x=x 
        self.y=y 
        self.size=size
        self.color=color 
        self.scale=scale

        self.i=i
        self.j=j
        self.matrix=[]
        for i in range(self.size[0]):
            self.matrix.append([])
            for j in range(size[1]):
                self.matrix[i].append(None)
    #create function to insert item to game map matrix
    def insert_item(self,item):
        self.matrix[int(item.i)][int(item.j)]=item
    #create function to run game map
    def run_it(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.size[1]*self.scale,self.size[0]*self.scale))
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.matrix[i][j]:
                    self.matrix[i][j].x=self.x+(j*self.scale)
                    self.matrix[i][j].y=self.y+(i*self.scale)
                    self.matrix[i][j].run_it(screen)