# helpermethods.py
# alexandra miranda
# senior project

import sys
import nltk as nl
import numpy as np
import matplotlib as mt

#reads a book
def readABook():
	file = input("What book should I read? ")
	inputfile = open(file)
	outputfile = open(file+".txt", 'w')
	word1 = ""
	for word in inputfile.split():
		outputfile.write(line)
		word1 = word
	print(word)

def sentiment():
	


#finds the sentence structures		
def sentenceStructs():
	return 0