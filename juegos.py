# !/usr/bin/python3
from tkinter import *
import threading
import sys
import os



from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def arkt():
    os.system ("start cartas/juegos.py")


def arkanoid():
   hilo1 = threading.Thread(target=arkt)
   hilo1.start()

B = Button(top, text = "Hello", command = arkanoid)
B.place(x = 50,y = 50)

top.mainloop()