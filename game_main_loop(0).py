#imports
import pygame , sys 
from pygame.locals import *
from game_map import Game_map
from button import Button
from player import Player , Players
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
pink=(250,150,150)
sky=(100,100,150)
#create constants
size_1=(75,75)
size_2=(50,50)
#create game maps
map_1=Game_map(240,0,(72,72),gray,10)
map_2=Game_map(1200,560,(2,3),black,80)
#create the functions
def func_e():
    players_1.direction='E'
    players_1.move_it()
def func_w():
    pass
def func_n():
    pass
def func_s():
    pass
#create buttons
button_e=Button(1,2,size_1,red,func_e,1)
button_w=Button(1,0,size_1,red,func_w,1)
button_n=Button(0,1,size_1,red,func_n,1)
button_s=Button(1,1,size_1,red,func_s,1)
#insert buttons to map_2
map_2.insert_item(button_e)
map_2.insert_item(button_w)
map_2.insert_item(button_n)
map_2.insert_item(button_s)
#create th players
player_1=Player(5,5,map_1)
#create visible players
players_1=Players(5,5,player_1,map_1)
#player_1 image
player_1.image='player_1.png'
player_1.size=size_2
#insert players to map_1
map_1.insert_item(player_1)
#game main loop
while True:
    screen.fill(black)
    map_1.run_it(screen)
    map_2.run_it(screen)
    pygame.display.update()