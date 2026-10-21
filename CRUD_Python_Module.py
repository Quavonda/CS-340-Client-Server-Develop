# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ Provides CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(
            host=HOST,
            port=PORT,
            username=USER,
            password=PASS,
            authSource='admin'
        )
                                    
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        #Make sure data was provided before attempting an insert
        if data is not None:
            try:
                # Insert the documents into the animals collection
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                # Handle an error without crashing the program
                print(f"An error occurred while creating the documents: {e}")
                return False
        else:
            # Returns False when there is no document to insert
            print("Nothing to save, because data parameter is empty.")
            return False

    # Read method to implement the R in CRUD.
    def read(self, query):
        # Make sure a query was provided before searching the database
        if query is not None:
            try:
                # find() returns a MongoDB cursor containing matching documents
                cursor = self.database.animals.find(query)
                
                # Convert the cursor to a list before returning the results
                return list(cursor)
            except Exception as e:
                # Return an empty list if the query cannot be completed
                print(f"An error occurred while reading the documents: {e}")
                return[]
            else:
                # Return an empty list when there is no query to perform
                print("Nothing to search because the query parameter is empty.")
                return[]
            
    # Update matching document(s) in the animals collection
    def update(self, query, new_data):
        # Make sure both the search query and new data were provided
        if query is not None and new_data is not None:
            try:
                # Update all documents that match the search query
                result = self.database.animals.update_many(
                    query,
                    {"$set": new_data}
                )
                
                # Return the number of documents that were changed
                return result.modified_count
            
            except Exception as e:
                # Return 0 if the update cannot be complete
                print(f"An error occurred while updating the documents: {e}")
                return 0
            else:
                print("Nothing to update because a parameter is empty.")
                return 0
            
    # Delete matching document(s) from the animal collection
    def delete(self, query):
        # Make sure a query was provided before deleting documents
        if query is not None:
            try:
                # Delete all documents that match the search query
                result = self.database.animals.delete_many(query)
                
                # Return the number of documents that were removed 
                return result.deleted_count
            
            except Exception as e:
                # Return 0 if the delete cannot be completed
                print(f"An error occurred while deleting the documents: {e}")
                return 0
        else:
            print("Nothing to delete because the query parameter is empty,")
            return 0          