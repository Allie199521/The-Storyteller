# storyteller.py
# alexandra miranda
# senior project

import sys
import character as c
import nltk as nl
import PyDictionary as pd
import numpy as np
import matplotlib as mp
import bookstructs as bs

allie = c.make_character("allie", False, 22)
print (allie)
allie.changeIsHuman(True)
print (allie)
dic = {('hello', 'goodbye')}
dic.add(('ciao', 'woah'))
allie.addCharacteristic(0, 'eyes: blue')
allie.describe(0)
bs.sentiment()
bs.readABook()