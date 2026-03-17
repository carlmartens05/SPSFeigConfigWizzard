# ======================
# main
# ======================

from config import Config
from wizard import wizard
from xml_generator import maak_xml
from input_helpers import vraag_tekst, vraag_getal


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
    verboden = r'<>:"/\\|?*'
    naam = input("Bestandsnaam (Enter = parameters): ").strip()
    if naam == "":
        naam = "parameters"
    for teken in verboden:
        naam = naam.replace(teken, "")
    return naam


if __name__ == "__main__":
    config = Config()

    wizard(config)

    if config.sub_parameter:
        afkorting = vraag_afkorting()
        projectnummer = vraag_projectnummer()
        bestandsnaam = vraag_bestandsnaam()

        maak_xml(bestandsnaam, afkorting, projectnummer,
                 config.hoofd_parameter, config.sub_parameter)
    else:
        print("Geen parameters ingevoerd, XML wordt niet aangemaakt.")
