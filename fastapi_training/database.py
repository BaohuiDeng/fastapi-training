from pymongo import MongoClient


DB_NAME = 'fastapi_training'

db_connection = MongoClient('mongodb://localhost:27017/')

fastapi_training = db_connection[DB_NAME]