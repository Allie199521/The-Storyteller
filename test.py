# storyteller.py
# alexandra miranda
# senior project

import sys
import character as c
import helpermethods as h
import nltk as nl
import PyDictionary as pd
import numpy as np
import matplotlib as mp

#h.readAWord()
allie = c.make_character("allie", False, 22)
print (allie)
allie.changeIsHuman(True)
print (allie)
allie.addCharacteristic(0, "eyes: blue")
allie.addCharacteristic(1, "shy")
allie.describe(0)
allie.describe(1)