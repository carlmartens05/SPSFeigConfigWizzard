# ============================
# keuzemenu overheadeuren v0.2
# ============================

# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code


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
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, afsluiting)
        elif submenu_keuze == "2":
            from ..submenus.motor_instellingen import motor_instelling_menu
            motor_instelling_menu(config)
        elif submenu_keuze == "3":
            from ..submenus.zelftest import zelftest_menu
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "4":
            from ..submenus.verkeerslichten import verkeerslichten_menu
            verkeerslichten_menu(config, afsluiting)
        elif submenu_keuze == "5":
            from ..submenus.node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "6":
            from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        elif submenu_keuze == "7":
            from ..submenus.bmi import BMI_menu
            BMI_menu(config)
        elif submenu_keuze == "8":
            from ..submenus.loopsnelheden import loopsnelheden_OHD_menu
            loopsnelheden_OHD_menu(config)
        # elif submenu_keuze == "9":
        #    from .onderhouds_interval import onderhouds_interval_menu
        #    onderhouds_interval_menu(config, "adv")
        elif submenu_keuze == "9":
            from submenus.boost import boost_menu
            boost_menu(config)
        elif submenu_keuze == "10":
            from ..submenus.positioning_system_profile import positioning_system_profile
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
        from ..submenus.motor_instellingen import motor_instelling_menu
        motor_instelling_menu(config)

    if vraag_ja_nee("positioneringssysteem instellen? (y/n)"):
        from ..submenus.positioning_system_profile import positioning_system_profile
        positioning_system_profile(config)

    if vraag_ja_nee("loopsnelheden aanpassen (y/n)"):
        from ..submenus.loopsnelheden import loopsnelheden_OHD_menu
        loopsnelheden_OHD_menu(config)

    if vraag_ja_nee("zelftest instellen? (y/n)"):
        from ..submenus.zelftest import zelftest_menu
        zelftest_menu(config, "ohd")

    if not config.boost_ingesteld() and vraag_ja_nee("boost instellen? (y/n)"):
        from ..submenus.boost import boost_menu
        boost_menu(config)

    if vraag_ja_nee("Verkeerslichtsturing instellen? (y/n)"):
        from ..submenus.verkeerslichten import verkeerslichten_menu
        verkeerslichten_menu(config, "ohd")

        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n)"):
            from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n)"):
                from ..submenus.auto_sluittijd import auto_sluittijd_menu
                auto_sluittijd_menu(config, "ohd")

    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n)"):
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, "ohd")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n)"):
        from ..submenus.node_id import node_id_menu
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n)"):
        from ..submenus.bmi import BMI_menu
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #    from ..submenus.onderhouds_interval import onderhouds_interval_menu
    #    onderhouds_interval_menu(config, "ohd")

    return True
