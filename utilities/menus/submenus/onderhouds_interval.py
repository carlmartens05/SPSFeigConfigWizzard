# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# onderhouds_intrval
# ======================


def onderhouds_interval(config, afsluiting):
    if afsluiting in ("as", "adv"):
        waarde = vraag_getal(
            "na hoeveel cycli moet de besturing info-melding I.080 geven? deze waarde is in duizend tal. (dus 50.000 is 50.)  ")
        if waarde is not None:
            config.sub_parameter.append(("0970", "1"))
            config.sub_parameter.append(("0971", waarde))

    if afsluiting in ("sg"):
        waarde = vraag_getal(
            "na hoeveel cycli moet de besturing info-melding I.080 geven? deze waarde is in duizend tal. (dus 50.000 is 50.)  ")
        if waarde is not None:
            config.sub_parameter.append(("0970", "1"))
            config.sub_parameter.append(("0971", waarde))

    if afsluiting in ("ohd"):
        waarde = vraag_getal(
            "na hoeveel cycli moet de besturing info-melding I.080 geven? deze waarde is in duizend tal. (dus 50.000 is 50.)  ")
        if waarde is not None:
            config.sub_parameter.append(("0970", "1"))
            config.sub_parameter.append(("0971", waarde))
