from fastapi import APIRouter
from app.models.task_model import Task
from app.models.db import engine
from sqlmodel import Session, select

router = APIRouter(prefix="/board", tags=["tasks"])


@router.get("/{board_id}", status_code=200)
async def list_tasks_from_board(board_id: int):
    with Session(engine) as session:
        task = select(Task).where(Task.board_id == board_id)
        return list(session.exec(task))


@router.post("/{board_id}", status_code=201)
async def add_task_to_board(board_id: int, req_task: Task):
    with Session(engine) as session:
        new_task = req_task
        new_task.board_id = board_id
        session.add(new_task)
        session.commit()
        session.refresh(req_task)
        return {'message':'task created',
                'task': new_task}
          

@router.put("/{board_id}/{task_id}", status_code=200)
async def edit_task_from_board(board_id: int, task_id: int, req_task: Task):
    with Session(engine) as session:
        task = session.exec(select(Task).where(Task.board_id == board_id).where(Task.id == task_id)).one()
        task.title = req_task.title
        task.description = req_task.description
        session.add(task)
        session.commit()
        session.refresh(task)
        return {'message':'task edited',
                'task': task}

@router.delete("/{board_id}/{task_id}", status_code=200)
async def delete_task_from_board(board_id: int, task_id: int):
    with Session(engine) as session:
        task = session.exec(select(Task).where(Task.id == task_id)).one()
        session.delete(task)
        session.commit()
        return {'message':'task deleted'}