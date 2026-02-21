from datetime import date
import os

parameters = []


# ======================
# Helper functies
# ======================

def vraag_ja_nee(vraag):
    while True:
        keuze = input(vraag).lower()
        if keuze in ("y", "n"):
            return keuze == "y"
        if keuze == "terug":
            return None
        print("Ongeldige invoer.")


def vraag_getal(vraag):
    while True:
        invoer = input(vraag + " (Enter = overslaan): ").lower()
        if invoer == "":
            return None
        if invoer.isdigit():
            return invoer
        print("Ongeldige invoer.")


# ======================
# Hoofd wizard
# ======================

def wizard():
    global parameters
    parameters.clear()

    while True:
        afsluiting = input(
            "Op welk soort afsluiting zit de besturing aangesloten? (as/sg/ohd) "
        ).lower()

        if afsluiting == "as" and as_menu():
            break
        elif afsluiting == "sg" and sg_menu():
            break
        elif afsluiting == "ohd" and ohd_menu():
            break
        else:
            print("Ongeldige invoer, probeer opnieuw.")


# ======================
# Slagbomen
# ======================

def as_menu():
    while True:
        keuze = input(
            "Wordt de slagboom aangestuurd door een PLC of standalone (plc/standalone)? "
        ).lower()

        if keuze == "plc":
            print("PLC modus nog niet geïmplementeerd.")
            return False
        elif keuze == "standalone":
            return as_standalone_menu()
        elif keuze == "terug":
            return False
        else:
            print("Ongeldige invoer.")


def as_standalone_menu():
    keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        auto_sluittijd_menu("as")

    keuze = vraag_ja_nee("Zelftest instellen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        zelftest_menu("as")

    keuze = vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        verkeerslichten_menu("as")

    return True


# ======================
# Speedgates
# ======================

def sg_menu():
    while True:
        sg_plc = input(
            "Wordt de speedgate aangestuurd door een PLC (y/n)? "
        ).lower()

        if sg_plc == "y":
            parameters.extend([
                ("0501", "0101"),
                ("0502", "0401"),
                ("0522", "1"),
                ("0503", "0701"),
                ("0010", "0"),
                ("0011", "0"),
                ("0012", "0"),
                ("08BA", "4"),
                ("0890", "0"),
            ])
            return True

        elif sg_plc == "n":
            keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
            if keuze is None:
                return False
            if keuze:
                auto_sluittijd_menu("sg")
            return True

        elif sg_plc == "terug":
            return False
        else:
            print("Ongeldige invoer.")


# ======================
# Overheaddeuren
# ======================

def ohd_menu():
    keuze = vraag_ja_nee("Motor instellingen aanpassen? (y/n) ")
    if keuze:
        motor_instelling_menu()

    keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
    if keuze:
        auto_sluittijd_menu("ohd")

    keuze = vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) ")
    if keuze:
        verkeerslichten_menu("ohd")

    return True


# ======================
# Submenu's
# ======================

def auto_sluittijd_menu(type_afsluiting):
    if type_afsluiting == "as":
        waarde = vraag_getal("Auto sluittijd geheel open (P.010)")
        if waarde is not None:
            parameters.append(("0010", waarde))

    if type_afsluiting == "sg":
        waarde = vraag_getal("Auto sluittijd half open (P.011)")
        if waarde is not None:
            parameters.append(("0011", waarde))

    if type_afsluiting in ("sg", "ohd"):
        waarde = vraag_getal("Geforceerde sluittijd (P.012)")
        if waarde is not None:
            parameters.append(("0012", waarde))


def motor_instelling_menu():
    freq = vraag_getal("Frequentie motor (P.100 Hz)")
    if freq is not None:
        parameters.append(("0100", freq))

    amp = vraag_getal("Amperage motor (P.101) laat de punt weg dus 2.1A = 21")
    if amp is not None:
        parameters.append(("0101", amp))

    cosphi = vraag_getal("Cos phi motor (P.102)")
    if cosphi is not None:
        parameters.append(("0102", cosphi))

    volt = vraag_getal("Voltage motor (P.103)")
    if volt is not None:
        parameters.append(("0103", volt))


def zelftest_menu(type_afsluiting):
    if type_afsluiting in ("as", "ohd"):
        inputnr = vraag_getal("Welke input wil je zelftesten? output 15 wordt standaard gebruikt als testoutput.")
        if inputnr:
            parameters.append((f"05{inputnr}A", "1"))
            parameters.append(("070f", "2501"))
            print(f"Input {inputnr} wordt getest.")


def verkeerslichten_menu(type_afsluiting):
    print("Standaard verkeerslichtsturing toegevoegd. K1 voor VKL buiten en K2 voor VKL binnen. rood op NC en groen op NO.")

    if type_afsluiting == "as":
        parameters.extend([
            ("0701", "1210"),
            ("0702", "1201"),
            ("0716", "2"),
            ("0719", "5"),
            ("071f", "19"),
            ("0726", "0"),
            ("0729", "5"),
            ("072f", "19"),
        ])

    elif type_afsluiting == "ohd":
        parameters.extend([
            ("0701", "1210"),
            ("0702", "1201"),
            ("0716", "2"),
            ("0719", "2"),
            ("071f", "19"),
            ("0726", "0"),
            ("0729", "2"),
            ("072f", "19"),
        ])


# ======================
# XML generatie
# ======================

def vraag_bestandsnaam():
    naam = input("Bestandsnaam (Enter = parameters): ").strip()
    return naam or "parameters"


def maak_xml(bestandsnaam):
    vandaag = date.today().strftime("%Y-%m-%d")

    xml = [
        '<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>',
        f'<parameterlist date="{vandaag}">'
    ]

    for code, waarde in parameters:
        xml.append(f'    <parameter ncode="{code}" pdef="{waarde}" />')

    xml.append('</parameterlist>')

    pad = os.path.join(os.path.expanduser("~"), "Downloads",
                       f"{bestandsnaam}_{vandaag}.xml")

    with open(pad, "w", encoding="iso-8859-1") as f:
        f.write("\n".join(xml))

    print(f"\n✅ XML opgeslagen: {pad}")


# ======================
# Start programma
# ======================

print("=== Config Wizard Feig besturingen V1.0 CMA 2026 ===\n")

if __name__ == "__main__":
    wizard()
    if parameters:
        naam = vraag_bestandsnaam()
        maak_xml(naam)