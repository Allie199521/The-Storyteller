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

h.readABook()
#h.readAWord()
allie = c.make_character("allie", False, 22)
print (allie)
allie.changeIsHuman(False)
print (allie)