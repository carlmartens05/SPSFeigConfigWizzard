# ======================
# main v0.3
# ======================

from utilities.config import *
from utilities.wizard import *
from utilities.xml_generator import *
from utilities.input_helpers import *


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
