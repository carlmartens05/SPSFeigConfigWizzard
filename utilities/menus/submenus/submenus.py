# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code

# == submenu's ==
# onderhouds intrval
from .onderhouds_interval import onderhouds_interval_menu
# auto sluittijd
from .auto_sluittijd import auto_sluittijd_menu
# motor instellingen
from .motor_instellingen import motor_instelling_menu
# zelftest
from .zelftest import zelftest_menu
# verkeerslichten
from .verkeerslichten import verkeerslichten_menu
# node id
from .node_id import node_id_menu


# ======================
# Submenu's
# ======================


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
