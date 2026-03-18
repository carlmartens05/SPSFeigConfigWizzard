# ===========================
# logic for parameters v0.1
# ===========================


def sorteer_parameters(param_list):
    """
    Sorteert parameters alfabetisch,
    maar zorgt dat parameter p.991 altijd bovenaan staat, voor het laden bij een slagboom vereist.
    """
    def sort_key(item):
        code = item[0].lower()
        if code == "0991":
            return ("", "")  # komt vóór alles
        return ("1", code)

    return sorted(param_list, key=sort_key)


def bereken_input_parameter_code(inputnr):
    """
    Zet inputnummer om naar de juiste parametercode.
    Inputs 1-15 → 05{hex}a
    Inputs 16-20 → ongeldig
    Inputs 21-26 → 0a1a t/m 0a6a
    """
    inputnr = int(inputnr)
    if 1 <= inputnr <= 15:
        input_hex = format(inputnr, "X").lower()
        return f"05{input_hex}a"
    elif 21 <= inputnr <= 26:
        input_calc = inputnr - 20
        return f"0a{input_calc}a"
    else:
        print("Ongeldige input. Toegestane waarden: 1-15 of 21-26.")
        return None
