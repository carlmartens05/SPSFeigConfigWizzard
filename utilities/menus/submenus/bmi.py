# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# BMI v0.1
# ======================


def BMI_menu(config):
    input_bmi = vraag_getal(
        'op welke input van de besturing zit de BMI aangesloten? standaard = 6, enter = 6')
    if input_bmi is None or input_bmi == "":
        input_bmi = "6"
        config.hoofd_parameter.append(("0506", "0165"))
    else:
        code = bereken_input_parameter_code(input_bmi)
        if code is None:
            return BMI_menu(config)
        config.hoofd_parameter.append((code, "0165"))
    print(f'input {input_bmi} wordt gebruikt voor BMI.')

    eindstand_bmi = vraag_getal(
        'naar welke positie moet de afsluiting bewegen bij een BMI melding? 0 = open 1 = dicht')
    if eindstand_bmi == "0":
        config.sub_parameter.append((f"05{input_bmi}0", "1"))
        config.sub_parameter.append((f"05{input_bmi}1", "18"))
        config.sub_parameter.append((f"05{input_bmi}3", "0"))
        config.sub_parameter.append((f"05{input_bmi}4", "1"))
        vkl_bmi = vraag_getal(
            "wat moeten de verkeerslichten doen bij een BMI melding? 0 = beide rood, 1= buiten groen , 2 = binnen groen 3 = beide groen")
        if vkl_bmi is not None:
            config.sub_parameter.append((f"05{input_bmi}6", vkl_bmi))
    elif eindstand_bmi == "1":
        config.sub_parameter.append((f"05{input_bmi}0", "8"))
        config.sub_parameter.append((f"05{input_bmi}1", "1"))
        config.sub_parameter.append((f"05{input_bmi}3", "3"))
        print("de afsluiting zal sluiten bij een BMI melding. verkeerslichten blijven op rood staan.")

    no_nc_bmi = vraag_getal(
        ' is de BMI een maak of een verbreek contact? maak = 0, verbreek = 1, enter = verbreek ')
    if no_nc_bmi is None or no_nc_bmi == "":
        config.sub_parameter.append((f"05{input_bmi}2", "1"))
    else:
        config.sub_parameter.append((f"05{input_bmi}2", no_nc_bmi))
