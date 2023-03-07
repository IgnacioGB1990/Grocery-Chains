import pygame
from pygame import mixer

def playSound2():
    mixer.init()
    mixer.music.load("././assets/won.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()