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
import Main

t = 0
Y = 0
G = [0]
T = [0]
fft_r = []
fft_f = []

fig, ax = plt.subplots(figsize=(13.9, 4))
ln, = ax.plot([], [])

fig2, ax2 = plt.subplots(figsize=(13.9, 4))


class basico:
    def __init__(self):
        def sine_wave(frequency, amplitude ,duration = 1, sample_rate=44100):
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            wave = amplitude * np.sin(2 * np.pi * frequency * t)
            # Asegurarse de que los datos estén en el rango de -32767 a 32767 para int16
            wave = wave.astype(np.int16)
            return wave

        def sine_graph(f,a,t):
            onda = a*np.sin(np.deg2rad(2*np.pi**2*f*t))
            return onda

        def create_audio_segment(wave, sample_rate=44100):
            audio_segment = AudioSegment(
                wave.tobytes(),
                frame_rate=sample_rate,
                sample_width=wave.dtype.itemsize,
                channels=1
            )
            return audio_segment


        def generate_chord(frecuencias, amplitudes):

            # Generar las ondas y crear segmentos de audio
            #notes = [create_audio_segment(sine_wave(f)) for f in frecuencias]
            notes = [create_audio_segment(sine_wave(f, a)) for f, a in zip(frecuencias, amplitudes)]

            if len(frecuencias) > 1:
                note_b = notes[0]
                for i in range(1, len(notes)):
                    note_b = note_b.overlay(notes[i])
                return note_b
            else:
                return notes[0]


        def exit(self):
            self.destroy()
            Main.aplic()


        self.men = Tk()
        w, h = self.men.winfo_screenwidth(), self.men.winfo_screenheight()
        self.men.geometry("%dx%d+0+0" % (w, h))
        self.men.resizable(False, False)
        


    
        fontStyle = tkFont.Font(family="Helvetica", size=30)
        fontt = tkFont.Font(family = "Helvetica", size = 14)
        fontb = tkFont.Font(family = "Helvetica", size = 20)
        fontO = tkFont.Font(family = "Helvetica", size = 12)
        fontO.configure(underline = True)

        menu_lateral = tk.Frame(self.men, bg='#4a657a', width=200)
        menu_lateral.pack(side="right", fill="y")

        label_amplitud_1 = tk.Label(menu_lateral, text="Amplitud 1", bg='#4a657a', fg="white", font=("Arial", 14))
        label_amplitud_1.pack(pady=15)
        slider_amplitud_1 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_amplitud_1.pack(padx=20, pady=5)

        # Slider de "Frecuencia"
        label_frecuencia_1 = tk.Label(menu_lateral, text="Frecuencia 1", bg='#4a657a', fg="white", font=("Arial", 14))
        label_frecuencia_1.pack(pady=15)
        slider_frecuencia_1 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_frecuencia_1.pack(padx=20, pady=5)

        label_amplitud_2 = tk.Label(menu_lateral, text="Amplitud 2", bg='#4a657a', fg="white", font=("Arial", 14))
        label_amplitud_2.pack(pady=15)
        slider_amplitud_2 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_amplitud_2.pack(padx=20, pady=10)

        # Slider de "Frecuencia"
        label_frecuencia_2 = tk.Label(menu_lateral, text="Frecuencia 2", bg='#4a657a', fg="white", font=("Arial", 14))
        label_frecuencia_2.pack(pady=15)
        slider_frecuencia_2 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_frecuencia_2.pack(padx=20, pady=10)

        label_amplitud_3 = tk.Label(menu_lateral, text="Amplitud 3", bg='#4a657a', fg="white", font=("Arial", 14))
        label_amplitud_3.pack(pady=15)
        slider_amplitud_3 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_amplitud_3.pack(padx=20, pady=15)

        # Slider de "Frecuencia"
        label_frecuencia_3 = tk.Label(menu_lateral, text="Frecuencia 3", bg='#4a657a', fg="white", font=("Arial", 14))
        label_frecuencia_3.pack(pady=15)
        slider_frecuencia_3 = tk.Scale(menu_lateral, from_=0, to=500, orient="horizontal")
        slider_frecuencia_3.pack(padx=20, pady=15)

        #Button de "Regresar"
        Btn_exit = tk.Button(menu_lateral, text="Regresar", font=("Arial", 14), command= lambda: exit(self.men))
        Btn_exit.pack(pady=35)


        def audiosegment_to_numpy(audio_segment):
            samples = np.array(audio_segment.get_array_of_samples())
            return samples

        def animate(i):
            global T, G
            #Se obtiene loa valores que se van a graficar
            if len(T) > 30:
                T = T[1:]
                G = G[1:]
            #Se grafican
            ln.set_data(T,G)
            ax.set_xlim(min(T)-3*pi/480, max(T)+3*pi/480)
            ax.set_ylim(min(G)-20 , max(G)+10)
            return ln
            

        def animate2(i):
            global fft_f, fft_r
            #Se obtiene loa valores que se van a graficar
            if len(fft_r) > 2:
                fft_r = fft_r[1:]
                fft_f = fft_f[1:]
            #Se grafican
            ax2.clear()
            ax2.set_xlim(0, 600)
            if len(fft_r) > 0:
                ax2.plot(fft_f[-1], fft_r[-1])
            else:
                ax2.plot(0,0)


        
        CA = FigureCanvasTkAgg(fig, master=self.men)
        CA.get_tk_widget().place(x = 0, y = 10)

        ani = animation.FuncAnimation(fig, animate, interval = 100)

        CA2 = FigureCanvasTkAgg(fig2, master=self.men)
        CA2.get_tk_widget().place(x = 0, y = 425)

        ani2 = animation.FuncAnimation(fig2, animate2, interval = 100)

        self.men.update()

        
        #Se invoca a la animación
        ani = animation.FuncAnimation(fig, animate)
        #ani2 = animation.FuncAnimation(fig2, animate)


        def update_gui():
            global t, fft_f, fft_r
            t = t + pi/480
            

            ampl_1 = slider_amplitud_1.get()
            frec_1 = slider_frecuencia_1.get()
            ampl_2 = slider_amplitud_2.get()
            frec_2 = slider_frecuencia_2.get()
            ampl_3 = slider_amplitud_3.get()
            frec_3 = slider_frecuencia_3.get()

            frecuencias = []
            amplitudes = []
            if (ampl_1 > 0 and frec_1 > 0):
                frecuencias.append(frec_1)
                amplitudes.append(ampl_1)
            if (ampl_2 > 0 and frec_2 > 0):
                frecuencias.append(frec_2)
                amplitudes.append(ampl_2)
            if (ampl_3 > 0 and frec_3 > 0):
                frecuencias.append(frec_3)
                amplitudes.append(ampl_3)

            if len(frecuencias) > 0 and len(amplitudes) > 0:
                chord = generate_chord(frecuencias, amplitudes)
                chord_samples = audiosegment_to_numpy(chord)
                time = np.linspace(0, len(chord_samples) / chord.frame_rate, num=len(chord_samples))
                fft_result = np.abs(np.fft.fft(chord_samples))
                fft_freqs = np.fft.fftfreq(len(fft_result), 1 / chord.frame_rate)
                fft_f.append(fft_freqs)
                fft_r.append(fft_result)

            sine_1 = sine_graph(frec_1, ampl_1, t)
            sine_2 = sine_graph(frec_2, ampl_2, t)
            sine_3 = sine_graph(frec_3, ampl_3, t)

            sine_total = sine_1+sine_2+sine_3
            #print(G)
            G.append(sine_total)
            T.append(t)




            self.men.after(int(100), update_gui)

        
        update_gui()
        self.men.mainloop()

