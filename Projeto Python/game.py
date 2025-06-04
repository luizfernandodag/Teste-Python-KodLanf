import math
import random
import time

from pygame import Rect

alien = Actor("alien")
alien.pos = 100, 56
WIDTH = 500
HEIGHT = alien.height + 20
alien.topright = 0, -10


#games states

game_started = False
music_on = True 

#Buttons

# btn_start = Rect(300, 200, 200, 50)
# btn_music = Rect(300, 270, 200, 50)
# btn_exit = Rect(300, 340, 200, 50)

def draw():
    screen.clear()
    alien.draw()
    
def update():
    alien.left+=2
    if alien.left > WIDTH:
        alien.rigth =0
        
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("You missed me")

def set_alien_hurt():
    alien.image = "alien_hurt"
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)
    

def set_alien_normal():
    alien.image = 'alien'