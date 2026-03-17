# ======================
# main
# ======================

from utilities.config import Config
from utilities.wizard import wizard
from utilities.xml_generator import maak_xml
from utilities.input_helpers import vraag_afkorting, vraag_projectnummer, vraag_bestandsnaam


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
