from fastapi import FastAPI
from app.models.db import engine

app = FastAPI()

@app.get("/")
async def home():
    return {"info": "this is the index route of the task board API, use /board to interact with boards and /board/{id} to retrieve all tasks associated with the chosen board"}


@app.get("/board")
async def list_boards():
    return ...


@app.post("/board")
async def new_board():
    return ...


@app.put("/board")
async def edit_board():
    return ...


@app.delete("/board")
async def delete_board():
    return ...

@app.get("/board/{board_id}")
async def list_board_tasks():
    return ...


@app.post("/board/{board_id}")
async def add_task_to_board():
    return ...

@app.put("/board/{board_id}/{task_id}{")
async def edit_task_from_board():
    return ...

@app.delete("/board/{board_id}/{task_id}{")
async def delete_task_from_board():
    return ...