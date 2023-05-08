#imports
import pygame , sys 
from pygame.locals import *
from game_map import Game_map
from wall import Wall
#create color
gray=(100,100,100)
#create player class
class Player():
    def __init__(self,i,j,game_map):
        self.i=i 
        self.j=j 
        self.game_map=game_map
        self.image=None 
        self.size=None 
        self.x=None 
        self.y=None
        self.direction='E'
    #create method to run the player
    def run_it(self,screen):
        if self.image:
            x=self.x
            y=self.y
            image=pygame.image.load(self.image)
            image=pygame.transform.scale(image,self.size)
            screen.blit(image,(x,y))
    #create method to move the player
    def move_it(self):
        i=int(self.i)
        j=int(self.j)
        sub_map=Game_map(0,0,(10,10),gray,4,self.i,self.j)
        if self.direction=='E':
            if self.j<self.game_map.size[1]-1:
                if not self.game_map.matrix[i][j+1]:
                    self.game_map.matrix[i][j]=None 
                    self.j+=0.2
                    self.game_map.insert_item(self)
     
        elif self.direction=='W':
            if self.j>0:
                if not self.game_map.matrix[i][j-1]:
                    self.game_map.matrix[i][j]=None 
                    self.j-=0.2
                    self.game_map.insert_item(self)

        elif self.direction=='N':
            if self.i>0:
                if not self.game_map.matrix[i-1][j]:
                    self.game_map.matrix[i][j]=None
                    self.i-=0.2
                    self.game_map.insert_item(self)
         
        elif self.direction=='S':
            if self.i<self.game_map.size[0]-1:
                if not self.game_map.matrix[i+1][j]:
                    self.game_map.matrix[i][j]=None 
                    self.i+=0.2
                    self.game_map.insert_item(self)
#create players class to create a group of player that they will move together
class Players():
    def __init__(self,n,m,first_player,game_map):
        self.n=n 
        self.m=m 
        self.first_player=first_player
        self.game_map=game_map
        
        i=self.first_player.i
        j=self.first_player.j
        for a in range(i,self.n+i):
            for b in range(j,self.m+j):
                player=Player(a,b,self.game_map)
                self.game_map.insert_item(player)
        self.direction='E'
    #create method to move players together
    def move_it(self):
        if self.direction=='E':
            j=(self.first_player.j+self.m)-1
            je=self.first_player.j
            ae=self.first_player.i
            a=(ae+self.n)-1
            while j>=je:
                i=a
                while i>ae:
                    self.game_map.matrix[i][j].direction='E'
                    self.game_map.matrix[i][j].move_it()
                    i-=1
                j-=1

        elif self.direction=='W':
            pass
            
        elif self.direction=='N':
            pass
            
        elif self.direction=='S':
            pass