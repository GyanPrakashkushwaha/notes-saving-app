from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient
from config.secret import SECRET_KEY_MONGO_DB

app = FastAPI()


client = MongoClient(SECRET_KEY_MONGO_DB)
# print(client)



