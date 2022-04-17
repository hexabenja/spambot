import pyautogui
import tkinter
import time
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
raiz = Tk() # Nombre de la variable TK
raiz.geometry('300x200') # anchura x altura
raiz.configure(bg = 'black') # Color de fondo de ventana
raiz.title('SPAMBOT') # Titulo de Ventana
raiz.iconbitmap("floppa.ico") # Favicon
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM) # Boton de salida
raiz.mainloop() # Para mantener la ventana abierta en bucle
