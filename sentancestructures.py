# sentancestructures.py
# alexandra miranda
# senior project

from random import *

verbs = ["runs", "walks", "climbs", "crawls", "sits"]
nouns = ["girl", "boy", "chicken", "cat", "dog"]
article = "the"
sentencestruct1 = ["<art>", "<noun>", "<verb>"]

def makeSent():
	noun = randint(0, length(verbs))
	verb = randint(0, length(nouns))
	for i in range(0, length(sentencestruct1)):
		if(sentencestruct1[i] == "<art>"):
			print article
		elif(sentencestruct1[i] == "<noun>"):
			print nouns[noun]
		elif(sentencestruct1[i] == "<verb>"):
			print verbs[verb]

makeSent()