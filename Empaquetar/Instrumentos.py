import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import csv
from tkinter import messagebox
import pandas as pd
from pydub import AudioSegment
from pydub.playback import play
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi
import threading
from playsound import playsound
import Main
from PIL import Image, ImageTk
X = []
Y = []
fig, ax = plt.subplots(figsize=(15.9, 5))


class Instrumentos:
    def __init__(self):
        self.ins = Toplevel()
        w, h = self.ins.winfo_screenwidth(), self.ins.winfo_screenheight()
        self.ins.geometry("%dx%d+0+0" % (w, h))
        self.ins.resizable(False, False)
        fontStyle = tkFont.Font(family="Arial", size=30)
        fontt = tkFont.Font(family = "Arial", size = 14)
        fontb = tkFont.Font(family = "Arial", size = 20)
        fontO = tkFont.Font(family = "Arial", size = 12)
        fontO.configure(underline = True)
        gtr_maj = AudioSegment.from_file(file = "GTR_GMajor.wav",  
                                  format = "wav")
        gtr_min = AudioSegment.from_file(file = "GTR_Gminor.wav",  
                                          format = "wav")
        bass_maj = AudioSegment.from_file(file = "BASS_GMajor.wav",  
                                          format = "wav")
        bass_min = AudioSegment.from_file(file = "BASS_Gminor.wav",  
                                          format = "wav")
        piano_maj = AudioSegment.from_file(file = "PIANO_GMajor.wav",  
                                          format = "wav")
        piano_min = AudioSegment.from_file(file = "PIANO_Gminor.wav",  
                                          format = "wav")
        def audiosegment_to_numpy(audio_segment):
            samples = np.array(audio_segment.get_array_of_samples())
            return samples

        def G_mayor():
            def play_audio():
                playsound("GTR_GMajor.wav")
                
            thread = threading.Thread(target=play_audio)
            thread.start()
            chord_samples = audiosegment_to_numpy(gtr_maj)
            time = np.linspace(0, len(chord_samples) / gtr_maj.frame_rate, num=len(chord_samples))
            fft_result = np.fft.fft(chord_samples)
            fft_freqs = np.fft.fftfreq(len(fft_result), 1 / gtr_maj.frame_rate)
            X.append(fft_freqs)
            Y.append(np.abs(fft_result))


        def G_menor():
            def play_audio():
                playsound("GTR_Gminor.wav")
            thread = threading.Thread(target=play_audio)
            thread.start()
            chord_samples = audiosegment_to_numpy(gtr_min)
            time = np.linspace(0, len(chord_samples) / gtr_min.frame_rate, num=len(chord_samples))
            fft_result = np.fft.fft(chord_samples)
            fft_freqs = np.fft.fftfreq(len(fft_result), 1 / gtr_min.frame_rate)
            X.append(fft_freqs)
            Y.append(np.abs(fft_result))


        def P_mayor():
            def play_audio():
                playsound("PIANO_GMajor.wav")
            thread = threading.Thread(target=play_audio)
            thread.start()
            chord_samples = audiosegment_to_numpy(piano_maj)
            time = np.linspace(0, len(chord_samples) / piano_maj.frame_rate, num=len(chord_samples))
            fft_result = np.fft.fft(chord_samples)
            fft_freqs = np.fft.fftfreq(len(fft_result), 1 / piano_maj.frame_rate)
            X.append(fft_freqs)
            Y.append(np.abs(fft_result))



        def P_menor():
            def play_audio():
                playsound("PIANO_Gminor.wav")
            thread = threading.Thread(target=play_audio)
            thread.start()
            chord_samples = audiosegment_to_numpy(piano_min)
            time = np.linspace(0, len(chord_samples) / piano_min.frame_rate, num=len(chord_samples))
            fft_result = np.fft.fft(chord_samples)
            fft_freqs = np.fft.fftfreq(len(fft_result), 1 / piano_min.frame_rate)
            X.append(fft_freqs)
            Y.append(np.abs(fft_result))

        def exit(self):
            self.destroy()
            Main.aplic()



        menu_bottom = tk.Frame(self.ins ,bg = "#4a657a", height = 450)
        menu_bottom.pack(side = "bottom", fill = "x")

        label_G = tk.Label(menu_bottom, text="Guitarra", bg="#4a657a", fg="white", font = ('Arial', 24))
        label_G.place(x=295 , y = 150)  # Expande el label horizontalmente y agrega espacio debajo

        # Crear los botones dentro del mismo Frame y alinearlos al borde del Label
        button1_G = tk.Button(menu_bottom, text="Mayor", font = ('Arial', 18), command = lambda: G_mayor())
        button2_G = tk.Button(menu_bottom, text="Menor", font = ('Arial', 18), command = lambda: G_menor())

        # Colocar los botones alineados en el main_frame
        button1_G.place(x = 250, y = 200)  # Botón izquierdo con margen
        button2_G.place(x = 375, y = 200)


        label_P = tk.Label(menu_bottom, text="Piano", bg="#4a657a", fg="white", font = ('Arial', 24))
        label_P.place(x=1115 , y = 150)  # Expande el label horizontalmente y agrega espacio debajo

        # Crear los botones dentro del mismo Frame y alinearlos al borde del Label
        button1_P = tk.Button(menu_bottom, text="Mayor", font = ('Arial', 18), command = lambda: P_mayor())
        button2_P = tk.Button(menu_bottom, text="Menor", font = ('Arial', 18), command = lambda: P_menor())

        # Colocar los botones alineados en el main_frame
        button1_P.place(x = 1050, y = 200)  # Botón izquierdo con margen
        button2_P.place(x = 1175, y = 200)

        # Crear el botón con la imagen
        boton_imagen = tk.Button(menu_bottom, text = "Regresar", font = ('Arial', 18), command= lambda: exit(self.ins))
        boton_imagen.place(x = 700, y = 300)

        def animate(i):
            global X, Y
            if len(X) > 1:
                X = X[1:]
                Y = Y[1:]
            ax.clear()
            if len(X) > 0:
                ax.plot(X[0][0:3000], Y[0][0:3000])
            else:
                ax.plot(0,0)

        CA = FigureCanvasTkAgg(fig, master=self.ins)
        CA.get_tk_widget().place(x = 0, y = 10)
        ani = animation.FuncAnimation(fig, animate, interval = 100)
        ani = animation.FuncAnimation(fig, animate)
        self.ins.update()

        self.ins.mainloop()




