# imports
from ..input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from .keuzemenu.keuzemenu_as import *
# ======================
# Slagbomen v0.3
# ======================


def as_menu(config):
    while True:
        waarde = vraag_getal(
            'welk profiel heeft de slagboom volgens de sticker op de besturing? (zie de handleiding van Bormet voor meer info)  ')
        if waarde is not None:
            config.hoofd_parameter.append(("0991", waarde))

        keuze = input(
            "Wordt de slagboom aangestuurd door een PLC (y/n)? plc maar geen open/dicht/stop? kies nee  ").lower()

        if keuze == "y":
            return as_plc_menu(config)
        elif keuze == "n":
            return as_standalone_menu(config)
        elif keuze == "terug":
            return False
        else:
            print("Ongeldige invoer.")


def as_plc_menu(config):
    config.hoofd_parameter.extend(
        [("0505", "1401"), ("0701", "0101"), ("0702", "0201")])
    config.sub_parameter.extend(
        [("0010", "0"), ("002a", "0"), ("04b7", "0"), ("0890", "0")])
    print("standaard parameters voor een PLC sturing toegevoegd. ")

    if vraag_ja_nee("wil je alle menu's doorlopen? of wil je kiezen welke menu's ingesteld moeten worden? kiezen = n, alles = y "):
        alle_menus_as_plc(config, "as")
    else:
        keuzemenu_menus_as_plc(config, "as")
    return True


def as_standalone_menu(config):
    if vraag_ja_nee("wil je alle menu's doorlopen? of wil je kiezen welke menu's ingesteld moeten worden? kiezen = n, alles = y "):
        alle_menus_as_standalone(config, "as")
    else:
        keuzemenu_menus_as_standalone(config, "as")
    return True
