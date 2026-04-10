# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# loopsnelheden v0.2
# ======================


def loopsnelheden_OHD_menu(config):
    if vraag_ja_nee(
            "wil je de standaard snelheden inladen (gebaseerd op de GFA SE 9.24) (y) of wil je alle waardes zelf bepalen? (n) (y/n)  "):
        # open
        config.sub_parameter.append(("0310", "60"))
        # dicht
        config.sub_parameter.append(("0350", "50"))
        config.sub_parameter.append(("0360", "30"))

        # = stop
        config.sub_parameter.append(("0374", "400"))
        config.sub_parameter.append(("0372", "150"))
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
