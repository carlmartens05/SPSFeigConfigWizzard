# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# zelftest menu v0.1
# ======================


def zelftest_menu(config, afsluiting):
    if not any(code.lower() == "070f" for code, _ in config.hoofd_parameter):
        config.hoofd_parameter.append(("070f", "2501"))

    inputnr = vraag_getal("Welke input wil je zelftesten? (1-15 of 21-26) ")
    if inputnr:
        code = bereken_input_parameter_code(inputnr)
        if code is None:
            return zelftest_menu(config, afsluiting)
        config.sub_parameter.append((code, "1"))
        print(f"Input {inputnr} wordt getest.")
        if vraag_ja_nee("Wil je nog een input testen? (y/n) "):
            return zelftest_menu(config, afsluiting)
