from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

DATABASE_URL = 'mongodb://localhost:27017'
DATABASE_NAME = 'tallyUp'

client = AsyncIOMotorClient(DATABASE_URL) # use this 
database = client[DATABASE_NAME]

sync_client = MongoClient(DATABASE_URL)
sync_database = sync_client[DATABASE_NAME]

def get_db():
    try:
        yield database

    except Exception as e:
        print("Unable to create MongoDB client due to, {}".format(e))

    finally:
        client.close()

def get_sync_db():
    try:
        yield sync_database

    except Exception as e:
        print("Unable to create SYNC MongoDB client due to, {}".format(e))

    finally:
        sync_client.close()

