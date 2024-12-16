"""
Javier Mejía Alecio (20304)

"""
#Se importan las librerias y módulos necesarios
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import csv
from tkinter import messagebox
import pandas as pd
import numpy as np
import seaborn
import Basic 
import Instrumentos 


#Se crea la clase maestra que es la que mantiene el programa corriendo y es nuetro primer bloque de código relativamente "grande"
class aplic():
    #Se crea la funición principal
    def __init__(self):
        #Se crea la ventana master. A esta ventana el usuario no tiene acceso por ser la que mantiene el loop del programa
        self.master = Tk()
        self.master.geometry("1x1")
        self.master.withdraw()
        
        
        #Se crea una sub-ventana     la cual es la primera ventana principal. Se definen características como la forma, lugar de aparición, título, icono, color y las fuentes utilizadas más adelante
        self.info = tk.Toplevel()
        self.info.title("Aplicación")
        self.info.geometry("420x500+425+125")
        self.info.resizable(False, False)
        #self.info.configure(bg = "#D0B77E")
        fontStyle = tkFont.Font(family="Helvetica", size=30)
        fontt = tkFont.Font(family = "Helvetica", size = 14)
        fontb = tkFont.Font(family = "Helvetica", size = 20)
        fontO = tkFont.Font(family = "Helvetica", size = 12)
        fontO.configure(underline = True)
        
        #Se crean los objetos como los botones y los labels que van a indicarle al usuario lo que tiene que hacer y le van a permitir interactuar con el programa

        self.info.btn_basicos = tk.Button(self.info, text="Básicos", font=fontStyle, command = lambda: bas(self.info))
        self.info.btn_basicos.pack(pady=100)

        # Botón de "Instrumentos"
        self.info.btn_instrumentos = tk.Button(self.info, text="Instrumentos", font=fontStyle, command = lambda: Ins(self.info))
        self.info.btn_instrumentos.pack(pady=20)

        

           
        #Se crea el loop principal para la aplicación
        self.master.mainloop()        
        
                
        
        

#Se crea la función para que pueda acceder a otro bloque de información (clase) que se encuentra en otro módulo
def bas(self):
    self.destroy()
    Basic.basico()  

def Ins(self):
    self.destroy()
    Instrumentos.Instrumentos()  
    
        
        
#Se crea la función para la función que inicial comience         
def main():
    app = aplic()
    return(0)
        
if __name__ == '__main__':
    main()