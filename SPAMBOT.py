from multiprocessing.spawn import spawn_main
import pydoc
import pyautogui
import tkinter
import time
import os

# Script python
# f = open('spam', 'r')
# time.sleep(5)
# for word in f:
    # pyautogui.typewrite(word)
    # pyautogui.press("enter")

# Script Ventana
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

def start(self):
        self.im = pydoc.open(os.getcwd() + "assets/Script.py")

raiz = Tk() # Nombre de la variable TK
raiz.geometry('600x600') # anchura x altura
raiz.configure(bg = 'black') # Color de fondo de ventana
raiz.title('SPAMBOT') # Titulo de Ventana
raiz.iconbitmap("floppa.ico") # Favicon
miFrame=Frame()
miFrame.pack()
Label(miFrame, text= "Spambot", fg="black", font=("Calibri Light", 18)).place(x=200, y=10)
miFrame.config(bg="gray")
miFrame.config(width=600, height=550)
miFrame.config(bd=45)
miFrame.config(relief="groove")
botonst= tkinter.Button(text="Iniciar script", command=start).pack(side=BOTTOM)
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM) # Boton de salida
raiz.mainloop() # Para mantener la ventana abierta en bucle

