# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# boost v0.1
# ======================


def boost_menu(config):
    boost_open = vraag_getal(
        "met welk percentage moet het voltage toenemen in opengang? 0-30% ")
    if boost_open is not None:
        config.sub_parameter.append(("0140", boost_open))

    boost_close = vraag_getal(
        "met welk percentage moet het voltage toenemen in dichtgang? 0-30% ")
    if boost_close is not None:
        config.sub_parameter.append(("0145", boost_close))
