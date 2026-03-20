# imports
from ..input_helpers import *
from ..parameter_logic import *
from .submenus.submenus import *


# ======================
# Overheaddeuren v0.1
# ======================


def ohd_menu(config):
    if vraag_ja_nee("Motor instellingen aanpassen? (y/n) "):
        motor_instelling_menu(config)

    if vraag_ja_nee("loopsnelheden aanpassen (y/n)"):
        loopsnelheden_OHD_menu(config)

    if vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) "):
        verkeerslichten_menu(config, "ohd")
        if vraag_ja_nee("Hellingbaan regeling instellen? (y/n) "):
            heling_baan_regeling_menu(config)
        else:
            if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
                auto_sluittijd_menu(config, "ohd")
    else:
        if vraag_ja_nee("Autosluittijd aanpassen? (y/n) "):
            auto_sluittijd_menu(config, "ohd")

    if vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) "):
        node_id_menu(config)

    if vraag_ja_nee("BMI instellen? (y/n) "):
        BMI_menu(config)

    # if vraag_ja_nee("wil je een onderhoudsteller instellen? (y/n) "):
    #    onderhouds_interval_menu(config, "ohd")

    return True
