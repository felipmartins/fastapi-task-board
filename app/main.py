from fastapi import FastAPI
from app.models import db

app = FastAPI()


@app.get("/")
async def home():
    return {"info": "this is the index route of the task board API, use /board to interact with boards and /board/{id} to retrieve all tasks associated with the chosen board"}