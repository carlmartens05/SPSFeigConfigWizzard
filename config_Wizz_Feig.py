from datetime import date
import os

parameters = []

def wizard():
    """
    Volledige wizard met loop en sub-menu's.
     - Hoofdmenu: keuze tussen AS, SG, OHD
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

# --- Sub-menu's voor specifieke afsluitingen ---
# - - - slagbomen - - - 

def as_menu():
    """
    Submenu voor slagboom.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        as_PLC = input("Wordt de slagboom aangestuurd door een PLC  of is deze standalone (PLC/standalone)? (typ 'terug' om terug te gaan) ").lower()
        if as_PLC == "plc":
            return as_PLC_menu()  # Ga naar sub-menu PLC keuzes
        elif as_PLC == "standalone":
            return as_standalone_menu()  # Ga naar sub-menu standalone keuzes
        elif as_PLC == "terug":
            print("Terug naar hoofdmenu...")
            return False  # terug naar hoofdmenu
        else:
            print("Moet nog gebouwd worden, gebruik je verstand!")
            input("Druk op Enter om af te sluiten.")
            return False  # terug naar hoofdmenu

def as_PLC_menu():
    """
    Submenu voor slagboom met PLC.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        print("Moet nog gebouwd worden, gebruik je verstand! as_PLC_menu")
        input("Druk op Enter om af te sluiten.")
        return False  # terug naar hoofdmenu

def as_standalone_menu():
    """
    Submenu voor slagboom met PLC.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        as_auto_sluittijd = input("wil je de autosluittijd aanpassen (y/n)? (typ 'terug' om terug te gaan) ").lower()
        if as_auto_sluittijd == "y":
            return auto_sluittijd_menu()  # Ga naar sub-menu autosluittijd keuzes
            return True  # klaar, doorgaan
        elif as_auto_sluittijd == "n":
            return False  # klaar, naar hoofdmenu
        elif as_auto_sluittijd == "terug":
            print("Terug naar hoofdmenu...")
            return False  # terug naar hoofdmenu

# - - - speedgates - - -

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
            as_auto_sluittijd = input("wil je de autosluittijd aanpassen (y/n)? (typ 'terug' om terug te gaan) ").lower()
            if as_auto_sluittijd == "y":
                return auto_sluittijd_menu()  # Ga naar sub-menu autosluittijd keuzes
            elif as_auto_sluittijd == "n":
                return False  # klaar, naar hoofdmenu
            elif as_auto_sluittijd == "terug":
                print("Terug naar hoofdmenu...")
                return False  # terug naar hoofdmenu
        elif sg_PLC == "terug":
            print("Terug naar hoofdmenu...")
            return False  # terug naar hoofdmenu
        else:
            print("Ongeldige invoer, probeer opnieuw.")

# - - - Overheaddeur - - -

def ohd_menu():
    """
    Submenu voor overheaddeur.
    Geeft True terug als parameters zijn toegevoegd, False als gebruiker terug wilt.
    """
    while True:
        OHD_motor_instellingen = input("wil je de motor instellingen aanpassen (y/n)? (typ 'terug' om terug te gaan) ").lower()
        if OHD_motor_instellingen == "y":
            motor_instelling_menu()  # Ga naar sub-menu motor instellingen keuzes
            auto_sluittijd_input = input("wil je de autosluittijd aanpassen (y/n)? (typ 'terug' om terug te gaan) ").lower()
            if auto_sluittijd_input == "y":
                auto_sluittijd_menu()  # Ga naar sub-menu autosluittijd keuzes
            return True
        elif OHD_motor_instellingen == "n":
            auto_sluittijd_input = input("wil je de autosluittijd aanpassen (y/n)? (typ 'terug' om terug te gaan) ").lower()
            if auto_sluittijd_input == "y":
                auto_sluittijd_menu()  # Ga naar sub-menu autosluittijd keuzes
            else:
                return False  # klaar, naar hoofdmenu
        elif OHD_motor_instellingen == "terug":
            print("Terug naar hoofdmenu...")
            return False  # terug naar hoofdmenu


# submenu's voor specifieke keuzes


def auto_sluittijd_menu():
    """Submenu voor auto sluittijden."""
    
    # P.010
    while True:
        invoer = input("Auto sluittijd geheel open (p.010, gebruiken bij slagbomen, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 200:
            parameters.append(("0010", invoer))
            break
        else:
            print("Ongeldige invoer.")

    # P.011
    while True:
        invoer = input("Auto sluittijd half open (p.011, gebruiken bij speedgates, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 200:
            parameters.append(("0011", invoer))
            break
        else:
            print("Ongeldige invoer.")

    # P.012
    while True:
        invoer = input("Geforceerde sluittijd (p.012, gebruiken bij speedgates en overheaddeuren,  Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 200:
            parameters.append(("0012", invoer))
            break
        else:
            print("Ongeldige invoer.")

    return True # klaar, doorgaan

def motor_instelling_menu():
    """Submenu voor motor instellingen."""

    # Frequentie
    while True:
        invoer = input("Frequentie motor (p.100, in Hz, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 200:
            parameters.append(("0100", invoer))
            break
        else:
            print("Ongeldige invoer.")

    # Amperage
    while True:
        invoer = input("Amperage motor (p.101, in Ampere, laat de punt weg, dus 2.1A = 21, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 45:
            parameters.append(("0101", invoer))
            break
        else:
            print("Ongeldige invoer.")

    # Cos phi
    while True:
        invoer = input("Cos phi motor (p.102, in graden, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit() and 0 <= int(invoer) <= 200:
            parameters.append(("0102", invoer))
            break
        else:
            print("Ongeldige invoer.")

    # Voltage
    while True:
        invoer = input("Voltage motor (p.103, in Volt, Enter = overslaan, 'terug' = menu): ").lower()
        if invoer == "terug":
            return False
        elif invoer == "":
            break
        elif invoer.isdigit():
            parameters.append(("0103", invoer))
            break
        else:
            print("Ongeldige invoer.")

    return True # klaar, doorgaan


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