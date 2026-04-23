# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import *

# ======================
# loopsnelheden v0.3
# ======================


def loopsnelheden_OHD_menu(config):
    if vraag_ja_nee(
            "wil je de standaard snelheden inladen (gebaseerd op de GFA SE 9.24) (y) of wil je alle waardes zelf bepalen? (n) (y/n)  "):
        # open
        config.sub_parameter.append(("0161", "60"))         # max hz. open
        config.sub_parameter.append(("0310", "60"))         # open hz.
        # R1 acceleration hz/s
        config.sub_parameter.append(("0312", "17"))
        config.sub_parameter.append(("0320", "35"))         # creep open hz.

        # dicht
        config.sub_parameter.append(("0162", "60"))         # max hz. close
        config.sub_parameter.append(("0350", "50"))         # close hz.
        # R5 acceleration hz/s
        config.sub_parameter.append(("0352", "25"))
        config.sub_parameter.append(("0360", "35"))         # creep close hz.
        # R6 brake acceleration hz/s
        config.sub_parameter.append(("0362", "25"))

        # = stop
        config.sub_parameter.append(("0374", "400"))
        # stopramp safety edge
        config.sub_parameter.append(("0372", "400"))
        config.sub_parameter.append(("0382", "400"))
        config.sub_parameter.append(("0388", "200"))

        print("standaard loopsnelheden toegevoegd")

    else:
        snelheid_open = vraag_getal(
            "Loopsnelheid open in Hz (p.310): hoofdsnelheid waarmee de deur opent, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
        if snelheid_open is not None:
            config.sub_parameter.append(("0310", snelheid_open))

        snelheid_dicht = vraag_getal(
            "Loopsnelheid sluiten in Hz (p.350): hoofdsnelheid waarmee de deur sluit, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
        if snelheid_dicht is not None:
            config.sub_parameter.append(("0350", snelheid_dicht))
