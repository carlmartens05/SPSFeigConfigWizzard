# imports
from ..input_helpers import *
from .keuzemenu.keuzemenu_sg import *


# ======================
# Speedgates v0.3
# ======================

def sg_menu(config):
    sg_plc = input(
        "Wordt de speedgate aangestuurd door een PLC (y/n)? plc maar geen open/dicht/stop? kies nee  ").lower()

    if sg_plc == "y":
        config.hoofd_parameter.extend(
            [("0501", "0101"), ("0502", "0401"), ("0503", "0701")])
        config.sub_parameter.extend(
            [("0522", "1"), ("0010", "0"), ("0011", "0"), ("0012", "0"), ("08ba", "4"), ("0890", "0")])

        print("standaard parameters voor een PLC sturing toegevoegd. ")

        if vraag_ja_nee("wil je alle menu's doorlopen? of wil je kiezen welke menu's ingesteld moeten worden? kiezen = n, alles = y "):
            alle_menus_sg_plc(config, "sg")
        else:
            keuzemenu_menus_sg_plc(config, "sg")
        return True

    elif sg_plc == "n":
        if vraag_ja_nee("wil je alle menu's doorlopen? of wil je kiezen welke menu's ingesteld moeten worden? kiezen = n, alles = y "):
            alle_menus_sg_standalone(config, "sg")
        else:
            keuzemenu_menus_sg_standalone(config, "sg")
        return True

    elif sg_plc == "terug":
        return False

    else:
        print("Ongeldige invoer, probeer opnieuw.")
