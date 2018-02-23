# sentancestructures.py
# alexandra miranda
# senior project

from random import *
from pattern.en import conjugate, lemma, lexeme, referenced, article

verbs = ["run", "walk", "climb", "crawl", "sit"]
nouns = ["girl", "boy", "chicken", "cat", "dog", "apple"]
article = "the"
sentencestruct1 = ["past", "<art>", "<noun>", "<verb>"]
sentencestruct2 = ["pres", "<art>", "<noun>", "<verb>"]

def makeSent(struct):
	noun = randint(0, len(nouns)-1)
	verb = randint(0, len(verbs)-1)
	tense = ''
	if(struct[0] == "past"):
		tense = 'sgp'
	elif(struct[0] == "pres"):
		tense = 'sg'
	for i in range(1, len(struct)):
		#if(struct[i] == "<art>"):
			#print article + ' ',
		if(struct[i] == "<noun>"):
			print referenced(nouns[noun]) + ' ',
		elif(struct[i] == "<verb>"):
			print conjugate(verbs[verb], '3' + tense) + ' ',
	print "\n"

makeSent(sentencestruct1)
makeSent(sentencestruct2)