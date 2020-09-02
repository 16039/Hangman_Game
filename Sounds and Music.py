##Sounds and music

from tkinter import *
import pygame

root = Tk()
root.title("Code")
root.geometry("500x400")

pygame.mixer.init() #Turn on sound mixer

def stop():
    pygame.mixer.music.stop()

def play():
    pygame.mixer.music.load("Are you bored yet.mp3")
    pygame.mixer.music.play(loops = 0)
    

my_button = Button(root, text = "Play song", command = play, font = ("Arial", 32))
my_button.pack(pady = 20)

stop_button = Button(root, text = "Stop", command = stop)
stop_button.pack(pady = 20)


root.mainloop()