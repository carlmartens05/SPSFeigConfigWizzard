# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# auto sluittijd v0.1
# ======================


def auto_sluittijd_menu(config, afsluiting):
    if afsluiting in ("as", "adv"):
        waarde = vraag_getal("Auto sluittijd geheel open (P.010)")
        if waarde is not None:
            config.sub_parameter.append(("0010", waarde))

    if afsluiting in ("sg", "adv"):
        waarde = vraag_getal("Auto sluittijd half open (P.011)")
        if waarde is not None:
            config.sub_parameter.append(("0011", waarde))

    if afsluiting in ("sg", "ohd", "adv"):
        waarde = vraag_getal("Geforceerde sluittijd (P.012)")
        if waarde is not None:
            config.sub_parameter.append(("0012", waarde))
