# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ==================================
#  positioning_system_profile v0.1
# ==================================


def positioning_system_profile(config):
    keuze = vraag_getal("""
        welk positioneringssysteem is aanwezig op de motor van de afsluiting?
        0 = mechanische eindcontacten, eindcontacten N.C., voor-eindcontacten N.O. 
        1 = mechanische eindcontacten, alles N.C.
        2 = encoder DES-A (GfA)
        3 = encoder DES-B (kostal)
        4 = encoder TST-PD/ TST-PE 
        5 = mechanische eindcontacten, ondersteunt door timers
        """)
    if keuze == "0":
        config.hoofd_parameter.append(("0205", "0000"))
    elif keuze == "1":
        config.hoofd_parameter.append(("0205", "0001"))
    elif keuze == "2":
        config.hoofd_parameter.append(("0205", "0300"))
    elif keuze == "3":
        config.hoofd_parameter.append(("0205", "0700"))
    elif keuze == "4":
        config.hoofd_parameter.append(("0205", "0800"))
    elif keuze == "5":
        config.hoofd_parameter.append(("0205", "0900"))
