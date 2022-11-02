from pymongo import MongoClient


client = MongoClient("mongodb+srv://Kyahyr:TQgTHidODc5Vh8Nn@cluster0.lcvaumm.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name = db["todos_app"]