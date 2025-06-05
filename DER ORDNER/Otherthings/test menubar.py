import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

root = tk.Tk()
root.title("Soundboard mit Speicherfunktion")
root.geometry("400x500")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Sound hinzufügen")
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=filemenu)
root.config(menu=menubar)

root.mainloop()