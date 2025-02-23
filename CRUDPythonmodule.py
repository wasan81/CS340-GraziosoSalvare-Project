from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # Parameters: username, password, host, port, db, and collection

        # Connection Variables
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.collection = collection

        # Initialize Connection
        self.client = MongoClient(f'mongodb://{self.username}:{self.password}@{self.host}:{self.port}')
        self.database = self.client[self.db]
        self.collection = self.database[self.collection]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, data=None):
        if data is None:
            raise Exception("Data parameter is empty, nothing to search for.")
            
        if not isinstance(data, dict):
            raise Exception("Invalid data format. Expected a dictionary.")
        
        results = list(self.collection.find(data))   
    
        # Return the results (even if empty)
        return results

    
# Update method to implement the U in CRUD
    def update(self, searchData, updateData, update_many=False):
        if searchData is None or updateData is None:
            raise Exception("Search criteria and update data cannot be empty.")
        
        if update_many:
            result = self.collection.update_many(searchData, {"$set": updateData})
        else:
            result = self.collection.update_one(searchData, {"$set": updateData})

        # Check how many documents were matched and modified
        print(f"Matched count: {result.matched_count}, Modified count: {result.modified_count}")
        
        return result.modified_count
    
# Delete method to implement the D in CRUD
    def delete(self, deleteData, delete_many=False):
        if not isinstance(deleteData, dict) or not deleteData:
            raise ValueError("Delete criteria must be a non-empty dictionary.")

        if delete_many:
            result = self.collection.delete_many(deleteData)
        else:
            result = self.collection.delete_one(deleteData)

        # Check how many documents were deleted
        print(f"Deleted count: {result.deleted_count}")
        
        return result.deleted_count

  
