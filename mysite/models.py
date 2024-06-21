from pymongo import MongoClient
import os
from django.conf import settings

def get_db():
    """
    Returns a connection to the MongoDB database.
    
    This function connects to the MongoDB database using the provided
    connection string and returns the database object.
    
    Returns:
        pymongo.MongoClient: A connection to the MongoDB database.
    """
    
    # Connect to the MongoDB database
    client = MongoClient(settings.MONGO_URI)
    
    # Get the 'new_db' database from the client
    db = client['new_db']
    
    # Return the database object
    return db