# helpermethods.py
# alexandra miranda
# senior project

import sys
import nltk as nl
from nltk import pos_tag, word_tokenize
import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

arr = []
sentances = {}
ana = SentimentIntensityAnalyzer()

#reads a book
def readABook():
	file1 = raw_input("What book should I read? ")
	inputfile = open(file1)
	line = inputfile.readline()
	while line:
		sentiment(line)
	sentenceStructs(line)
	arr = section()
	plt.plot(arr)
	plt.show()

# provides the sentiment of a given sentence
def sentiment(sent):
	score = ana.polarity_scores(sent)
	arr.append(score['compound'])

#finds the sentence structures		
def sentenceStructs(sent):
	txt = word_tokenize(sent)
	print nl.pos_tag(txt)

#average out sections of sentiment
def section():
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