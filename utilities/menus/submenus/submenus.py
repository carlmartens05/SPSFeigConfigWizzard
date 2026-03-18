# imports
# == algemeen ==
from ...input_helpers import *
from ...parameter_logic import bereken_input_parameter_code


# ======================
# Submenu's
# ======================

# onderhouds intrval
from .onderhouds_interval import onderhouds_interval_menu
# auto sluittijd
from .auto_sluittijd import auto_sluittijd_menu
# motor instellingen
from .motor_instellingen import motor_instelling_menu
# zelftest
from .zelftest import zelftest_menu
# verkeerslichten
from .verkeerslichten import verkeerslichten_menu
# node id
from .node_id import node_id_menu
# heling baan regeling
from .heling_baan_regeling import heling_baan_regeling_menu
# loopsnelheden
from .loopsnelheden import loopsnelheden_OHD_menu
# BMI
from .bmi import BMI_menu
