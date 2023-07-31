from pymongo import MongoClient
from config.secret import SECRET_KEY_MONGO_DB

client = MongoClient(SECRET_KEY_MONGO_DB)

