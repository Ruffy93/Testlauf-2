import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os
import json

pygame.mixer.init()

SAVE_FILE = "sounds.json"

root = tk.Tk()
root.title("Soundboard")
root.geometry("400x500")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

sound_buttons = []  # Liste von {"label": ..., "filepath": ..., "button": tk.Button}

def play_sound(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    else:
        messagebox.showerror("Fehler", f"Datei nicht gefunden:\n{file}")

def stop_sound():
    pygame.mixer.music.stop()

def save_sounds():
    # Nur label und filepath speichern
    save_data = [{"label": s["label"], "filepath": s["filepath"]} for s in sound_buttons]
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=2)

def remove_sound(entry):
    # Button entfernen
    entry["button"].destroy()
    # Aus Liste entfernen
    sound_buttons.remove(entry)
    # Speicher aktualisieren
    save_sounds()

def show_context_menu(event, entry):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Entfernen", command=lambda: remove_sound(entry))
    menu.tk_popup(event.x_root, event.y_root)

def add_button(label, filepath):
    entry = {"label": label, "filepath": filepath}
    btn = tk.Button(button_frame, text=label, width=30, height=2,
                    command=lambda f=filepath: play_sound(f))
    btn.pack(pady=5)
    btn.bind("<Button-3>", lambda event, e=entry: show_context_menu(event, e))  # Rechtsklick
    entry["button"] = btn
    sound_buttons.append(entry)

def add_sound():
    filetypes = [("Audio-Dateien", "*.wav *.mp3")]
    filepath = filedialog.askopenfilename(title="Sound auswählen", filetypes=filetypes)

    if filepath:
        label = os.path.basename(filepath)
        add_button(label, filepath)
        save_sounds()

def load_sounds():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
                for entry in saved:
                    if os.path.exists(entry["filepath"]):
                        add_button(entry["label"], entry["filepath"])
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte sounds.json nicht laden:\n{e}")

# Menü
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Sound hinzufügen", command=add_sound)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=filemenu)
root.config(menu=menubar)

# Stop-Button
stop_button = tk.Button(root, text="Stop", command=stop_sound, fg="red", height=2, width=30)
stop_button.pack(pady=10)

# Geladene Sounds anzeigen
load_sounds()

root.mainloop()