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
# parameters: self; char name, bool gender, int age
def __init__(self, name, gender, age):

# toString()
# returns a character's name/pronoun in an array
def toString(self):

# isHuman(bool)
# goes from true to false if character changes to not human
# parameter: a boolean (if goes from human to not human - false)
#				(if goes from not human to human - true)
def isHuman(self, bool):