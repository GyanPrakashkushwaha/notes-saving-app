from typing import Union
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import client

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse) 
async def read_item(request: Request):
    docs = list(client.notesSaving.notesSavingApp.find({}))

    docs_new = []
    for item in docs:
        # Use get method to access the values and provide a default value of an empty string
        docs_new.append({
            "_id": str(item["_id"]),
            "title": str(item.get('title')),
            "desc": str(item.get("item")),
            "item": str(item.get("important"))
        })

    return templates.TemplateResponse("index.html", {"request": request, 'docs': docs_new})


@note.post("/")
async def create_item(request :Request):
    form = await request.form()

    form_dict = dict(form)

    form_dict['important'] = True if form_dict.get('important') == 'on' else False

    note = client.notesSaving.notesSavingApp.insert_one(form_dict)
    
    return {'sucess':True}


