# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import *

# ======================
# detector v0.2
# ======================


def detector_menu(config, afsluiting):
    detector = vraag_getal("""
                ===== welk type lusdetector wordt er gebruikt? =====
                0 = externe lusdetector, aangesloten op een input.
                1 = FEIG TST Suvek 2, opsteek detector.
                2 = FEIG TST RFUxK, detector ingebouwd in extensionboard.
                3 = zowel Suvek als RFUxK 
                """)

    if detector == "0":
        if afsluiting == "ohd":
            config.hoofd_parameter.append(("0502", "1801"))
            print("parameter toegevoegd voor externe lusdetector aangesloten op input 2 ")
        if afsluiting == "as":
            print(
                "sluit de detector aan op input 5 en pas deze aan dmv de dipinstellingen")

    if detector == "1":
        config.hoofd_parameter.append(("0802", "0302"))
        ch1 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch1 == "0":
            config.sub_parameter.append(("0660", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch1 == "1":
            config.sub_parameter.append(("0660", "24"))
            config.sub_parameter.append(("066c", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch1 == "2":
            config.sub_parameter.append(("0660", "24"))
            config.sub_parameter.append(("066c", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch1 == "3":
            config.sub_parameter.append(("0660", "23"))
            config.sub_parameter.append(("066c", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch1 == "4":
            config.sub_parameter.append(("0660", "23"))
            config.sub_parameter.append(("066c", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch1 == "5":
            config.sub_parameter.append(("0660", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch1 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, f)")
            config.hoofd_parameter.append((f"070{output_ch1}", "0612"))
            print(f"kanaal 1 schakelt output {output_ch1} ")

            logic_output_ch1 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch1 == "0":
                config.sub_parameter.append((f"07{output_ch1}4", "0"))
                print(f"output {output_ch1} is in rust verbroken")

            if logic_output_ch1 == "1":
                config.sub_parameter.append((f"07{output_ch1}4", "1"))
                print(f"output {output_ch1} is in rust gemaakt")

        ch2 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch2 == "0":
            config.sub_parameter.append(("0670", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch2 == "1":
            config.sub_parameter.append(("0670", "24"))
            config.sub_parameter.append(("067c", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch2 == "2":
            config.sub_parameter.append(("0670", "24"))
            config.sub_parameter.append(("067c", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch2 == "3":
            config.sub_parameter.append(("0670", "23"))
            config.sub_parameter.append(("067c", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch2 == "4":
            config.sub_parameter.append(("0670", "23"))
            config.sub_parameter.append(("067c", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch2 == "5":
            config.sub_parameter.append(("0670", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch2 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, f)")
            config.hoofd_parameter.append((f"070{output_ch2}", "0613"))
            print(f"kanaal 2 schakelt output {output_ch2} ")

            logic_output_ch2 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)
            if logic_output_ch2 == "0":
                config.sub_parameter.append((f"07{output_ch2}4", "0"))
                print(f"output {output_ch2} is in rust verbroken")

            if logic_output_ch2 == "1":
                config.sub_parameter.append((f"07{output_ch2}4", "1"))
                print(f"output {output_ch2} is in rust gemaakt")

    if detector == "2":
        config.hoofd_parameter.append(("0800", "5"))
        ch3 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch3 == "0":
            config.sub_parameter.append(("06c0", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch3 == "1":
            config.sub_parameter.append(("06c0", "24"))
            config.sub_parameter.append(("06cc", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch3 == "2":
            config.sub_parameter.append(("06c0", "24"))
            config.sub_parameter.append(("06cc", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch3 == "3":
            config.sub_parameter.append(("06c0", "23"))
            config.sub_parameter.append(("06cc", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch3 == "4":
            config.sub_parameter.append(("06c0", "23"))
            config.sub_parameter.append(("06cc", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch3 == "5":
            config.sub_parameter.append(("06c0", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch3 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch3}", "0612"))
            config.sub_parameter.append((f"07{output_ch3}0", "6"))
            config.sub_parameter.append((f"07{output_ch3}f", "50"))
            print(f"kanaal 1 schakelt output {output_ch3} ")

            logic_output_ch3 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch3 == "0":
                config.sub_parameter.append((f"07{output_ch3}4", "0"))
                print(f"output {output_ch3} is in rust verbroken")

            if logic_output_ch3 == "1":
                config.sub_parameter.append((f"07{output_ch3}4", "1"))
                print(f"output {output_ch3} is in rust gemaakt")

        ch4 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch4 == "0":
            config.sub_parameter.append(("06d0", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch4 == "1":
            config.sub_parameter.append(("06d0", "24"))
            config.sub_parameter.append(("06dc", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch4 == "2":
            config.sub_parameter.append(("06d0", "24"))
            config.sub_parameter.append(("06dc", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch4 == "3":
            config.sub_parameter.append(("06d0", "23"))
            config.sub_parameter.append(("06dc", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch4 == "4":
            config.sub_parameter.append(("06d0", "23"))
            config.sub_parameter.append(("06dc", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch4 == "5":
            config.sub_parameter.append(("06d0", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch4 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch4}", "0613"))
            config.sub_parameter.append((f"07{output_ch4}0", "6"))
            config.sub_parameter.append((f"07{output_ch4}f", "51"))
            print(f"kanaal 2 schakelt output {output_ch4} ")

            logic_output_ch4 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch4 == "0":
                config.sub_parameter.append((f"07{output_ch4}4", "0"))
                print(f"output {output_ch4} is in rust verbroken")

            if logic_output_ch4 == "1":
                config.sub_parameter.append((f"07{output_ch4}4", "1"))
                print(f"output {output_ch4} is in rust gemaakt")

    if detector == "3":
        config.hoofd_parameter.append(("0800", "5"))
        config.hoofd_parameter.append(("0802", "0302"))
        ch1 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch1 == "0":
            config.sub_parameter.append(("0660", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch1 == "1":
            config.sub_parameter.append(("0660", "24"))
            config.sub_parameter.append(("066c", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch1 == "2":
            config.sub_parameter.append(("0660", "24"))
            config.sub_parameter.append(("066c", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch1 == "3":
            config.sub_parameter.append(("0660", "23"))
            config.sub_parameter.append(("066c", "1"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch1 == "4":
            config.sub_parameter.append(("0660", "23"))
            config.sub_parameter.append(("066c", "0"))
            print(
                "kanaal 1 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch1 == "5":
            config.sub_parameter.append(("0660", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch1 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch1}", "0612"))
            print(f"kanaal 1 schakelt output {output_ch1} ")

            logic_output_ch1 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch1 == "0":
                config.sub_parameter.append((f"07{output_ch1}4", "0"))
                print(f"output {output_ch1} is in rust verbroken")

            if logic_output_ch1 == "1":
                config.sub_parameter.append((f"07{output_ch1}4", "1"))
                print(f"output {output_ch1} is in rust gemaakt")

        ch2 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch2 == "0":
            config.sub_parameter.append(("0670", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch2 == "1":
            config.sub_parameter.append(("0670", "24"))
            config.sub_parameter.append(("067c", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch2 == "2":
            config.sub_parameter.append(("0670", "24"))
            config.sub_parameter.append(("067c", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch2 == "3":
            config.sub_parameter.append(("0670", "23"))
            config.sub_parameter.append(("067c", "1"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch2 == "4":
            config.sub_parameter.append(("0670", "23"))
            config.sub_parameter.append(("067c", "0"))
            print(
                "kanaal 2 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch2 == "5":
            config.sub_parameter.append(("0670", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch2 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch2}", "0613"))
            print(f"kanaal 2 schakelt output {output_ch2} ")

            logic_output_ch2 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch2 == "0":
                config.sub_parameter.append((f"07{output_ch2}4", "0"))
                print(f"output {output_ch2} is in rust verbroken")

            if logic_output_ch2 == "1":
                config.sub_parameter.append((f"07{output_ch2}4", "1"))
                print(f"output {output_ch2} is in rust gemaakt")

        ch3 = vraag_getal("""
                wat is de functie van de lus die op kanaal 3 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch3 == "0":
            config.sub_parameter.append(("06c0", "20"))
            print("kanaal 3 uitgeschakeld")

        if ch3 == "1":
            config.sub_parameter.append(("06c0", "24"))
            config.sub_parameter.append(("06cc", "1"))
            print(
                "kanaal 3 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch3 == "2":
            config.sub_parameter.append(("06c0", "24"))
            config.sub_parameter.append(("06cc", "0"))
            print(
                "kanaal 3 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch3 == "3":
            config.sub_parameter.append(("06c0", "23"))
            config.sub_parameter.append(("06cc", "1"))
            print(
                "kanaal 3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch3 == "4":
            config.sub_parameter.append(("06c0", "23"))
            config.sub_parameter.append(("06cc", "0"))
            print(
                "kanaal 3 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch3 == "5":
            config.sub_parameter.append(("06c0", "21"))
            print(
                "kanaal 3 = geen interne functie, maar wel extern doorgezet.")

            output_ch3 = vraag_getal(
                "welke output moet kanaal 3 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch3}", "0612"))
            config.sub_parameter.append((f"07{output_ch3}0", "6"))
            config.sub_parameter.append((f"07{output_ch3}f", "50"))
            print(f"kanaal 1 schakelt output {output_ch3} ")

            logic_output_ch3 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch3 == "0":
                config.sub_parameter.append((f"07{output_ch3}4", "0"))
                print(f"output {output_ch3} is in rust verbroken")

            if logic_output_ch3 == "1":
                config.sub_parameter.append((f"07{output_ch3}4", "1"))
                print(f"output {output_ch3} is in rust gemaakt")

        ch4 = vraag_getal("""
                wat is de functie van de lus die op kanaal 4 zit aangesloten?
                         0 = uitgeschakeld
                         1 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten    (standaard OHD functie)
                         2 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando           (alternatieve OHD functie)
                         3 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten    (standaard AS functie)
                         4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando           (alternatieve AS functie)
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch4 == "0":
            config.sub_parameter.append(("06d0", "20"))
            print("kanaal 4 uitgeschakeld")

        if ch4 == "1":
            config.sub_parameter.append(("06d0", "24"))
            config.sub_parameter.append(("06dc", "1"))
            print(
                "kanaal 4 = sluit/veiligheid lus, stoppen bij sluiten, sluitcomando na verlaten")

        if ch4 == "2":
            config.sub_parameter.append(("06d0", "24"))
            config.sub_parameter.append(("06dc", "0"))
            print(
                "kanaal 4 = sluit/veiligheid lus, stoppen bij sluiten, geen sluitcomando")

        if ch4 == "3":
            config.sub_parameter.append(("06d0", "23"))
            config.sub_parameter.append(("06dc", "1"))
            print(
                "kanaal 4 = sluit/veiligheid lus, omkeren bij sluiten, sluitcomando na verlaten")

        if ch4 == "4":
            config.sub_parameter.append(("06d0", "23"))
            config.sub_parameter.append(("06dc", "0"))
            print(
                "kanaal 4 = sluit/veiligheid lus, omkeren bij sluiten, geen sluitcomando")

        if ch4 == "5":
            config.sub_parameter.append(("06d0", "21"))
            print(
                "kanaal 4 = geen interne functie, maar wel extern doorgezet.")

            output_ch4 = vraag_getal(
                "welke output moet kanaal 4 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch4}", "0613"))
            config.sub_parameter.append((f"07{output_ch4}0", "6"))
            config.sub_parameter.append((f"07{output_ch4}f", "51"))
            print(f"kanaal 2 schakelt output {output_ch4} ")

            logic_output_ch4 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch4 == "0":
                config.sub_parameter.append((f"07{output_ch4}4", "0"))
                print(f"output {output_ch4} is in rust verbroken")

            if logic_output_ch4 == "1":
                config.sub_parameter.append((f"07{output_ch4}4", "1"))
                print(f"output {output_ch4} is in rust gemaakt")


def detector_PLC_menu(config, afsluiting):
    detector = vraag_getal("""
                ===== welk type lusdetector wordt er gebruikt? =====
                0 = externe lusdetector, aangesloten op een input van de PLC
                2 = FEIG TST RFUxK, detector ingebouwd in extensionboard.
                3 = zowel Suvek als RFUxK 
                """)

    if detector == "0":
        print("sluit de detector aan op de inputs van de PLC en pas deze aan dmv de dipinstellingen ")

    if detector == "1":
        config.hoofd_parameter.append(("0802", "0302"))
        ch1 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch1 == "0":
            config.sub_parameter.append(("0660", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch1 == "5":
            config.sub_parameter.append(("0660", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch1 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, f)")
            config.hoofd_parameter.append((f"070{output_ch1}", "0612"))
            print(f"kanaal 1 schakelt output {output_ch1} ")

            logic_output_ch1 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch1 == "0":
                config.sub_parameter.append((f"07{output_ch1}4", "0"))
                print(f"output {output_ch1} is in rust verbroken")

            if logic_output_ch1 == "1":
                config.sub_parameter.append((f"07{output_ch1}4", "1"))
                print(f"output {output_ch1} is in rust gemaakt")

        ch2 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch2 == "0":
            config.sub_parameter.append(("0670", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch2 == "5":
            config.sub_parameter.append(("0670", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch2 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, f)")
            config.hoofd_parameter.append((f"070{output_ch2}", "0613"))
            print(f"kanaal 2 schakelt output {output_ch2} ")

            logic_output_ch2 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)
            if logic_output_ch2 == "0":
                config.sub_parameter.append((f"07{output_ch2}4", "0"))
                print(f"output {output_ch2} is in rust verbroken")

            if logic_output_ch2 == "1":
                config.sub_parameter.append((f"07{output_ch2}4", "1"))
                print(f"output {output_ch2} is in rust gemaakt")

    if detector == "2":
        config.hoofd_parameter.append(("0800", "5"))
        ch3 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch3 == "0":
            config.sub_parameter.append(("06c0", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch3 == "5":
            config.sub_parameter.append(("06c0", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch3 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch3}", "0612"))
            config.sub_parameter.append((f"07{output_ch3}0", "6"))
            config.sub_parameter.append((f"07{output_ch3}f", "50"))
            print(f"kanaal 1 schakelt output {output_ch3} ")

            logic_output_ch3 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch3 == "0":
                config.sub_parameter.append((f"07{output_ch3}4", "0"))
                print(f"output {output_ch3} is in rust verbroken")

            if logic_output_ch3 == "1":
                config.sub_parameter.append((f"07{output_ch3}4", "1"))
                print(f"output {output_ch3} is in rust gemaakt")

        ch4 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch4 == "0":
            config.sub_parameter.append(("06d0", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch4 == "5":
            config.sub_parameter.append(("06d0", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch4 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch4}", "0613"))
            config.sub_parameter.append((f"07{output_ch4}0", "6"))
            config.sub_parameter.append((f"07{output_ch4}f", "51"))
            print(f"kanaal 2 schakelt output {output_ch4} ")

            logic_output_ch4 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch4 == "0":
                config.sub_parameter.append((f"07{output_ch4}4", "0"))
                print(f"output {output_ch4} is in rust verbroken")

            if logic_output_ch4 == "1":
                config.sub_parameter.append((f"07{output_ch4}4", "1"))
                print(f"output {output_ch4} is in rust gemaakt")

    if detector == "3":
        config.hoofd_parameter.append(("0800", "5"))
        config.hoofd_parameter.append(("0802", "0302"))
        ch1 = vraag_getal("""
                wat is de functie van de lus die op kanaal 1 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch1 == "0":
            config.sub_parameter.append(("0660", "20"))
            print("kanaal 1 uitgeschakeld")

        if ch1 == "5":
            config.sub_parameter.append(("0660", "21"))
            print(
                "kanaal 1 = geen interne functie, maar wel extern doorgezet.")

            output_ch1 = vraag_getal(
                "welke output moet kanaal 1 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch1}", "0612"))
            print(f"kanaal 1 schakelt output {output_ch1} ")

            logic_output_ch1 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch1 == "0":
                config.sub_parameter.append((f"07{output_ch1}4", "0"))
                print(f"output {output_ch1} is in rust verbroken")

            if logic_output_ch1 == "1":
                config.sub_parameter.append((f"07{output_ch1}4", "1"))
                print(f"output {output_ch1} is in rust gemaakt")

        ch2 = vraag_getal("""
                wat is de functie van de lus die op kanaal 2 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch2 == "0":
            config.sub_parameter.append(("0670", "20"))
            print("kanaal 2 uitgeschakeld")

        if ch2 == "5":
            config.sub_parameter.append(("0670", "21"))
            print(
                "kanaal 2 = geen interne functie, maar wel extern doorgezet.")

            output_ch2 = vraag_getal(
                "welke output moet kanaal 2 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch2}", "0613"))
            print(f"kanaal 2 schakelt output {output_ch2} ")

            logic_output_ch2 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch2 == "0":
                config.sub_parameter.append((f"07{output_ch2}4", "0"))
                print(f"output {output_ch2} is in rust verbroken")

            if logic_output_ch2 == "1":
                config.sub_parameter.append((f"07{output_ch2}4", "1"))
                print(f"output {output_ch2} is in rust gemaakt")

        ch3 = vraag_getal("""
                wat is de functie van de lus die op kanaal 3 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch3 == "0":
            config.sub_parameter.append(("06c0", "20"))
            print("kanaal 3 uitgeschakeld")

        if ch3 == "5":
            config.sub_parameter.append(("06c0", "21"))
            print(
                "kanaal 3 = geen interne functie, maar wel extern doorgezet.")

            output_ch3 = vraag_getal(
                "welke output moet kanaal 3 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch3}", "0612"))
            config.sub_parameter.append((f"07{output_ch3}0", "6"))
            config.sub_parameter.append((f"07{output_ch3}f", "50"))
            print(f"kanaal 1 schakelt output {output_ch3} ")

            logic_output_ch3 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch3 == "0":
                config.sub_parameter.append((f"07{output_ch3}4", "0"))
                print(f"output {output_ch3} is in rust verbroken")

            if logic_output_ch3 == "1":
                config.sub_parameter.append((f"07{output_ch3}4", "1"))
                print(f"output {output_ch3} is in rust gemaakt")

        ch4 = vraag_getal("""
                wat is de functie van de lus die op kanaal 4 zit aangesloten?
                         0 = uitgeschakeld
                         5 = geen interne functie, maar wel extern doorgezet.                       (command forwarding)       
                                        """)
        if ch4 == "0":
            config.sub_parameter.append(("06d0", "20"))
            print("kanaal 4 uitgeschakeld")

        if ch4 == "5":
            config.sub_parameter.append(("06d0", "21"))
            print(
                "kanaal 4 = geen interne functie, maar wel extern doorgezet.")

            output_ch4 = vraag_getal(
                "welke output moet kanaal 4 aansturen? (1-2, 5-9 a-b, f)")
            config.hoofd_parameter.append((f"070{output_ch4}", "0613"))
            config.sub_parameter.append((f"07{output_ch4}0", "6"))
            config.sub_parameter.append((f"07{output_ch4}f", "51"))
            print(f"kanaal 2 schakelt output {output_ch4} ")

            logic_output_ch4 = vraag_getal("""
                moet het contact in rust verbroken of gemaakt zijn? 
                        0 = verbroken
                        1 = gemaakt
                                           """)

            if logic_output_ch4 == "0":
                config.sub_parameter.append((f"07{output_ch4}4", "0"))
                print(f"output {output_ch4} is in rust verbroken")

            if logic_output_ch4 == "1":
                config.sub_parameter.append((f"07{output_ch4}4", "1"))
                print(f"output {output_ch4} is in rust gemaakt")
