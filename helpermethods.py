# helpermethods.py
# alexandra miranda
# senior project

import sys

def readABook():
	file = input("What book should I read? ")
	inputfile = open(file)
	outputfile = open(file+".txt", 'w')
	for line in inputfile:
		outputfile.write(line)