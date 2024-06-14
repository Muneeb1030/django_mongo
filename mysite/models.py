from pymongo import MongoClient


def get_db():
    client = MongoClient("")
    db = client['new_db']
    return db
