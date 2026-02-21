from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        if username and password:
            self.username = username
            self.password = password
            USER = username
            PASS = password
            HOST = 'localhost'
            PORT = 27017
            DB = 'aac'
            COL = 'animals'
            # Authenticate against the admin database
            self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
        else:
            # Fallback for unauthenticated access
            self.client = MongoClient('mongodb://localhost:27017')
            self.database = self.client['aac']
            self.collection = self.database['animals']

    def create(self, data):
        """
        Inserts a document into the specified MongoDB database and collection.
        :param data: A dictionary containing key/value pairs to insert
        :return: True if successful insert, else False
        """
        if data is not None:
            try:
                insert_result = self.collection.insert_one(data)
                return True if insert_result.acknowledged else False
            except Exception as e:
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """
        Queries for documents from the specified MongoDB database and collection.
        :param query: A dictionary containing key/value pairs for lookup
        :return: A list of documents matching the query, or an empty list if failed
        """
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"An error occurred during read: {e}")
                return []
        else:
            return []

    def update(self, query, data):
        """
        Queries for and changes document(s) from a specified MongoDB database and specified collection.
        """
        if query is not None:
            try:
                result = self.collection.update_many(query, {"$set": data})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Nothing to update, because query parameter is empty")

    def delete(self, query):
        """
        Queries for and removes document(s) from a specified MongoDB database and specified collection.
        """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")