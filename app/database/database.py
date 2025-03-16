# import motor.motor_asyncio
# from pymongo import mongo_client
# import pymongo
# from app.config import settings

# # client = mongo_client.MongoClient(settings.DATABASE_URL)
# client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
# print('Connected to MongoDB...')

# db = client[settings.MONGO_INITDB_DATABASE]
# User = db.users
# Sms = db.sms
# User.create_index([("email", pymongo.ASCENDING)], unique=True)
# Sms.create_index([("email", pymongo.ASCENDING)], unique=True)