# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# verkeerslichten v0.1
# ======================


def verkeerslichten_menu(config, afsluiting):
    print("Standaard verkeerslichtsturing toegevoegd. K1 voor VKL buiten en K2 voor VKL binnen. rood op NC en groen op NO.")

    if afsluiting in ("as", "adv"):
        config.hoofd_parameter.extend([("0701", "1210"), ("0702", "1201")])
        config.sub_parameter.extend(
            [("0716", "2"), ("0719", "5"), ("071f", "19"), ("0726", "0"), ("0729", "5"), ("072f", "19")])

    if afsluiting in ("ohd"):
        config.hoofd_parameter.extend([("0701", "1210"), ("0702", "1201")])
        config.sub_parameter.extend(
            [("0716", "2"), ("0719", "2"), ("071f", "19"), ("0726", "0"), ("0729", "2"), ("072f", "19")])
