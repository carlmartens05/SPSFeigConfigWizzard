# ======================
# Imports v0.1
# ======================

# Algemeen
from datetime import date
import os

# Bestanden
from .parameter_logic import sorteer_parameters

# ======================
# XML generator
# ======================


def maak_xml(bestandsnaam, afkorting, projectnummer, hoofd_parameter, sub_parameter):
    vandaag = date.today().strftime("%Y-%m-%d")

    # projectnummer altijd hoofdparameter
    if projectnummer:
        sub_parameter.append(("0927", projectnummer))

    # 🔹 sorteren per groep
    hoofd_sorted = sorteer_parameters(hoofd_parameter)
    sub_sorted = sorteer_parameters(sub_parameter)

    # 🔹 hoofd eerst, daarna sub
    alle_parameters = hoofd_sorted + sub_sorted

    # nette uitlijning
    max_ncode_len = max(len(code) for code, _ in alle_parameters)

    xml_lines = [
        '<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>',
        f'<parameterlist version="none" editor="{afkorting}" serial="{projectnummer}" date="{vandaag}">'
    ]

    # 🔹 Hoofdparameters bovenaan
    for code, waarde in hoofd_sorted:
        xml_lines.append(
            f'    <parameter ncode="{code.ljust(max_ncode_len)}" pdef="{waarde}" />')

    # 🔹 Subparameters daaronder
    for code, waarde in sub_sorted:
        xml_lines.append(
            f'    <parameter ncode="{code.ljust(max_ncode_len)}" pdef="{waarde}" />')

    xml_lines.append('</parameterlist>')

    pad = os.path.join(
        os.path.expanduser("~"),
        "Downloads",
        f"{projectnummer}_{bestandsnaam}_{vandaag}.xml" if projectnummer else f"{bestandsnaam}_{vandaag}.xml"
    )

    with open(pad, "w", encoding="iso-8859-1") as f:
        f.write("\n".join(xml_lines))

    print("\nXML opgeslagen in Downloads:")
    print(pad)
    input("\nDruk op Enter om af te sluiten...")
