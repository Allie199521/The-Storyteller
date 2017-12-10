# helpermethods.py
# alexandra miranda
# senior project

import sys
import nltk as nl
import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
from textblob import TextBlob

arr = []

#reads a book
def readABook():
	file1 = raw_input("What book should I read? ")
	inputfile = open(file1)
	for line in inputfile:
		sentiment(line)
	arr = section()
	print arr
	plt.plot(arr)
	plt.show()

# provides the sentiment of a given sentence
def sentiment(sent):
	sent1 = TextBlob(sent)
	arr.append(sent1.sentiment.polarity)

#finds the sentence structures		
def sentenceStructs():
	return 0

#average out sections of sentiment
def section():
	print len(arr)
	size = int(np.floor(len(arr)/100))
	i = 0
	temp = []
	arr1 = []
	for x in arr:
		temp.append(x)
		i+=1
		if i == size:
			arr1.append(np.average(temp))
			temp = []
			i = 0
	return arr1