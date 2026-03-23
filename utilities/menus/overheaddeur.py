# imports
from ..input_helpers import *
from ..parameter_logic import *
from .submenus.submenus import *


# ======================
# Overheaddeuren v0.2
# ======================


def ohd_menu(config):
    if vraag_ja_nee("wil je alle menu's doorlopen of wil je kiezen welke menu's ingesteld moeten worden? kiezen = y, alles = n "):
        keuzemenu_menus_ohd(config, "ohd")
    else:
        alle_menus_ohd(config, "ohd")
    return True
