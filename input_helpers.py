# ======================
# vraag hulpfuncties
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
