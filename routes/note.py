from fastapi import APIRouter
from models.note import Note

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.db import conn
from schemas.note import note_entity, notes_entity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    # docs = conn.notes.notes.find_one({})
    # print(docs)

    docs = conn.notes.notes.find()
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })

    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()

    formdict = dict(form)
    # This will give error if user does not check it as there will no key named important.
    formdict["important"] = True if formdict["important"] == "on" else False

    inserted_note = conn.notes.notes.insert_one(formdict)
    return {"Success": True}
