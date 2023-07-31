# notes-saving-app

---
## Base Code... With explaination


```
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

# Mounting the "/static" path to serve static files (CSS, JS, images, etc.) from the "static" directory.
# This allows you to access static files like CSS in your HTML templates.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setting up the Jinja2Templates to render HTML templates from the "templates" directory.
templates = Jinja2Templates(directory="templates")

# Creating a MongoDB client to connect to the database.
# Replace the connection string with your actual MongoDB connection string.
client = MongoClient('mongodb+srv://GyanPrakashKushwaha:GyanPrakashKushwaha@notes-saving-app.e7roz38.mongodb.net/notes-saving-app')

# Defining the root path ("/") route for the application.
@app.get("/", response_class=HTMLResponse) 
async def read_items(request: Request):
    # Querying the MongoDB database to find one document in the "notesSavingApp" collection.
    docs = client.notesSaving.notesSavingApp.find_one({})
    print(docs)  # Printing the retrieved document for debugging purposes.
    
    # Rendering the "index.html" template with the provided data.
    # The "request" object is passed to access request-specific information in the template.
    # The "docs" object is passed to be used in the template.
    return templates.TemplateResponse("index.html", {"request": request, "docs": docs})

# Defining another route for "/items/{item_id}" path.
# This function will be executed when a request is made to this path with an "item_id" parameter.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # The function takes "item_id" as a path parameter and "q" as a query parameter (optional).
    # It returns a dictionary containing the "item_id" and "q" values in the response.
    # For example, if you access "/items/123?q=test", it will return:
    # {"item_id": 123, "q": "test"}
    return {"item_id": item_id, "q": q}
```