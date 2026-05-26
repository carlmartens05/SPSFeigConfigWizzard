# ======================
# inputs v0.1
# ======================


# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import *


def standaard_inputs_OHD(config):
    config.hoofd_parameter.append(("0501", "0110"))
    config.hoofd_parameter.append(("0502", "1801"))
    config.hoofd_parameter.append(("0503", "0106"))
    config.hoofd_parameter.append(("0505", "0501"))
    config.hoofd_parameter.append(("0461", "0"))

    print("standaard inputs ingeladen.")

    if vraag_ja_nee("Is er inklimbeveiliging aanwezig? (y/n)"):
        config.hoofd_parameter.append(("0504", "1407"))
        config.sub_parameter.append(("0540", "14"))
        config.sub_parameter.append(("0541", "5"))
        print("Parameters voor inklimbeveiliging ingeladen.")
