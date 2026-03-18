# imports
from ..input_helpers import *
from .submenus.submenus import *


# ===========================================================
# advanced menu voor handmatige submenu's en parameters v0.1
# ===========================================================

def advanced_menu(config, afsluiting):
    keuze = vraag_getal("""
        welkom in het geavenceerde menu, hier kan je handmatig naar submenu's van de wizard zonder de rest te doorlopen. 
        ook kan je handmatig parameters toevoegen.
        keuzes: 
        1 = submenu's
        2 = handmatig parameters toevoegen
        """)

    if keuze == "1":
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
                9 = onderhouds-teller
                klaar = klaar met configureren en maak bestand aan. 
                terug = terug naar adv. menu. 
                (enter = terug naar hoofdmenu)
                """)

            if submenu_keuze == "1":
                auto_sluittijd_menu(config, afsluiting)
            elif submenu_keuze == "2":
                motor_instelling_menu(config)
            elif submenu_keuze == "3":
                zelftest_menu(config, afsluiting)
            elif submenu_keuze == "4":
                verkeerslichten_menu(config, afsluiting)
            elif submenu_keuze == "5":
                node_id_menu(config)
            elif submenu_keuze == "6":
                heling_baan_regeling_menu(config)
            elif submenu_keuze == "7":
                BMI_menu(config)
            elif submenu_keuze == "8":
                loopsnelheden_OHD_menu(config)
            elif submenu_keuze == "9":
                onderhouds_interval_menu(config, "adv")
            elif submenu_keuze == "klaar":
                return True
            elif submenu_keuze == "terug":
                return advanced_menu(config, afsluiting)
            elif submenu_keuze is None or submenu_keuze == "":
                return False
            else:
                print("Ongeldige keuze.")

    elif keuze == "2":
        while True:
            ncode = input(
                "Voer het parameternummer in van de parameter die je wilt toevoegen. (van de parameter alles na de ' p. ' dus p.xxx vul xxx in.) als je klaar ben geen dan niks in en druk op enter. (Enter = klaar): ").strip()

            if ncode == "":
                print("Handmatige parameter invoer beëindigd.")
                return True

            waarde = input("Voer de waarde in voor deze parameter: ").strip()
            config.sub_parameter.append((ncode, waarde))
            print(f"Parameter p.{ncode} met waarde {waarde} toegevoegd.")
