# imports
from ...input_helpers import vraag_getal, vraag_ja_nee, vraag_tekst
from ...parameter_logic import bereken_input_parameter_code

# ======================
# heling baan regeling v0.1
# ======================


def heling_baan_regeling_menu(config):
    helling_minimale_groentijd = vraag_getal(
        "minimal greentime (P.017): wat is de minimale tijd dat het groene verkeerslicht aan moet blijven staan zonder dat er een voertuig door de afsluiting is gereden, voordat deze omschakeld naar de andere zijde.")
    if helling_minimale_groentijd is not None:
        config.sub_parameter.append(("0017", helling_minimale_groentijd))

    hellingbaan_roodtijd = vraag_getal(
        "Waiting-time between changing green-direction(P.01a): de tijd dat beide verkeerslichten op rood staan en dus de tijd dat het voertuig nodig heeft om de gehele afstand naar het andere verkeerslicht af te leggen.")
    if hellingbaan_roodtijd is not None:
        config.sub_parameter.append(("001a", hellingbaan_roodtijd))

    geforceerde_sluittijd = vraag_getal(
        "geforceerde sluittijd (P.012): voor de hellingbaanregeling moet de geforceerde sluittijd in worden gesteld, houd rekening met de lengte van de hellingbaan. in de regel is de waarde van p.01a + 30sec een goede maatstaf om mee te beginnen.   ")
    if geforceerde_sluittijd is not None:
        config.sub_parameter.append(("0012", geforceerde_sluittijd))

    hellingbaan_voorkeur_richting = vraag_getal("""voorkeursrichting (P.891): welke richting heeft de voorkeur bij het wisselen van zijde? 1 = inrijden/Trapeziumzijde, 2 = uitrijden/rechthoekzijde, 0 = geen voorkeur
                                            """)
    if hellingbaan_voorkeur_richting is not None:
        config.sub_parameter.append(("0891", hellingbaan_voorkeur_richting))
