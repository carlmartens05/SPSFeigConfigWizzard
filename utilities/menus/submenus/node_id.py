# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# node id v0.2
# ======================


def node_id_menu(config):
    node_id = vraag_getal(
        "Wat is de Node ID van de besturing? T.B.V. de PXS Feig koppeling (P.8ba) als standaard, gebruik hier het nummer van je afsluiting. (bijv. SG in -> 1, SG uit -> 2). ")
    if node_id is not None:
        config.sub_parameter.append(("08b1", node_id))
