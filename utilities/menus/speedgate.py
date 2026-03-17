# imports
from ..input_helpers import *
from .submenus import *


# ======================
# Speedgates
# ======================

def sg_menu(config):
    sg_plc = input(
        "Wordt de speedgate aangestuurd door een PLC (y/n)? plc maar geen open/dicht/stop? kies nee  ").lower()

    if sg_plc == "y":
        config.hoofd_parameter.extend(
            [("0501", "0101"), ("0502", "0401"), ("0503", "0701")])
        config.sub_parameter.extend(
            [("0522", "1"), ("0010", "0"), ("0011", "0"), ("0012", "0"), ("08BA", "4"), ("0890", "0")])

        if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
            node_id_menu(config)

        if vraag_ja_nee("BMI instellen? (y/n) "):
            BMI_menu(config)
        return True

    elif sg_plc == "n":
        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
                auto_sluittijd_menu(config, "sg")

        if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
            node_id_menu(config)

        if vraag_ja_nee("BMI instellen? (y/n) "):
            BMI_menu(config)
        return True

    elif sg_plc == "terug":
        return False

    else:
        print("Ongeldige invoer, probeer opnieuw.")
