# character.py
# alexandra miranda
# senior project

import sys
import dictionaries
from array import *

looksLike = {()}
actsLike = {()}

class Character:
	name = ""
	gender = True 	# gender = true or false, false = female; true = male
	age = 0
	isHuman = True
	
	#initialize a character
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age

	#print out the character's name
	def __str__(self):
		return self.name + " %s %s %s" %(self.gender, self.age, self.isHuman)

	#changes a character's age
	def changeAge(self, newage):
		self.age = newage
		
	#changes whether or not the character is human
	def changeIsHuman(self, isHuman):
		self.isHuman = isHuman

	#takes user input to request characteristics or chooses randomly
	def looksLike(self):
		return 0

######################################Needs Work############################################
	# this adds a charaterisitc to the proper
	# id = 0 - lookslike[]
	# id = 1 - actslike[]
	def addCharacteristic(self, id, fact):
		words = fact.split()
		fact1 = words[0]
		fact2 = words[1]
		if(id == 0):
			looksLike.add((fact1, fact2))
		elif (id == 1):
			actsLike.add((fact1, fact2))

	def describe(self, id):
		if(id == 0):
			print looksLike
		elif (id == 1):
			print actsLike
#############################################################################################
			
#method to define character
def make_character(name, gender, age):
	char = Character(name, gender, age)
	return char