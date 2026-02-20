from datetime import date
import os

parameters = []

def wizard():
    """
    Volledige wizard met terug-optie.
    """
    while True:  # hoofdloop van wizard
        # --- Hoofdmenu ---
        afsluiting = input("Op welk soort afsluiting zit de besturing aangesloten? (as/sg/ohd) ").lower()

        if afsluiting == "as":
            # Ga naar sub-menu AS
            if not as_menu():
                continue  # gebruiker koos 'terug', ga opnieuw naar hoofdmenu
            break  # AS keuze voltooid, ga door naar bestandsnaam
            return  # stopt wizard
        elif afsluiting == "sg":
            # Ga naar sub-menu SG
            if not sg_menu():
                continue  # gebruiker koos 'terug', ga opnieuw naar hoofdmenu
            break  # SG keuze voltooid, ga door naar bestandsnaam
        elif afsluiting == "ohd":
             # Ga naar sub-menu OHD
            if not ohd_menu():
                continue  # gebruiker koos 'terug', ga opnieuw naar hoofdmenu
            break  # OHD keuze voltooid, ga door naar bestandsnaam
            return  # stopt wizard  
        else:
            print("Ongeldige invoer, probeer opnieuw.")

def as_menu():
    """
    Submenu voor slagboom.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        print("Moet nog gebouwd worden, gebruik je verstand!")
        input("Druk op Enter om af te sluiten.")
        return False  # terug naar hoofdmenu

def sg_menu():
    """
    Submenu voor Speedgate PLC keuzes.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        sg_PLC = input("Wordt de speedgate aangestuurd door een PLC (y/n)? (typ 'terug' om terug te gaan) ").lower()
        if sg_PLC == "y":
            # Voeg parameters toe
            parameters.append(("0501", "0101"))
            parameters.append(("0502", "0401"))
            parameters.append(("0522", "1"))
            parameters.append(("0503", "0701"))
            parameters.append(("0010", "0"))
            parameters.append(("0011", "0"))
            parameters.append(("0012", "0"))
            parameters.append(("08ba", "4"))
            parameters.append(("0890", "0"))
            return True  # klaar, doorgaan
        elif sg_PLC == "n":
            print("Moet nog gebouwd worden, gebruik je verstand!")
            input("Druk op Enter om af te sluiten.")
            return False
        elif sg_PLC == "terug":
            print("Terug naar hoofdmenu...")
            return False  # terug naar hoofdmenu
        else:
            print("Ongeldige invoer, probeer opnieuw.")

def ohd_menu():
    """
    Submenu voor slagboom.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        print("Moet nog gebouwd worden, gebruik je verstand!")
        input("Druk op Enter om af te sluiten.")
        return False  # terug naar hoofdmenu

def vraag_bestandsnaam():
    bestandsnaam_input = input(
        "Hoe moet het bestand heten? (de datum is al standaard toegevoegd)\n"
        "dit bestand wordt automatisch opgeslagen in je Downloads-map.\n"
        "(zonder .xml, Enter = 'parameters'): "
    ).strip()
    if bestandsnaam_input == "":
        bestandsnaam_input = "parameters"
    return bestandsnaam_input

def maak_xml(bestandsnaam_input):
    vandaag = date.today().strftime("%Y-%m-%d")

    xml_lines = [
        '<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>',
        f'<parameterlist version="none" editor="configwizardFeig" serial="" date="{vandaag}">'
    ]

    for ncode, waarde in parameters:
        xml_lines.append(f'    <parameter ncode="{ncode}" pdef="{waarde}" />')

    xml_lines.append('</parameterlist>')

    downloads_map = os.path.join(os.path.expanduser("~"), "Downloads")
    bestand_naam = f"{bestandsnaam_input}_{vandaag}.xml"
    bestand_pad = os.path.join(downloads_map, bestand_naam)

    with open(bestand_pad, "w", encoding="iso-8859-1") as file:
        file.write("\n".join(xml_lines))

    print("\n✅ XML opgeslagen in:")
    print(bestand_pad)
    print("\nXML bestand succesvol aangemaakt en correct afgesloten.")


# === Programma start hier ===
print("=== Config Wizard Feig besturingen V1.0 CMA 2026 ===\n")
if __name__ == "__main__":
    wizard()  # start wizard
    if parameters:  # alleen doorgaan als er parameters zijn toegevoegd
        bestandsnaam = vraag_bestandsnaam()
        maak_xml(bestandsnaam)