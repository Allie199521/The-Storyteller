# helpermethods.py
# alexandra miranda
# senior project

import sys
import nltk as nl
import numpy as np
import matplotlib as mt
from textblob import TextBlob

#reads a book
def readABook():
	file = input("What book should I read? ")
	inputfile = open(file)
	outputfile = open(file+".txt", 'w')
	for word in inputfile.split():
		outputfile.write(word)
	print(word)

# provides the sentiment of a given sentence
def sentiment():
	sent = "this candy is good"
	sent1 = TextBlob(sent)
	print (sent1.sentiment.polarity)

#finds the sentence structures		
def sentenceStructs():
	return 0