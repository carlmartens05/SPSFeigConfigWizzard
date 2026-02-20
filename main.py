from datetime import date
import os
parameters = []

print("=== Config Wizard Feig besturingen speedgate ===\n")

# Vraag 1: Automatische modus
PLC = input("wordt de speedgate aangestuurd door een PLC (y/n): ").lower()
if PLC == "y":
    parameters.append(("0501", "0101"))
    parameters.append(("0502", "0401"))
    parameters.append(("0522", "1"))
    parameters.append(("0503", "0701"))
    parameters.append(("0010", "0"))
    parameters.append(("0011", "0"))
    parameters.append(("0012", "0"))
    parameters.append(("08ba", "4"))
    parameters.append(("0890", "0"))

else:
    print("nog te bouwen, gebruik je verstand!")

# Vraag 2: Snelheid
while True:
    speed = input("Open snelheid (0-100): ")
    if speed.isdigit() and 0 <= int(speed) <= 100:
        parameters.append(("102", speed))
        break
    else:
        print("Ongeldige invoer. Kies 0 t/m 100.")

# Vraag 3: Veiligheidslus
loop = input("Veiligheidslus aanwezig? (ja/nee): ").lower()
parameters.append(("150", "ON" if loop == "ja" else "OFF"))

# Vraag 4: Alarm
alarm = input("Alarm bij geforceerd openen? (ja/nee): ").lower()
parameters.append(("200", "ON" if alarm == "ja" else "OFF"))


#vraag naar bestandsnaam
bestandsnaam_input = input("Hoe moet het bestand heten? (zonder .xml, Enter = 'parameters'): ").strip()
if bestandsnaam_input == "":
    bestandsnaam_input = "parameters"


# Datum genereren
vandaag = date.today().strftime("%Y-%m-%d")

# XML opbouwen
xml_lines = [
    '<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>',
    f'<parameterlist version="none" editor="CMA" serial="" date="{vandaag}">'
]

for ncode, waarde in parameters:
    xml_lines.append(f'    <parameter ncode="{ncode}" pdef="{waarde}" />')

xml_lines.append('</parameterlist>')

# Bestand schrijven
# --- Downloads map automatisch vinden ---
downloads_map = os.path.join(os.path.expanduser("~"), "Downloads")

# Bestandsnaam met datum
bestand_naam = f"{bestandsnaam_input}_{vandaag}.xml"
bestand_pad = os.path.join(downloads_map, bestand_naam)

# Bestand opslaan
with open(bestand_pad, "w", encoding="iso-8859-1") as file:
    file.write("\n".join(xml_lines))

print("\n✅ XML opgeslagen in:")
print(bestand_pad)
print("\nXML bestand succesvol aangemaakt en correct afgesloten.")
