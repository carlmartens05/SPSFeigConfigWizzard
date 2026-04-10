# imports
from ..input_helpers import *
from ..parameter_logic import *
from .keuzemenu.keuzemenu_ohd import *


# ======================
# Overheaddeuren v0.3
# ======================


def ohd_menu(config):
    ohd_plc = input(
        "Wordt de overheaddeur aangestuurd door een PLC (y/n)? plc maar geen open/dicht/stop? kies nee  ")
    if ohd_plc == "n":
        if vraag_ja_nee("wil je alle menu's doorlopen? of wil je kiezen welke menu's ingesteld moeten worden? kiezen = n, alles = y "):
            alle_menus_ohd_standalone(config, "ohd")
        else:
            keuzemenu_menus_ohd_standalone(config, "ohd")
    if ohd_plc == "y":
        ohd_plc_menu(config, "ohd")
    return True


def ohd_plc_menu(config):
    config.hoofd_parameter.extend(
        [("0501", "0101"), ("0502", "0401"), ("0503", "0701"), ("0505", "1403"), ("0701", "0101"), ("0702", "0201")])
    config.sub_parameter.extend(
        [("0522", "1"), ("0010", "0"), ("0011", "0"), ("0012", "0")])
    print("standaard parameters voor een PLC sturing toegevoegd. ")
