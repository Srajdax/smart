import pymongo
from bson.objectid import ObjectId
import cerberus

from cerberus import Validator

# database connection
client = pymongo.MongoClient("localhost", 27017)
db = client.smile


class Factory:

    client = client

    def __init__(self, collections):
        self.collections = collections

    # Self operations
    def getCollections(self):
        return [x.name for x in self.collections]

    # Create Operations

    def insertOne(self, collection, data):
        """
        Insert a document into the `collection` specified in argument

        returns:
            Inserted data with the ObjectId
        """
        collection = db[collection.name]
        index = collection.insert_one(data)
        return collection.find_one({'_id': index.inserted_id})

    def insertMany(self, collection, data, load=False):
        """
        Insert many documents into the `collection` specified in argument
        with the data parameters

        returns:
            If load==True: Inserted datas with the ObjectId
            Else: default pymongo return
        """
        collection = db[collection.name]
        indexes = collection.insert_many(data)
        if load:
            cursor = collection.find({'_id': {'$in': indexes.inserted_ids}})
            return cursor
        return indexes

    # Read Operations

    def findOne(self, collection, data):
        """
        Find a document of the `collection` specified in argument
        with data as parameters
        """
        collection = db[collection.name]
        return collection.find_one(data)

    def findOneById(self, collection, index):
        """
        Find a document of the `collection` specified in argument
        with the Id
        """
        collection = db[collection.name]
        return collection.find_one({'_id': ObjectId(index)})

    def findAll(self, collection, pageSize=False, page=False):
        """
        Find all the corresponding documents with the specified `pageSize`,
        number of `page`

        returns: all the documents
        """
        collection = db[collection.name]
        if page:
            last_id = None
            for i in range(page):
                if not last_id:
                    cursor = collection.find().limit(pageSize)
                else:
                    cursor = collection.find(
                        {'_id': {'$gt': last_id}}).limit(pageSize)
                data = [x for x in cursor]
                if not data:
                    return None
                last_id = data[-1]['_id']

            return data
        return [x for x in collection.find()]

    def find(self, collection, data, pageSize=False, page=False):
        """
        Find all the corresponding documents with the specified `pageSize`,
        number of `page` and the specified data

        returns: all the documents
        """
        collection = db[collection.name]
        if page:
            last_id = None
            for i in range(page):
                if not last_id:
                    cursor = collection.find(data).limit(pageSize)
                else:
                    data['_id'] = {'$gt': last_id}
                    cursor = collection.find(data).limit(pageSize)
                r = [x for x in cursor]
                if not r:
                    return None
                last_id = r[-1]['_id']

            return r
        return [x for x in collection.find(data)]

    # Update Operations
    def updateOne(self, collection, query, data, projection=None):
        """
        Update the document of the `collection` matching the query

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.find_one_and_update(query, data, projection=projection,
                                              return_document=pymongo.ReturnDocument.AFTER)

    def updateOneById(self, collection, index, data, projection=None):
        """
        Update the document of the `collection`  matching the `index`

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.find_one_and_update({'_id': ObjectId(index)}, data, projection=projection,
                                              return_document=pymongo.ReturnDocument.AFTER)

    def updateMany(self, collection, query, data, projection=None):
        """
        Update the document of the `collection` matching the query

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.update_many(query, data)

    def replaceOne(self, collection, query, data, projection=None):
        """
        Replace the document of the `collection`  matching the `index`

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.find_one_and_replace(query, data, projection=projection,
                                               return_document=pymongo.ReturnDocument.AFTER)

    def replaceOneById(self, collection, index, data, projection=None):
        """
        Replace the document of the `collection`  matching the `index`

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.find_one_and_replace({'_id': ObjectId(index)}, data, projection=projection,
                                               return_document=pymongo.ReturnDocument.AFTER)

    # Delete Operations

    def deleteOne(self, collection, query, projection=None):
        """
        Delete the document of the `collection`  matching the `query`

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.find_one_and_delete(query, projection=projection)

    def deleteMany(self, collection, query):
        """
        Delete the documents of the `collection`  matching the `query`

        returns: the updated document
        """
        collection = db[collection.name]
        return collection.delete_many(query)

    # Other functions

    def raw(self):
        return client
