# ============================
# subemenu's v0.2
# ============================

# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code

# ======================
# Submenu's import
# ======================

# onderhouds intrval
from .onderhouds_interval import onderhouds_interval_menu
# auto sluittijd
from .auto_sluittijd import auto_sluittijd_menu
# motor instellingen
from .motor_instellingen import motor_instelling_menu
# zelftest
from .zelftest import zelftest_menu
# verkeerslichten
from .verkeerslichten import verkeerslichten_menu
# node id
from .node_id import node_id_menu
# heling baan regeling
from .heling_baan_regeling import heling_baan_regeling_menu
# loopsnelheden
from .loopsnelheden import loopsnelheden_OHD_menu
# BMI
from .bmi import BMI_menu

# ============================
# keuzemenu voor subemenu's
# ============================

# == slagbomen ==

# === as plc's ===


def keuzemenu_menus_as_plc(config, afsluiting):
    from ..slagboom import as_plc_menu
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? ===== 
                1 = zelftest 
                2 = node id voor PXS Feig koppeling 
                3 = BMI instellingen
                4 = onderhouds-teller
                klaar = klaar met configureren en maak bestand aan. 
                terug = terug naar AS PLC menu. 
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "2":
            node_id_menu(config)
        elif submenu_keuze == "3":
            BMI_menu(config)
        elif submenu_keuze == "4":
            onderhouds_interval_menu(config, "as")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            return as_plc_menu(config)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_as_plc(config, afsluiting):
    if vraag_ja_nee("Zelftest instellen? (y/n) "):
        zelftest_menu(config, "as")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        BMI_menu(config)

    if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
        onderhouds_interval_menu(config, "as")
    return True

# === as standalone


def keuzemenu_menus_as_standalone(config, afsluiting):
    from ..slagboom import as_standalone_menu
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? ===== 
                1 = autosluittijd 
                2 = zelftest 
                3 = verkeerslichten 
                4 = node id voor PXS Feig koppeling 
                5 = hellingbaan regeling
                6 = BMI instellingen
                7 = onderhouds-teller
                klaar = klaar met configureren en maak bestand aan. 
                terug = terug naar adv. menu. 
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            auto_sluittijd_menu(config, afsluiting)
        elif submenu_keuze == "2":
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "3":
            verkeerslichten_menu(config, afsluiting)
        elif submenu_keuze == "4":
            node_id_menu(config)
        elif submenu_keuze == "5":
            heling_baan_regeling_menu(config)
        elif submenu_keuze == "6":
            BMI_menu(config)
        elif submenu_keuze == "7":
            onderhouds_interval_menu(config, "as")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            return as_standalone_menu(config)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_as_standalone(config, afsluiting):
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
        onderhouds_interval_menu(config, "as")
    return True
