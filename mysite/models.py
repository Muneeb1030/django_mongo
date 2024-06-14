from pymongo import MongoClient


def get_db():
    client = MongoClient("mongodb+srv://admin:myhomePassword@cluster0.m5kp7d2.mongodb.net/")
    db = client['new_db']
    return db
