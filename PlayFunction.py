import tkinter
import pygame
from pygame import mixer
from tkinter import *

root = tkinter.Tk()
root.configure(bg="white")
root.title("Music Library")
root.geometry("800x500")
pygame.init()
mixer.init()

isPause = False


def play():
    pygame.mixer.music.load("star_wars.wav")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(0)


def pause():
    global isPause
    if isPause == False:
        pygame.mixer.music.pause()
        isPause = True
    else:
        pygame.mixer.music.unpause()
        isPause = False


def stop():
    pygame.mixer.music.stop()


def quit():
    root.quit()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


btn_play = tkinter.Button(root, text="Play", fg="blue",
                          bg="white", command=play)
btn_play.pack()

btn_pause = tkinter.Button(root, text="Pause", fg="blue",
                           bg="white", command=pause)
btn_pause.pack()

btn_stop = tkinter.Button(root, text="Stop", fg="blue",
                          bg="white", command=stop)
btn_stop.pack()

btn_exit = tkinter.Button(root, text="Exit", fg="blue",
                          bg="white", command=quit)
btn_exit.pack()
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.pack()

root.mainloop()
