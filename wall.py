#imports
import pygame , sys 
from pygame.locals import *
from game_map import Game_map
#create wall class
class Wall():
    def __init__(self,i,j,size,color):
        self.i=i
        self.j=j
        self.size=size
        self.color=color
        self.x=None
        self.y=None
    #create function to draw the wall on map
    def run_it(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.size[0],self.size[1]))
#create walls class
class Walls():
    def __init__(self,i,j,length,type,size,color,game_map):
        if type==0:
            while j<length:
                wall=Wall(i,j,size,color)
                game_map.insert_item(wall)
                j+=1
            
        elif type==1:
            while i<length:
                wall=Wall(i,j,size,color)
                game_map.insert_item(wall)
                i+=1