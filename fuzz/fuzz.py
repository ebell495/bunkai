#!/bin/python3

import atheris
import sys
from janome import *

# with atheris.instrument_imports():
from bunkai import Bunkai
from bunkai.algorithm.bunkai_sbd.bunkai_sbd import BunkaiSentenceBoundaryDisambiguation


@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    if len(barray) > 0:
        if barray[0] % 5 == 0:
            del barray[0]
            bunkai = Bunkai()
            bunkai(str(barray))
        elif barray[0] % 5 == 1:
            del barray[0]
            bunkai = BunkaiSentenceBoundaryDisambiguation(path_model=None)
            bunkai(str(barray))
        elif barray[0] % 5 == 2:
            del barray[0]
            bunkai = BunkaiSentenceBoundaryDisambiguation(path_model=None)
            bunkai.find_eos(str(barray))
        elif barray[0] % 5 == 3:
            del barray[0]
            bunkai = BunkaiSentenceBoundaryDisambiguation(path_model=None)
            an_obj = bunkai.eos(str(barray))
            layers = an_obj.get_morph_analysis()
        else:
            del barray[0]
            bunkai = BunkaiSentenceBoundaryDisambiguation(path_model=None)
            an_obj = bunkai.eos(str(barray))
            layers = an_obj.available_layers()
    else:
        bunkai = Bunkai()
        bunkai(str(barray))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()