# ============================
# subemenu's v0.6
# ============================

# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code


# ============================
# keuzemenu voor subemenu's
# ============================

# == speedgate ==


# == overheaddeur ==

# === ohd standalone ===


def keuzemenu_menus_ohd_standalone(config, afsluiting):
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? =====
                1 = autosluittijd
                2 = motor instellingen
                3 = zelftest
                4 = verkeerslichten
                5 = node id voor PXS Feig koppeling
                6 = hellingbaan regeling
                7 = BMI instellingen
                8 = loopsnelheden instellen
                9 = boost instellingen
                10 = positioneringssysteem
                klaar = klaar met configureren en maak bestand aan.
                terug = terug naar adv. menu.
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            from .auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, afsluiting)
        elif submenu_keuze == "2":
            from .motor_instellingen import motor_instelling_menu
            motor_instelling_menu(config)
        elif submenu_keuze == "3":
            from .zelftest import zelftest_menu
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "4":
            from .verkeerslichten import verkeerslichten_menu
            verkeerslichten_menu(config, afsluiting)
        elif submenu_keuze == "5":
            from .node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "6":
            from .heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        elif submenu_keuze == "7":
            from .bmi import BMI_menu
            BMI_menu(config)
        elif submenu_keuze == "8":
            from .loopsnelheden import loopsnelheden_OHD_menu
            loopsnelheden_OHD_menu(config)
        # elif submenu_keuze == "9":
        #    from .onderhouds_interval import onderhouds_interval_menu
        #    onderhouds_interval_menu(config, "adv")
        elif submenu_keuze == "9":
            from submenus.boost import boost_menu
            boost_menu(config)
        elif submenu_keuze == "10":
            from .positioning_system_profile import positioning_system_profile
            positioning_system_profile(config)
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            from ..overheaddeur import ohd_menu
            return ohd_menu(config, afsluiting)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_ohd_standalone(config, afsluiting):
    if vraag_ja_nee("Motor instellingen aanpassen? (y/n) "):
        from .motor_instellingen import motor_instelling_menu
        motor_instelling_menu(config)

    if vraag_ja_nee("positioneringssysteem instellen? (y/n)   "):
        from .positioning_system_profile import positioning_system_profile
        positioning_system_profile(config)

    if vraag_ja_nee("loopsnelheden aanpassen (y/n)  "):
        from .loopsnelheden import loopsnelheden_OHD_menu
    if vraag_ja_nee("zelftest instellen? (y/n)"):
        from .zelftest import zelftest_menu
        zelftest_menu(config, "ohd")

    if vraag_ja_nee("loopsnelheden aanpassen? (y/n)"):
        from .loopsnelheden import loopsnelheden_OHD_menu
        loopsnelheden_OHD_menu(config)

    if vraag_ja_nee("boost intellen? (y/n)   "):
        from .boost import boost_menu
        boost_menu(config)

    if vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) "):
        from .verkeerslichten import verkeerslichten_menu
        verkeerslichten_menu(config, "ohd")
        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
            from .heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
                from .auto_sluittijd import auto_sluittijd_menu
                auto_sluittijd_menu(config, "ohd")

    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
            auto_sluittijd_menu(config, "ohd")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        from .node_id import node_id_menu
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        from .bmi import BMI_menu
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #    from .onderhouds_interval import onderhouds_interval_menu
    #    onderhouds_interval_menu(config, "ohd")

    return True
