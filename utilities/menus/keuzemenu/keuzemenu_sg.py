# ============================
# keuzemenu speedgate v0.2
# ============================

# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code


# === sg plc's ===


def keuzemenu_menus_sg_plc(config, afsluiting):
    from ..speedgate import sg_menu
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? =====
                1 = node id voor PXS Feig koppeling
                2 = BMI instellingen
                klaar = klaar met configureren en maak bestand aan.
                terug = terug naar adv. menu.
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            from ..submenus.node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "2":
            from ..submenus.bmi import BMI_menu
            BMI_menu(config)
        #    elif submenu_keuze == "3":
        #    from ..submenus.onderhouds_interval import onderhouds_interval_menu
        #        onderhouds_interval_menu(config, "adv")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            return sg_menu(config, afsluiting)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_sg_plc(config, afsluiting):
    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        from ..submenus.node_id import node_id_menu
        node_id_menu(config)
    if vraag_ja_nee("BMI instellen? (y/n) "):
        from ..submenus.bmi import BMI_menu
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #    from .onderhouds_interval import onderhouds_interval_menu
    #    onderhouds_interval_menu(config, "sg")
    return True

# === sg standalone ===


def keuzemenu_menus_sg_standalone(config, afsluiting):
    from ..speedgate import sg_menu
    while True:
        submenu_keuze = vraag_tekst("""
                ===== welk submenu wil je doorlopen? =====
                1 = autosluittijd
                2 = node id voor PXS Feig koppeling
                3 = hellingbaan regeling
                4 = BMI instellingen
                klaar = klaar met configureren en maak bestand aan.
                terug = terug naar adv. menu.
                (enter = terug naar hoofdmenu)
                """)

        if submenu_keuze == "1":
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, afsluiting)
        elif submenu_keuze == "2":
            from ..submenus.node_id import node_id_menu
            node_id_menu(config)
        elif submenu_keuze == "3":
            from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
            heling_baan_regeling_menu(config)
        elif submenu_keuze == "4":
            from ..submenus.bmi import BMI_menu
            BMI_menu(config)
        # elif submenu_keuze == "5":
        #    from .onderhouds_interval import onderhouds_interval_menu
        #    onderhouds_interval_menu(config, "sg")
        elif submenu_keuze == "klaar":
            return True
        elif submenu_keuze == "terug":
            return sg_menu(config)
        elif submenu_keuze is None or submenu_keuze == "":
            return False
        else:
            print("Ongeldige keuze.")


def alle_menus_sg_standalone(config, afsluiting):
    if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
        from ..submenus.heling_baan_regeling import heling_baan_regeling_menu
        heling_baan_regeling_menu(config)
    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
            from ..submenus.auto_sluittijd import auto_sluittijd_menu
            auto_sluittijd_menu(config, "sg")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        from ..submenus.node_id import node_id_menu
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        from ..submenus.bmi import BMI_menu
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #    from .onderhouds_interval import onderhouds_interval_menu
    #    onderhouds_interval_menu(config, "sg")
    return True
