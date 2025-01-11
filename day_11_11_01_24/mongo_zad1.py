# MongoDB to open-source'owa, dokumentowa baza danych typu NoSQL dostępna na różne platformy.
# Wykorzystuje format JSON z opcjonalnymi schematami i jest rozwijana przez MongoDB Inc.
# nosql
# https://www.ovhcloud.com/pl/learn/what-is-mongodb/
# docker pull mongo
# docker run --name mongodb -d -p 27017:27017 mongo
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print(mydb.list_collection_names())
