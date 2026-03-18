# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# =========================
# motor instellingen v0.1
# =========================


def motor_instelling_menu(config):
    freq = vraag_getal("Frequentie motor (P.100 Hz)")
    if freq is not None:
        config.sub_parameter.append(("0100", freq))

    amp = vraag_getal("Amperage motor (P.101) laat de punt weg dus 2.1A = 21")
    if amp is not None:
        config.sub_parameter.append(("0101", amp))

    cosphi = vraag_getal("Cos phi motor (P.102)")
    if cosphi is not None:
        config.sub_parameter.append(("0102", cosphi))

    volt = vraag_getal("Voltage motor (P.103)")
    if volt is not None:
        config.sub_parameter.append(("0103", volt))
