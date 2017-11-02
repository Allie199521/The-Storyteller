# character.py
# alexandra miranda
# senior project

# gender = true or false, true = female; false = male
class Character:
	name = ""
	gender = True
	age = 0
	isHuman = True
	looksLike = []
	actsLike = []
	
	#initialize a character
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
		self.looksLike = looksLike()
		self.actsLike = acts()
	
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

	def addCharacteristic(self, id, fact):
		if(id == 0):
			
		

#method to define character(Supposedly)
def make_character(name, gender, age):
	char = Character(name, gender, age)
	return char