# ======================
# boost v0.3
# ======================

from ...input_helpers import vraag_getal


def boost_menu(config):
    boost_open = vraag_getal(
        "met welk percentage moet het voltage toenemen in opengang? 0-30% ")
    if boost_open is not None:
        config.set_parameter("0140", boost_open)

    boost_close = vraag_getal(
        "met welk percentage moet het voltage toenemen in dichtgang? 0-30% ")
    if boost_close is not None:
        config.set_parameter("0145", boost_close)
