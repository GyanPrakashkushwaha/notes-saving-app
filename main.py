from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from secret import SECRET_KEY_MONGO_DB

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # this is for rendering CSS codes
templates = Jinja2Templates(directory="templates") # this is to use Jinja2Templates to render the HTLM file inside the templates templates directory

client = MongoClient(SECRET_KEY_MONGO_DB)
# print(client)


@app.get("/", response_class=HTMLResponse) 
async def read_item(request: Request): # this function is a function of fastapi library to read stuff in the http requests.
    docs = client.notesSaving.notesSavingApp.find_one({})
    print(docs)
    return templates.TemplateResponse("index.html", {"request": request, 'docs' :docs}) # by this I am rendering everything in my webpage.


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
