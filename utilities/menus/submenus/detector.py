# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# detector v0.1
# ======================


def detector_menu(config):
    detector = vraag_getal("""
                ===== welk type lusdetector wordt er gebruikt? =====
                0 = externe lusdetector, aangesloten op input 2  (OHD)
                1 = FEIG TST Suvek 2, opsteek detector.
                2 = FEIG TST RFUxK, detector ingebouwd in extensionboard.
                3 = zowel Suvek als RFUxK 
                """)

    if detector == "0":
        config.hoofd_parameter.append(("0502", "1801"))
    print("parameter toegevoegd voor externe lusdetector aangesloten op input 2 ")

    if detector == "1":
        print("TODO")

    if detector == "2":
        print("TODO")

    if detector == "3":
        print("TODO")
