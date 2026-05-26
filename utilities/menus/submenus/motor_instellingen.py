# =========================
# motor instellingen v0.8
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

    motor_profile = vraag_getal("""
                ===== wil je een motor profiel selecteren? ( controleer altijd zelf of de ingestelde waarde klopt!!!) =====
                0 = alles zelf instellen
                1 = GfA SE 9.24  (part no. 10002188 )
                2 = GfA SI 25.10 (part no. 10003166 )
                """)
    if motor_profile == "0":
        freq = vraag_getal("Frequentie motor (P.100 Hz)")
        if freq is not None:
            config.set_parameter("0100", freq)

        amp = vraag_getal(
            "Amperage motor (P.101) laat de punt weg dus 2.1A = 21")
        if amp is not None:
            config.set_parameter("0101", amp)

        cosphi = vraag_getal("Cos phi motor (P.102)")
        if cosphi is not None:
            config.set_parameter("0102", cosphi)

        volt = vraag_getal("Voltage motor (P.103)")
        if volt is not None:
            config.set_parameter("0103", volt)

    if motor_profile == "1":
        config.sub_parameter.append(("0100", "50"))
        config.sub_parameter.append(("0101", "21"))
        config.sub_parameter.append(("0102", "60"))
        config.sub_parameter.append(("0103", "230"))
        print("standaard parameters toegevoegd voor de GfA SE 9.24 (part no. 10002188 ) ")

    if motor_profile == "2":
        config.sub_parameter.append(("0100", "50"))
        config.sub_parameter.append(("0101", "31"))
        config.sub_parameter.append(("0102", "51"))
        config.sub_parameter.append(("0103", "230"))
        print("standaard parameters toegevoegd voor de GfA SI 25.10 (part no. 10003166 ) ")

    # Boost alleen vragen als nog niet ingesteld
    if not config.boost_ingesteld() and vraag_ja_nee("wil je een boost instellen? (y/n)"):
        from .boost import boost_menu
        boost_menu(config)
