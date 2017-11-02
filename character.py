# character.py
# alexandra miranda
# senior project


class Character:
	name = ""
	gender = True 	# gender = true or false, false = female; true = male
	age = 0
	isHuman = True
	looksLike = []
	actsLike = []
	
	#initialize a character
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
		self.looksLike = []
		self.actsLike = []

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

	# this adds a charaterisitc to the proper
	# id = 0 - lookslike[]
	# id = 1 - actslike[]
#	def addCharacteristic(self, id, fact):
#		if(id == 0):
#			looksLike.append(fact)
#		elif (id == 1):
#			actsLike.append(fact)
#
#	def describe(self, id):
#		if(id == 0):
#			print looksLike
#		elif (id == 1):
#			print actsLike
			

#method to define character
def make_character(name, gender, age):
	char = Character(name, gender, age)
	return char