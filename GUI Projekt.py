#!/usr/bin/env python3

import tkinter as tk

import random
import socket as so

from tkinter import *
from tkinter import messagebox
import serial

#so= socket.socket()                                                  #für drahtlose Kommunikation

#so.connect(('172.20.10.3', 30303))

#so.setblocking(True)
#so.recv(1024) 
#so.recv(1024)



esp_server = serial.Serial('COM3', 9600)
input = esp_server.readline()
      

#---------------------------Comandos erstellen------
def button_action():
    anweisungs_label.config(text="Ich wurde geändert!")
#---------- input verwerden und passende Antwort in einer Zeile im selben Fenster ausgeben.
def abfrage():
    while True:
        if input ==(b'0\r\n'):
            anweisungs_label.config(text="Ich bin immer noch leer")
        elif input == (b'1\r\n'):
            anweisungs_label.config(text="Pooooost")
        elif input ==(b'2\r\n'):
            anweisungs_label.config(text="Meine Tür ist noch geöffnet")

        break
        fenster.update()
        sleep(2)
        refresh_label.config(text=" Nochmal?")
    
    
    return

#Input verwerten und jeweilig passede Antwort in einem extra Fenster ausgeben.
def status_abfrage():
    if input ==(b'0\r\n'):
        s_text="\
************************\n\
Der aktuelle Status deines Briefkastens\n\
lauet = Leer!\n\
Schau später erneut vorbei\n\
************************"
        
        messagebox.showinfo(message=s_text, title = "Status")
    elif input ==(b'1\r\n'):
        s_text="\
************************\n\
Der aktuelle Status deines Briefkastens\n\
lauet = Voll!\n\
Ich kann geleert werden.\n\
************************"
        
        messagebox.showinfo(message=s_text, title = "Status")

    elif input ==(b'2\r\n'):
        s_text="\
************************\n\
Momentan scheint dein Briefkasten nicht verschloßen zu sein.\n\
Bitte überprüfe dies, ansonsten kann ich dir nicht den Status ausgeben\n\
Nicht, dass sich jemand Unbefugtes bedient.\n\
************************"
        messagebox.showinfo(message=s_text, title = "Status")


#---- Ausgabetext beim Infobutton
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: L. Schiphorst & C. Tusche\n\
Stichtag 14.06.2018\n\
Version: 1.4\n\
Kundenservice :+4915226539014 \n\
************************"
	begruessung_label.pack 
	messagebox.showinfo(message=m_text, title = "Infos")
        
fenster = Tk()
#Überschrift des Fensters
fenster.title("Bedienprogramm ")



#--------------- Menüleiste erstellen

menuleiste = Menu(fenster)

#----------- Menü - Reiter: Datei, Extra und Status erstellen
datei_menu = Menu(menuleiste, tearoff=0)
extra_menu = Menu(menuleiste, tearoff=0)
status_menu = Menu(menuleiste,tearoff=0)


# --------------Drop-Down für Reiter erstellen
datei_menu.add_command(label="Anwenden", command=button_action)
datei_menu.add_separator() # Trennlinie
datei_menu.add_command(label="Exit", command=fenster.quit)

extra_menu.add_command(label="Info!", command=action_get_info_dialog)
status_menu.add_command(label="Status!", command =status_abfrage)

# Nun fügen wir die Menüs (Datei, Extra ud Status) der Menüleiste hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Extra", menu=extra_menu, bitmap ="info")
menuleiste.add_cascade(label="Status", menu=status_menu)
# Die Menüleiste mit den Menüeinträgen noch dem Fenster übergeben.
fenster.config(menu=menuleiste, bg ="#FBEFF8")



#----------------Lables und Buttons erstellen
begruessung_label = Label(fenster, text="Ich bin dein persönlicher Briefkasten Assistent",bg = "#FBEFF8", fg="#B4045F")
anweisungs_label = Label(fenster, text="Für einen aktuellen Status:\n\
Klicke auf 'refresh'.",bg = "#FBEFF8")
refresh_button = Button(fenster, text="Refresh", command=abfrage, bg ='#FACC2E')
refresh_label = Label(fenster, text="Für eine erweiterte Ausgabe, drücke 'Erweiterter Status'", bg = "#FBEFF8")
status_label = Label(fenster, text=input, bg = "#FBEFF8", fg ="#F5A9BC")
exit_button = Button(fenster, text="Beenden", command=fenster.quit, bg='#FF0040')
B1 = Button(fenster, text = "Erweiterter Status", command = status_abfrage, bg ='#40FF00')
neu_button =Button(fenster, text ="Neu", command = fenster.update())

#Lables und Buttons in gewünschter Reihenfolge dem Fenster hinzufügen und platzieren
begruessung_label.grid(row=1, column=1)

anweisungs_label.grid(row=2, column=1)
status_label.grid(row=1, column=2)
refresh_button.grid(row=2, column=2)
refresh_label.grid(row=3, column=1)
B1.grid(row=3, column=2)
exit_button.grid (row=4, column=1)
fenster.mainloop()



