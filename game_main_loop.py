#imports
import pygame , sys 
from pygame.locals import *
from game_map import Game_map
from button import Button
from player import Player
from wall import Wall , Walls
#start pygame and set up the screen
pygame.init()
screen=pygame.display.set_mode()
#create the color
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
gray=(100,100,100)
pink=(250,200,200)
#create th game map
map_1=Game_map(0,0,(18,35),gray,40)
#create constants
size=(40,40)
size_1=(78,78)
#create the buttons functions
def func_e():
    player_1.direction='E' 
    player_1.move_it()
def func_w():
    player_1.direction='W' 
    player_1.move_it()
def func_n():
    player_1.direction='N' 
    player_1.move_it()
def func_s():
    player_1.direction='S' 
    player_1.move_it()
#create function to place the wall
def func_create_wall():
    i=int(player_1.i)
    j=int(player_1.j)
    if player_1.direction=='W':
        if j<player_1.game_map.size[1]-1:
            if not player_1.game_map.matrix[i][j+1]:
                wall=Wall(i,j+1,size,yellow)
               
                player_1.game_map.insert_item(wall)
                
            elif player_1.game_map.matrix[i][j+1]:
                player_1.game_map.matrix[i][j+1]=None

    elif player_1.direction=='E':
        if j>0:
            if not player_1.game_map.matrix[i][j-1]:
                wall=Wall(i,j-1,size,yellow)
                player_1.game_map.insert_item(wall)
                
            elif player_1.game_map.matrix[i][j-1]:
                player_1.game_map.matrix[i][j-1]=None
        
    elif player_1.direction=='S':
        if i>0:
            if not player_1.game_map.matrix[i-1][j]:
                wall=Wall(i-1,j,size,yellow)
                player_1.game_map.insert_item(wall)
                
            elif player_1.game_map.matrix[i-1][j]:
                player_1.game_map.matrix[i-1][j]=None
        
    elif player_1.direction=='N':
        if i<player_1.game_map.size[0]-1:
            if not player_1.game_map.matrix[i+1][j]:
                wall=Wall(i+1,j,size,yellow)
                player_1.game_map.insert_item(wall)
                
            elif player_1.game_map.matrix[i+1][j]:
                player_1.game_map.matrix[i+1][j]=None
#create the buttons
button_e=Button(16,33,size_1,red,func_e,1)
button_w=Button(16,29,size_1,red,func_w,1)
button_n=Button(14,31,size_1,red,func_n,1)
button_s=Button(16,31,size_1,red,func_s,1)
button_create_wall=Button(14,33,size_1,blue,func_create_wall,0)
#create the player
player_1=Player(2,2,size,'player_1.png',map_1)
#insert buttons and players  to map_1
map_1.insert_item(button_e)
map_1.insert_item(button_w)
map_1.insert_item(button_n)
map_1.insert_item(button_s)
map_1.insert_item(button_create_wall)
map_1.insert_item(player_1)
#game main loop
while True:
    screen.fill(black)
    map_1.run_it(screen)
    pygame.display.update()
    pygame.time.Clock().tick(60)