# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# loopsnelheden v0.1
# ======================


def loopsnelheden_OHD_menu(config):
    snelheid_open = vraag_getal(
        "Loopsnelheid open in Hz (p.310): hoofdsnelheid waarmee de deur opent, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
    if snelheid_open is not None:
        config.sub_parameter.append(("0310", snelheid_open))

    snelheid_dicht = vraag_getal(
        "Loopsnelheid sluiten in Hz (p.350): hoofdsnelheid waarmee de deur sluit, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
    if snelheid_dicht is not None:
        config.sub_parameter.append(("0350", snelheid_dicht))
