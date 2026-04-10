# ============================
# keuzemenu slagbomen v0.1
# ============================

# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code


# === as plc's ===


def keuzemenu_menus_as_plc(config, afsluiting):
    from slagboom import as_plc_menu
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? =====
                1 = zelftest
                2 = node id voor PXS Feig koppeling
                3 = BMI instellingen
                klaar = klaar met configureren en maak bestand aan.
                terug = terug naar AS PLC menu.
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            from ..submenus.zelftest import zelftest_menu
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "2":
            from ..submenus.node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "3":
            from ..submenus.bmi import BMI_menu
            BMI_menu(config)
#        elif submenu_keuze == "4":
#            from ..submenus.onderhouds_interval import onderhouds_interval_menu
#            onderhouds_interval_menu(config, "as")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            from ..slagboom import as_plc_menu
            return as_plc_menu(config)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_as_plc(config, afsluiting):
    if vraag_ja_nee("Zelftest instellen? (y/n) "):
        from ..submenus.zelftest import zelftest_menu
        zelftest_menu(config, "as")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        from ..submenus.node_id import node_id_menu
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        from ..submenus.bmi import BMI_menu
        BMI_menu(config)

#    if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
#            from .onderhouds_interval import onderhouds_interval_menu
#        onderhouds_interval_menu(config, "as")
    return True

# === as standalone ===


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
                klaar = klaar met configureren en maak bestand aan.
                terug = terug naar adv. menu.
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, afsluiting)
        elif submenu_keuze == "2":
            from ..submenus.zelftest import zelftest_menu
            zelftest_menu(config, afsluiting)
        elif submenu_keuze == "3":
            from ..submenus.verkeerslichten import verkeerslichten_menu
            verkeerslichten_menu(config, afsluiting)
        elif submenu_keuze == "4":
            from ..submenus.node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "5":
            from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        elif submenu_keuze == "6":
            from ..submenus.bmi import BMI_menu
            BMI_menu(config)
        # elif submenu_keuze == "7":
        #            from .onderhouds_interval import onderhouds_interval_menu
        #    onderhouds_interval_menu(config, "as")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            from ..slagboom import as_standalone_menu
            return as_standalone_menu(config)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_as_standalone(config, afsluiting):
    if vraag_ja_nee("Zelftest instellen? (y/n)  "):
        from ..submenus.zelftest import zelftest_menu
        zelftest_menu(config, "as")

    if vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) "):
        from ..submenus.verkeerslichten import verkeerslichten_menu
        verkeerslichten_menu(config, "as")
        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
            from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
                from ..submenus.auto_sluittijd import auto_sluittijd_menu
                auto_sluittijd_menu(config, "as")
    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, "as")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        from ..submenus.node_id import node_id_menu
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        from ..submenus.bmi import BMI_menu
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #            from ..submenus.onderhouds_interval import onderhouds_interval_menu
    #    onderhouds_interval_menu(config, "as")
    return True
