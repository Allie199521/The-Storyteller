# makedb.py
# alexandra miranda
# senior project

from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.admin

books = db["Books"]