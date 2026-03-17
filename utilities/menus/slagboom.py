# imports
from ..input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from .submenus.submenus import *

# ======================
# Slagbomen
# ======================


def as_menu(config):
    while True:
        waarde = vraag_getal(
            'welk profiel heeft de slagboom volgens de sticker op de besturing? (zie de handleiding van Bormet voor meer info)  ')
        if waarde is not None:
            config.hoofd_parameter.append(("0991", waarde))

        keuze = input("Wordt de slagboom aangestuurd door een PLC of standalone (PLC = open/dicht/stop, plc maar geen open/dicht/stop? kies standalone.) (plc/standalone)?   ").lower()

        if keuze == "plc":
            return as_plc_menu(config)
        elif keuze == "standalone":
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

    if vraag_ja_nee("Zelftest instellen? (y/n) "):
        zelftest_menu(config, "as")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        BMI_menu(config)

    if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
        onderhouds_interval(config, "as")

    return True


def as_standalone_menu(config):
    if vraag_ja_nee("Zelftest instellen? (y/n)  "):
        zelftest_menu(config, "as")

    if vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) "):
        verkeerslichten_menu(config, "as")
        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
                auto_sluittijd_menu(config, "as")
    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
            auto_sluittijd_menu(config, "as")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        BMI_menu(config)

    if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
        onderhouds_interval(config, "as")

    return True
