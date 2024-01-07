from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from fastapi_training.Router import blog
from fastapi_training.Router import user


app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
fastapi_training = client.fastapi_training

app.include_router(blog.router)
app.include_router(user.router)