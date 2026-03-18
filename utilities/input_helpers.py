# =========================
# vraag hulpfuncties v0.1
# =========================

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
        invoer = input(
            vraag + " (Enter = overslaan of standaardwaarde): ").lower()
        if invoer == "":
            return None
        if invoer.isdigit():
            return invoer
        print("Ongeldige invoer.")


def vraag_tekst(vraag):
    while True:
        invoer = input(vraag).strip()
        if invoer == "":
            return None
        return invoer


def vraag_afkorting():
    while True:
        afkorting = input(
            "Wat is je naamafkorting? (bijv. CMA, Enter = FCW (Feig_config_Wizard)): ").strip().lower()
        if afkorting == "":
            return "fcw"
        if not afkorting.isalpha():
            print("Gebruik alleen letters.")
            continue
        if len(afkorting) > 3:
            print("Maximaal 3 tekens.")
            continue
        return afkorting


def vraag_projectnummer():
    while True:
        projectnummer = input(
            "Wat is het projectnummer? (Enter = leeg laten, alleen cijfers): ").strip()
        if projectnummer == "":
            return ""
        if not projectnummer.isdigit():
            print(" Alleen cijfers toegestaan.")
            continue
        if len(projectnummer) > 7:
            print(" Maximaal 7 cijfers.")
            continue
        return projectnummer


def vraag_bestandsnaam():
    verboden = r'<>:"/\\|?*'
    naam = input("Bestandsnaam (Enter = parameters): ").strip()
    if naam == "":
        naam = "parameters"
    for teken in verboden:
        naam = naam.replace(teken, "")
    return naam
