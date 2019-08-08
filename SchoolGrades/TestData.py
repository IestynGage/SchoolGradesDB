import pymongo
from pymongo import MongoClient

cluster = MongoClient()
db = cluster["school"]
collection = db["students"]

post1 = {"_id":0,"FName":"Peter","LName":"Parker","English":"A","Math":"A*","Science":"A*"}
post2 = {"_id":1,"FName":"Ryan","LName":"Jewels","English":"A*","Math":"C","Drama":"A"}
post3 = {"_id":2,"FName":"Kevin","LName":"Thomas","English":"D","Math":"C","RE":"C"}
post4 = {"_id":3,"FName":"Jim","LName":"Link","English":"E","Math":"B","French":"B"}
post5 = {"_id":4,"FName":"James","LName":"Gage","English":"C","Math":"C","Computer Science":"A*"}

post6 = {"_id":5,"FName":"Bob","LName":"Smith","English":"B","Math":"B","Chemistry":"C"}
post7 = {"_id":6,"FName":"John","LName":"McMorris","English":"C*","Math":"B","Theatre":"B"}
post8 = {"_id":7,"FName":"Ned","LName":"McDonald","English":"D","Math":"D","History":"A"}
post9 = {"_id":8,"FName":"Ben","LName":"Watermill","English":"A","Math":"A*","Spanish":"C"}
post10 = {"_id":9,"FName":"Sam","LName":"Parker","English":"C","Math":"C","Electronics":"B"}

list = [post1,post2,post3,post4,post5,post6,post7,post8,post9,post10]

collection.insert_many(list)
#print(collection.count())