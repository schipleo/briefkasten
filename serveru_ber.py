import tkinter as tk
import random
import socket

size=25                                                             #Integer erstellen 
length=1
feedcollision=False

                             # zufälliger Feedpoint(Apfel)



w = tk.Canvas(tk.Tk(), width=500, height=500)                       #Canvas = Zeichenebene 
w.pack()



for x in range(50,450,25):                                          #erstellen des Spielfeldes
    for y in range(50,450,25):
        w.create_rectangle(x, y, x+size, y+size, fill="yellow")     #füllt es gelb aus

s= socket.socket()                                                  #für drahtlose Kommunikation
s.connect(('192.168.43.51', 30303))
s.setblocking(True)           


                
