from datetime import date
import os

parameters = []

# ======================
# Helper functies
# ======================


def vraag_ja_nee(vraag):
    while True:
        keuze = input(vraag).lower()
        if keuze in ("y", "n"):
            return keuze == "y"
        if keuze == "terug":
            return None
        print("Ongeldige invoer.")


def vraag_getal(vraag):
    while True:
        invoer = input(vraag + " (Enter = overslaan): ").lower()
        if invoer == "":
            return None
        if invoer.isdigit():
            return invoer
        print("Ongeldige invoer.")

# ======================
# Hoofd wizard
# ======================


def wizard():
    global parameters
    parameters.clear()
    while True:
        afsluiting = input(
            """
        ====================================================================
        ===   SPS Feig config wizard V0.1.2  made by CMA powered by AI   ===
        ====================================================================

        Op welk soort afsluiting zit de besturing aangesloten? (as/sg/ohd)
            """
        ).lower()

        if afsluiting == "as" and as_menu():
            break
        elif afsluiting == "sg" and sg_menu():
            break
        elif afsluiting == "ohd" and ohd_menu():
            break
        elif afsluiting == "adv" and advanced_menu():
            break
        else:
            print("Ongeldige invoer, probeer opnieuw.")

# ======================
# Slagbomen
# ======================


def as_menu():
    while True:
        waarde = vraag_getal(
            'welk profiel heeft de slagboom volgens de sticker op de besturing? (zie de handleiding van Bormet voor meer info)').lower()
        if waarde is not None:
            parameters.append(("0991", waarde))

        keuze = input(
            "Wordt de slagboom aangestuurd door een PLC of standalone (PLC = open/dicht/stop, plc maar geen open/dicht/stop? kies standalone.) (plc/standalone)? "
        ).lower()

        if keuze == "plc":
            return as_plc_menu()
        elif keuze == "standalone":
            return as_standalone_menu()
        elif keuze == "terug":
            return False
        else:
            print("Ongeldige invoer.")


def as_plc_menu():
    # Voeg standaard parameters toe
    parameters.extend([
        ("0010", "0"),
        ("002a", "0"),
        ("04b7", "0"),
        ("0505", "1401"),
        ("0701", "0101"),
        ("0702", "0201"),
        ("0890", "0"),
    ])
    print("Parameters voor open/dicht/stop toegevoegd voor slagboom met PLC.")

    # Zelftest instellen
    keuze = vraag_ja_nee("Zelftest instellen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        zelftest_menu("as")

    # Node ID instellen
    keuze_node = vraag_ja_nee(
        "Node ID instellen voor PXS Feig koppeling? (y/n) ")
    if keuze_node is None:
        return False
    if keuze_node:
        node_id_menu()

    keuze_bmi = vraag_ja_nee("BMI instellen? (y/n) ")
    if keuze_bmi is None:
        return False
    if keuze_bmi:
        BMI_menu()

    return True


def as_standalone_menu():

    keuze = vraag_ja_nee("Zelftest instellen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        zelftest_menu("as")

    keuze_vkl = vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) ")
    if keuze_vkl is None:
        return False
    if keuze_vkl:
        verkeerslichten_menu("as")
        keuze_hellingbaan = vraag_ja_nee(
            "Hellingbaan regeling instellen? (y/n) ")
        if keuze_hellingbaan is None:
            return False
        if keuze:
            heling_baan_regeling_menu()
        if not keuze_hellingbaan:
            keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
            if keuze is None:
                return False
            if keuze:
                auto_sluittijd_menu("as")
    if not keuze_vkl:
        keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
        if keuze is None:
            return False
        if keuze:
            auto_sluittijd_menu("as")

    keuze = vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        node_id_menu()

    keuze_bmi = vraag_ja_nee("BMI instellen? (y/n) ")
    if keuze_bmi is None:
        return False
    if keuze_bmi:
        BMI_menu()

    return True

# ======================
# Speedgates
# ======================


def sg_menu():
    while True:
        sg_plc = input(
            "Wordt de speedgate aangestuurd door een PLC (y/n)? plc maar geen open/dicht/stop? kies nee").lower()

        if sg_plc == "y":
            parameters.extend([
                ("0501", "0101"),
                ("0502", "0401"),
                ("0522", "1"),
                ("0503", "0701"),
                ("0010", "0"),
                ("0011", "0"),
                ("0012", "0"),
                ("08BA", "4"),
                ("0890", "0"),
            ])
            keuze = vraag_ja_nee(
                "Node ID instellen voor PXS Feig koppeling? (y/n) ")
            if keuze is None:
                return False
            if keuze:
                node_id_menu()

            keuze_bmi = vraag_ja_nee("BMI instellen? (y/n) ")
            if keuze_bmi is None:
                return False
            if keuze_bmi:
                BMI_menu()
            return True

        elif sg_plc == "n":
            keuze_hellingbaan = vraag_ja_nee(
                "Hellingbaan regeling instellen? (y/n) ")
            if keuze_hellingbaan is None:
                return False
            if keuze_hellingbaan:
                heling_baan_regeling_menu()
            if not keuze_hellingbaan:
                keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
                if keuze is None:
                    return False
                if keuze:
                    auto_sluittijd_menu("sg")

            keuze_node = vraag_ja_nee(
                "Node ID instellen voor PXS Feig koppeling? (y/n) ")
            if keuze_node is None:
                return False
            if keuze_node:
                node_id_menu()

            keuze_bmi = vraag_ja_nee("BMI instellen? (y/n) ")
            if keuze_bmi is None:
                return False
            if keuze_bmi:
                BMI_menu()
            return True

        elif sg_plc == "terug":
            return False

        else:
            print("Ongeldige invoer, probeer opnieuw.")

# ======================
# Overheaddeuren
# ======================


def ohd_menu():
    keuze = vraag_ja_nee("Motor instellingen aanpassen? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        motor_instelling_menu()

    keuze_vkl = vraag_ja_nee("Verkeerslichtsturing instellen? (y/n) ")
    if keuze_vkl is None:
        return False
    if keuze:
        verkeerslichten_menu("ohd")
        keuze_hellingbaan = vraag_ja_nee(
            "Hellingbaan regeling instellen? (y/n) ")
        if keuze_hellingbaan is None:
            return False
        if keuze_hellingbaan:
            heling_baan_regeling_menu()
        if not keuze_hellingbaan:
            keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
            if keuze is None:
                return False
            if keuze:
                auto_sluittijd_menu("ohd")
    if not keuze_vkl:
        keuze = vraag_ja_nee("Autosluittijd aanpassen? (y/n) ")
        if keuze is None:
            return False
        if keuze:
            auto_sluittijd_menu("ohd")

    keuze = vraag_ja_nee("Node ID instellen voor PXS Feig koppeling? (y/n) ")
    if keuze is None:
        return False
    if keuze:
        node_id_menu()

    keuze_bmi = vraag_ja_nee("BMI instellen? (y/n) ")
    if keuze_bmi is None:
        return False
    if keuze_bmi:
        BMI_menu()

    return True

# ======================
# advanced menu voor handmatige submenu's en parameters
# ======================


def advanced_menu():
    pass
#
# gereserveerde ruimte
#

# ======================
# Submenu's
# ======================


def auto_sluittijd_menu(type_afsluiting):
    if type_afsluiting == "as":
        waarde = vraag_getal("Auto sluittijd geheel open (P.010)")
        if waarde is not None:
            parameters.append(("0010", waarde))

    if type_afsluiting == "sg":
        waarde = vraag_getal("Auto sluittijd half open (P.011)")
        if waarde is not None:
            parameters.append(("0011", waarde))

    if type_afsluiting in ("sg", "ohd"):
        waarde = vraag_getal("Geforceerde sluittijd (P.012)")
        if waarde is not None:
            parameters.append(("0012", waarde))


def motor_instelling_menu():
    freq = vraag_getal("Frequentie motor (P.100 Hz)")
    if freq is not None:
        parameters.append(("0100", freq))

    amp = vraag_getal("Amperage motor (P.101) laat de punt weg dus 2.1A = 21")
    if amp is not None:
        parameters.append(("0101", amp))

    cosphi = vraag_getal("Cos phi motor (P.102)")
    if cosphi is not None:
        parameters.append(("0102", cosphi))

    volt = vraag_getal("Voltage motor (P.103)")
    if volt is not None:
        parameters.append(("0103", volt))


def zelftest_menu(type_afsluiting):
    if type_afsluiting in ("as", "ohd"):
        inputnr = vraag_getal(
            "Welke input wil je zelftesten? output 15 wordt standaard gebruikt als testoutput.")
        if inputnr:
            parameters.append((f"05{inputnr}A", "1"))
            parameters.append(("070f", "2501"))
            print(f"Input {inputnr} wordt getest.")
            keuze = vraag_ja_nee("Wil je nog een input testen? (y/n) ")
            if keuze:
                return zelftest_menu(type_afsluiting)


def verkeerslichten_menu(type_afsluiting):
    print("Standaard verkeerslichtsturing toegevoegd. K1 voor VKL buiten en K2 voor VKL binnen. rood op NC en groen op NO.")

    if type_afsluiting == "as":
        parameters.extend([
            ("0701", "1210"),
            ("0702", "1201"),
            ("0716", "2"),
            ("0719", "5"),
            ("071f", "19"),
            ("0726", "0"),
            ("0729", "5"),
            ("072f", "19"),
        ])
    elif type_afsluiting == "ohd":
        parameters.extend([
            ("0701", "1210"),
            ("0702", "1201"),
            ("0716", "2"),
            ("0719", "2"),
            ("071f", "19"),
            ("0726", "0"),
            ("0729", "2"),
            ("072f", "19"),
        ])


def node_id_menu():
    node_id = vraag_getal(
        "Wat is de Node ID van de besturing? T.B.V. de PXS Feig koppeling (P.8ba) als standaard, gebruik hier het nummer van je afsluiting. (bijv. SG in -> 1, SG uit -> 2). ")
    if node_id is not None:
        parameters.append(("08ba", node_id))


def heling_baan_regeling_menu():
    helling_minimale_groentijd = vraag_getal(
        "minimal greentime (P.017): wat is de minimale tijd dat het groene verkeerslicht aan moet blijven staan zonder dat er een voertuig door de afsluiting is gereden, voordat deze omschakeld naar de andere zijde.")
    if helling_minimale_groentijd is not None:
        parameters.append(("0017", helling_minimale_groentijd))

    hellingbaan_roodtijd = vraag_getal(
        "Waiting-time between changing green-direction(P.01a): de tijd dat beide verkeerslichten op rood staan en dus de tijd dat het voertuig nodig heeft om de gehele afstand naar het andere verkeerslicht af te leggen.")
    if hellingbaan_roodtijd is not None:
        parameters.append(("001a", hellingbaan_roodtijd))

    geforceerde_sluittijd = vraag_getal(
        "geforceerde sluittijd (P.012): voor de hellingbaanregeling moet de geforceerde sluittijd in worden gesteld, houd rekening met de lengte van de hellingbaan. in de regel is de waarde van p.01a + 30sec een goede maatstaf om mee te beginnen.   ")
    if geforceerde_sluittijd is not None:
        parameters.append(("0012", geforceerde_sluittijd))

    hellingbaan_voorkeur_richting = vraag_getal("""voorkeursrichting (P.891): welke richting heeft de voorkeur bij het wisselen van zijde? 1 = inrijden/Trapeziumzijde, 2 = uitrijden/rechthoekzijde, 0 = geen voorkeur
                                            """)
    if hellingbaan_voorkeur_richting is not None:
        parameters.append(("0891", hellingbaan_voorkeur_richting))


def loopsnelheden_OHD_menu():
    pass
    # nog implenteren


def loopsnelheden_SG_menu():
    pass
    # nog implementeren, controleren of deze ook kunnen worden ingesteld via het OHD menu


def BMI_menu():
    input_bmi = vraag_getal(
        'op welke input van de besturing zit de BMI aangesloten? standaard = 6, enter = 6')
    if input_bmi is None or input_bmi == "":
        input_bmi = "6"
        parameters.append(("0506", "165"))
    elif input_bmi is not None:
        parameters.append((f"050{input_bmi}", "165"))
    print(f'input {input_bmi} wordt gebruikt voor BMI.')
    eindstand_bmi = vraag_getal(
        'naar welke positie moet de afsluiting bewegen bij een BMI melding? 0 = open 1 = dicht')
    if eindstand_bmi == "0":
        parameters.append((f"05{input_bmi}0", "1"))
        parameters.append((f"05{input_bmi}1", "18"))
        parameters.append((f"05{input_bmi}3", "0"))
        parameters.append((f"05{input_bmi}4", "1"))
        vkl_bmi = vraag_getal(
            "wat moeten de verkeerslichten doen bij een BMI melding? 0 = beide rood, 1= buiten groen , 2 = binnen groen 3 = beide groen")
        if vkl_bmi is not None:
            parameters.append((f"05{input_bmi}6", vkl_bmi))

    elif eindstand_bmi == "1":
        parameters.append((f"05{input_bmi}0", "8"))
        parameters.append((f"05{input_bmi}1", "1"))
        parameters.append((f"05{input_bmi}3", "3"))
        print("de afsluiting zal sluiten bij een BMI melding. verkeerslichten blijven op rood staan.")

    no_nc_bmi = vraag_getal(
        ' is de BMI een maak of een verbreek contact? maak = 0, verbreek = 1, enter = verbreek ')
    if no_nc_bmi is None or no_nc_bmi == "":
        parameters.append((f"05{input_bmi}2", "1"))
        print("de BMI is ingesteld als verbreek contact.")
    elif no_nc_bmi is not None:
        parameters.append((f"05{input_bmi}2", no_nc_bmi))


# ======================
# Invoerfuncties
# ======================


def vraag_afkorting():
    while True:
        afkorting = input(
            "Wat is je naamafkorting? (bijv. CMA, Enter = FCW (Feig_config_Wizard)): ").strip().lower()
        if afkorting == "":
            return "fcw"
        if not afkorting.isalpha():
            print("Gebruik alleen letters.")
            continue
        if len(afkorting) > 3:
            print("Maximaal 3 tekens.")
            continue
        return afkorting


def vraag_projectnummer():
    while True:
        projectnummer = input(
            "Wat is het projectnummer? (Enter = leeg laten, alleen cijfers): ").strip()
        if projectnummer == "":
            return ""
        if not projectnummer.isdigit():
            print(" Alleen cijfers toegestaan.")
            continue
        if len(projectnummer) > 7:
            print(" Maximaal 7 cijfers.")
            continue
        return projectnummer


def vraag_bestandsnaam():
    verboden = r'<>:"/\|?*'
    naam = input("Bestandsnaam (Enter = parameters): ").strip()
    if naam == "":
        naam = "parameters"
    for teken in verboden:
        naam = naam.replace(teken, "")
    return naam

# ======================
# XML generator
# ======================


def maak_xml(bestandsnaam, afkorting, projectnummer, parameters):
    vandaag = date.today().strftime("%Y-%m-%d")

    # schrijf projectnummer naar P.927
    parameters.append(("0927", projectnummer))

    # Bereken maximale lengte van ncode voor nette uitlijning
    max_ncode_len = max(len(code) for code, _ in parameters)

    # Begin van XML
    xml_lines = [
        '<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>',
        f'<parameterlist version="none" editor="{afkorting}" serial="{projectnummer}" date="{vandaag}">'
    ]

    # Voeg parameters toe met nette uitlijning
    for code, waarde in parameters:
        # Zorg dat ncode altijd dezelfde breedte krijgt
        code_padded = code.ljust(max_ncode_len)
        xml_lines.append(
            f'    <parameter ncode="{code_padded}" pdef="{waarde}" />')

    # Sluit de parameterlist
    xml_lines.append('</parameterlist>')

    # Bestandslocatie
    pad = os.path.join(
        os.path.expanduser("~"),
        "Downloads",
        f"{bestandsnaam}_{projectnummer}_{vandaag}.xml" if projectnummer else f"{bestandsnaam}_{vandaag}.xml"
    )

    # Schrijf bestand
    with open(pad, "w", encoding="iso-8859-1") as f:
        f.write("\n".join(xml_lines))

    print("\n XML opgeslagen in Downloads:")
    print(pad)
    print("\nDruk op Enter om af te sluiten...")
    input()

# ======================
# Programma start
# ======================


if __name__ == "__main__":
    wizard()  # vult parameters

    if parameters:
        afkorting = vraag_afkorting()
        projectnummer = vraag_projectnummer()
        bestandsnaam = vraag_bestandsnaam()
        maak_xml(bestandsnaam, afkorting, projectnummer, parameters)
        parameters.append(("0927", "{projectnummer}"))
    else:
        print("Geen parameters ingevoerd, XML wordt niet aangemaakt.")
