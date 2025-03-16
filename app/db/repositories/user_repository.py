from pymongo import MongoClient
from bson.objectid import ObjectId

class User:
    def __init__(self, db):
        self.collection = db['users']

    def create_user(self, username, password, emailid, phonenumber, first_name, last_name):
        user = {
            "username": username,
            "password": password,
            "emailid": emailid,
            "phonenumber": phonenumber,
            "first_name": first_name,
            "last_name": last_name
        }
        result = self.collection.insert_one(user)
        return str(result.inserted_id)

    def get_user(self, user_id):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return user

    def update_user(self, user_id, update_fields):
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_fields}
        )
        return result.modified_count

    def delete_user(self, user_id):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count