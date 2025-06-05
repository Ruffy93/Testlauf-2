Hersteller = "Mercedes"
Farbe = "Blau"
Türen = "3"
Größe = "Groß"
Kraftstoff = "Diesel"
Fahrzeug_Typ = "LKW"
Anzahl_Sitze = "2"
Baujahr = "2015"
Hubraum = "12.5"
Getriebe = "Automatic"
Maximale_Zuladung = "44"

print ("Ohne Variablentausch")
print (f"Farbe {Farbe}")
print (f"Hersteller {Hersteller}")
print (f"Türen {Türen}")
print (f"Größe {Größe}")
print (f"Kraftstoff {Kraftstoff}")
print (f"Fahrzeugtyp {Fahrzeug_Typ}")
print (f"Anzahl_Sitze {Anzahl_Sitze}")
print (f"Baujahr {Baujahr}")
print (f"Hubraum {Hubraum}")
print (f"Getriebe {Getriebe}")
print (f"Maximale_Zuladung {Maximale_Zuladung} Tonnen")


Farbe, Größe = Größe, Farbe

print ("Variable getauscht:")
print (f"Farbe {Farbe}")
print (f"Größe {Größe}")
