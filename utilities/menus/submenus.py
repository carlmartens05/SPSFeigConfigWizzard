# imports
from ..input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ..parameter_logic import bereken_input_parameter_code

# ======================
# Submenu's
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


def zelftest_menu(config, afsluiting):
    if not any(code.lower() == "070f" for code, _ in config.hoofd_parameter):
        config.hoofd_parameter.append(("070f", "2501"))

    inputnr = vraag_getal("Welke input wil je zelftesten? (1-15 of 21-26) ")
    if inputnr:
        code = bereken_input_parameter_code(inputnr)
        if code is None:
            return zelftest_menu(config, afsluiting)
        config.sub_parameter.append((code, "1"))
        print(f"Input {inputnr} wordt getest.")
        if vraag_ja_nee("Wil je nog een input testen? (y/n) "):
            return zelftest_menu(config, afsluiting)


def verkeerslichten_menu(config, afsluiting):
    print("Standaard verkeerslichtsturing toegevoegd. K1 voor VKL buiten en K2 voor VKL binnen. rood op NC en groen op NO.")

    if afsluiting in ("as", "adv"):
        config.hoofd_parameter.extend([("0701", "1210"), ("0702", "1201")])
        config.sub_parameter.extend(
            [("0716", "2"), ("0719", "5"), ("071f", "19"), ("0726", "0"), ("0729", "5"), ("072f", "19")])

    if afsluiting in ("ohd"):
        config.hoofd_parameter.extend([("0701", "1210"), ("0702", "1201")])
        config.sub_parameter.extend(
            [("0716", "2"), ("0719", "2"), ("071f", "19"), ("0726", "0"), ("0729", "2"), ("072f", "19")])


def node_id_menu(config):
    node_id = vraag_getal(
        "Wat is de Node ID van de besturing? T.B.V. de PXS Feig koppeling (P.8ba) als standaard, gebruik hier het nummer van je afsluiting. (bijv. SG in -> 1, SG uit -> 2). ")
    if node_id is not None:
        config.sub_parameter.append(("08ba", node_id))


def heling_baan_regeling_menu(config):
    helling_minimale_groentijd = vraag_getal(
        "minimal greentime (P.017): wat is de minimale tijd dat het groene verkeerslicht aan moet blijven staan zonder dat er een voertuig door de afsluiting is gereden, voordat deze omschakeld naar de andere zijde.")
    if helling_minimale_groentijd is not None:
        config.sub_parameter.append(("0017", helling_minimale_groentijd))

    hellingbaan_roodtijd = vraag_getal(
        "Waiting-time between changing green-direction(P.01a): de tijd dat beide verkeerslichten op rood staan en dus de tijd dat het voertuig nodig heeft om de gehele afstand naar het andere verkeerslicht af te leggen.")
    if hellingbaan_roodtijd is not None:
        config.sub_parameter.append(("001a", hellingbaan_roodtijd))

    geforceerde_sluittijd = vraag_getal(
        "geforceerde sluittijd (P.012): voor de hellingbaanregeling moet de geforceerde sluittijd in worden gesteld, houd rekening met de lengte van de hellingbaan. in de regel is de waarde van p.01a + 30sec een goede maatstaf om mee te beginnen.   ")
    if geforceerde_sluittijd is not None:
        config.sub_parameter.append(("0012", geforceerde_sluittijd))

    hellingbaan_voorkeur_richting = vraag_getal("""voorkeursrichting (P.891): welke richting heeft de voorkeur bij het wisselen van zijde? 1 = inrijden/Trapeziumzijde, 2 = uitrijden/rechthoekzijde, 0 = geen voorkeur
                                            """)
    if hellingbaan_voorkeur_richting is not None:
        config.sub_parameter.append(("0891", hellingbaan_voorkeur_richting))


def loopsnelheden_OHD_menu(config):
    snelheid_open = vraag_getal(
        "Loopsnelheid open in Hz (p.310): hoofdsnelheid waarmee de deur opent, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
    if snelheid_open is not None:
        config.sub_parameter.append(("0310", snelheid_open))

    snelheid_dicht = vraag_getal(
        "Loopsnelheid sluiten in Hz (p.350): hoofdsnelheid waarmee de deur sluit, zorg dat deze waarde rond de waarde of gelijk is aan de HZ-waarde van de motor zodat de motor het meeste kracht heeft.")
    if snelheid_dicht is not None:
        config.sub_parameter.append(("0350", snelheid_dicht))


def BMI_menu(config):
    input_bmi = vraag_getal(
        'op welke input van de besturing zit de BMI aangesloten? standaard = 6, enter = 6')
    if input_bmi is None or input_bmi == "":
        input_bmi = "6"
        config.hoofd_parameter.append(("0506", "165"))
    else:
        code = bereken_input_parameter_code(input_bmi)
        if code is None:
            return BMI_menu(config)
        config.hoofd_parameter.append((code, "165"))
    print(f'input {input_bmi} wordt gebruikt voor BMI.')

    eindstand_bmi = vraag_getal(
        'naar welke positie moet de afsluiting bewegen bij een BMI melding? 0 = open 1 = dicht')
    if eindstand_bmi == "0":
        config.sub_parameter.append((f"05{input_bmi}0", "1"))
        config.sub_parameter.append((f"05{input_bmi}1", "18"))
        config.sub_parameter.append((f"05{input_bmi}3", "0"))
        config.sub_parameter.append((f"05{input_bmi}4", "1"))
        vkl_bmi = vraag_getal(
            "wat moeten de verkeerslichten doen bij een BMI melding? 0 = beide rood, 1= buiten groen , 2 = binnen groen 3 = beide groen")
        if vkl_bmi is not None:
            config.sub_parameter.append((f"05{input_bmi}6", vkl_bmi))
    elif eindstand_bmi == "1":
        config.sub_parameter.append((f"05{input_bmi}0", "8"))
        config.sub_parameter.append((f"05{input_bmi}1", "1"))
        config.sub_parameter.append((f"05{input_bmi}3", "3"))
        print("de afsluiting zal sluiten bij een BMI melding. verkeerslichten blijven op rood staan.")

    no_nc_bmi = vraag_getal(
        ' is de BMI een maak of een verbreek contact? maak = 0, verbreek = 1, enter = verbreek ')
    if no_nc_bmi is None or no_nc_bmi == "":
        config.sub_parameter.append((f"05{input_bmi}2", "1"))
    else:
        config.sub_parameter.append((f"05{input_bmi}2", no_nc_bmi))
