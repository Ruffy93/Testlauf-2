import tkinter as tk
import pygame
import os

pygame.mixer.init()

def play_sound(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    else:
        print(f"Datei nicht gefunden: {file}")

root = tk.Tk()
root.title("Mein Soundboard")
root.geometry("300x300")

sounds = [
    ("Nothing", "NoThing.mp3"),
    ("K-Wölfe", "Kontra_K-Wölfe.mp3"),
    ("Halt Stop", "Halt stop jetzt rede ich!.mp3"),
    ("Jigsaw", "Jigsaw laugh.mp3"),
    ("oh Shit!", "oh shit not Good!.mp3"),
    ("Rick Oh No", "RickGrime.mp3"),
    ("This is Bullshit", "this is bullshit.mp3")
     ]

for label, file in sounds:
    tk.Button(root, text=label, command=lambda f=file: play_sound(f), height=2, width=10).pack(pady=5)

tk.Button(root, text="Stop", command=pygame.mixer.music.stop, height=2, width=20, fg="red").pack(pady=10)
root.mainloop()