# =========================
# motor instellingen v0.5
# =========================

from ...input_helpers import vraag_getal, vraag_ja_nee


def motor_instelling_menu(config):
    config.sub_parameter.append(("0111", "0"))
    config.sub_parameter.append(("0112", "1"))
    config.sub_parameter.append(("0115", "25"))
    config.sub_parameter.append(("0116", "100"))
    config.sub_parameter.append(("0117", "0"))
    config.sub_parameter.append(("0142", "0"))
    config.sub_parameter.append(("0147", "0"))
    config.sub_parameter.append(("0143", "100"))
    config.sub_parameter.append(("0148", "100"))
    config.sub_parameter.append(("0165", "2"))

    freq = vraag_getal("Frequentie motor (P.100 Hz)")
    if freq is not None:
        config.set_parameter("0100", freq)

    amp = vraag_getal("Amperage motor (P.101) laat de punt weg dus 2.1A = 21")
    if amp is not None:
        config.set_parameter("0101", amp)

    cosphi = vraag_getal("Cos phi motor (P.102)")
    if cosphi is not None:
        config.set_parameter("0102", cosphi)

    volt = vraag_getal("Voltage motor (P.103)")
    if volt is not None:
        config.set_parameter("0103", volt)

    rotate = vraag_getal(
        "draairichting van de motor, 0 = rechts draaiend en 1 = links draaiend")
    if rotate is not None:
        config.set_parameter("0130", rotate)

    # Boost alleen vragen als nog niet ingesteld
    if not config.boost_ingesteld() and vraag_ja_nee("wil je een boost instellen? (y/n)"):
        from .boost import boost_menu
        boost_menu(config)
