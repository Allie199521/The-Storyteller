#walkingskeleton.py
#by alexandra miranda
#senior project

##Book Structs:##

# readABook(bookname) -
# paramaters: book's name
# should be able to parse a book 
# and get the following data:
# title, obviously
# author
# most commonly used words
# sentiment chart && array
# sentence structures
# (maybe) get a summary from anther struct
def readABook(name):

# defineAWord(word)
# parameters: word
# should be able to find word
# can define and store the following:
# word
# parts of speach
# definition
# antonyms
# synonyms
# words most used before
# words most used after
def defineAword(word):

# sentanceStruct(sentance)
# parameters: a sentance [string]
# should be able to define:
# find part of speech (in context)
# build a [map] that tracks the sentance struct
# save this sentance struct in database
def sentanceStruct(sentance):

##Character Structs:##

# name = ""
# gender = True // true for male and false for female
# age = 0
# isHuman = True
# looksLike = []
# actsLike = []

# __init__(self, name, gender, age)
# parameters: self; char name, bool gender, int age
def __init__(self, name, gender, age):

# __init__(self, name, feature)
# parameters: self; char name, string feature
def __init__(self, name, feature):

# toString()
# returns a character's name/pronoun in an array
def toString(self):

# isHuman(bool)
# goes from true to false if character changes to not human
# parameter: a boolean (if goes from human to not human - false)
#				(if goes from not human to human - true)
def isHuman(self, bool):

# addCharacterisitic(self, id, fact)
# parameters: int id (either 0 or 1), string fact
# should be able to add the fact to the appropriate array
def addCharacterisitic(self, id, fact):

##Plurals Struct:##

# characters = new Character()

##Databases Required:##

# dictionary
	##contains##
	# words
	# definition
	# synonyms
	# antonyms
	# part of speech
	# relevant words (car --> drive)
	# words that come before (most often)
	# words that come after (most often)

# charteristics(looks)
	##contains:##
	# eye color(s)
	# hair color(s)
	# body type
	# hair type
	# face type
	# height
	# ~weight
	# backgrounds - where come from
		# will correlate with personality
			# shy == country; etc.

# personalities
	##contains##
	# different personality traits
	# a series of actions that would relate
	# maybe look into giving them personality types

# sentance structures
	##contains##
	# sentence structures
	# parts of speech

# books:
	##contains##
	# title
	# author
	# sentiment
	# common words
	# common sentance structs