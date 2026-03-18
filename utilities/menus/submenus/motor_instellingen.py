# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# =========================
# motor instellingen v0.2
# =========================


def motor_instelling_menu(config):
    config.sub_parameter.append(("0111", "0"))
    config.sub_parameter.append(("0112", "1"))
    config.sub_parameter.append(("0115", "25"))
    config.sub_parameter.append(("0116", "100"))
    config.sub_parameter.append(("0117", "1"))
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

    rotate = vraag_getal(
        "draairichting van de motor, 0 = rechts draaiend en 1 = links draaiend")
    if rotate is not None:
        config.sub_parameter.append(("0130", rotate))

    if vraag_ja_nee(" wil je een boost instellen? (y/n)"):
        from .boost import boost_menu
        boost_menu(config)
