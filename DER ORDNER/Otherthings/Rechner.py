import tkinter as tk

def button_click(zeichen):
    aktueller_text = eingabe.get()
    eingabe.delete(0, tk.END)
    eingabe.insert(0, aktueller_text + zeichen)

def berechne():
    try:
        ergebnis = eval(eingabe.get())
        eingabe.delete(0, tk.END)
        eingabe.insert(0, str(ergebnis))
    except:
        eingabe.delete(0, tk.END)
        eingabe.insert(0, "Fehler")

def clear():
    eingabe.delete(0, tk.END)


fenster = tk.Tk()
fenster.title("BigMama Rechner")

eingabe = tk.Entry(fenster, width=20, font=("Arial", 16), borderwidth=3, relief="solid", justify="right")
eingabe.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (text, zeile, spalte) in buttons:
    if text == "=":
        tk.Button(fenster, text=text, width=5, height=2, command=berechne).grid(row=zeile, column=spalte)
    else:
        tk.Button(fenster, text=text, width=5, height=2, command=lambda z=text: button_click(z)).grid(row=zeile, column=spalte)

tk.Button(fenster, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

fenster.mainloop()