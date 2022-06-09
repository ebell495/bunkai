#!/usr/local/bin/python3 

import atheris
import sys

# with atheris.instrument_imports():
from bunkai import Bunkai
from bunkai.algorithm.bunkai_sbd.bunkai_sbd import BunkaiSentenceBoundaryDisambiguation

bun = Bunkai()
bun1 = BunkaiSentenceBoundaryDisambiguation(path_model=None)

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 5 == 0:
        bun(in_string)
    elif option % 5 == 1:
        bun1(in_string)
    elif option % 5 == 2:
        bun1.find_eos(in_string)
    elif option % 5 == 3:
        an_obj = bun1.eos(in_string)
        layers = an_obj.get_morph_analysis()
    else:
        an_obj = bun1.eos(in_string)
        layers = an_obj.available_layers()


atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()