from fastapi import FastAPI
from app.models.db import engine
from app.routes import task_routes, board_routes


app = FastAPI()

app.include_router(board_routes.router)
app.include_router(task_routes.router)


@app.get("/", tags=["home"])
async def home():
    return {"info": "this is the index route of the task board API, use /board to interact with boards and /board/{id} to retrieve all tasks associated with the chosen board"}
