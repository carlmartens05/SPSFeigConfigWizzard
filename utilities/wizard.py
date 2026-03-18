# ======================
# wizard v0.1
# ======================

from utilities.input_helpers import *
from utilities.parameter_logic import *
from .menus.slagboom import as_menu
from .menus.speedgate import sg_menu
from .menus.overheaddeur import ohd_menu
from .menus.advanced import advanced_menu


def wizard(config):
    config.hoofd_parameter.clear()
    config.sub_parameter.clear()
    while True:
        afsluiting = input("""
        ====================================================================
        ===   SPS Feig config wizard V0.3  made by CMA   ===
        ====================================================================

        Op welk soort afsluiting zit de besturing aangesloten? (as/sg/ohd)
            """).lower()

        if afsluiting == "as" and as_menu(config):
            break
        elif afsluiting == "sg" and sg_menu(config):
            break
        elif afsluiting == "ohd" and ohd_menu(config):
            break
        elif afsluiting == "adv" and advanced_menu(config, "adv"):
            break
        else:
            print("Ongeldige invoer, probeer opnieuw.")
