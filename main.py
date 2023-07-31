from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from config.secret import SECRET_KEY_MONGO_DB

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # this is for rendering CSS codes
templates = Jinja2Templates(directory="templates") # this is to use Jinja2Templates to render the HTLM file inside the templates templates directory

client = MongoClient(SECRET_KEY_MONGO_DB)
# print(client)


@app.get("/", response_class=HTMLResponse) 
async def read_item(request: Request):
    docs = list(client.notesSaving.notesSavingApp.find({}))

    docs_new = []
    for i in docs:
        # Use a try-except block to handle conversion to integer and set a default value of 0
        try:
            ratings = int(i["ratings"])
        except (ValueError, KeyError):
            ratings = 0  # Set a default value of 0 if "ratings" is missing or cannot be converted to an integer

        docs_new.append({
            'id': i["_id"],
            'name': i["name"],
            'ratings': ratings,
            'price': i['price'],
            'imgURL': i['imgURL'],
            # 'storage_ram': i['storage_ram'],
            # 'camera': i['camera'],
            # 'oS_Processor': i['oS_Processor'],
            # 'display': i['display'],
            # 'network': i['network'],
            # 'battery': i['battery'],
        })

    return templates.TemplateResponse("index.html", {"request": request, 'docs': docs_new})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
