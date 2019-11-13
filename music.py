import pygame
import tkinter
from pygame import mixer
from tkinter import *

mixer.init()



pygame.init()

root = tkinter.Tk()
root.configure(bg="silver")
root.title("Music Library")
root.geometry("800x500")
mixer.init()


isPause = False


def play():
    pygame.mixer.music.load("song.mp3")
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




scale = Scale(root,length=130, width=25, from_=0, to=100, orient=HORIZONTAL, command = set_vol)
scale.place(x=90, y=285)


btn_play = tkinter.Button(root, font='Times 15 bold', height=3, width=8, text="Play", fg="white",
                          bg="black", command=play)
btn_play.place(x=90, y=15)

btn_pause = tkinter.Button(root,font='Times 15 bold', height=3, width=8, text="Pause", fg="white",
                           bg="black", command=pause)
btn_pause.place(x=90, y=80)

btn_stop = tkinter.Button(root,font='Times 15 bold', height=3, width=8, text="Stop", fg="white",
                          bg="black", command=stop)
btn_stop.place(x=90, y=140)

btn_exit = tkinter.Button(root,font='Times 15 bold', height=3, width=8, text="Exit", fg="white",
                          bg="black", command=quit)
btn_exit.place(x=90, y=200)

root.mainloop()