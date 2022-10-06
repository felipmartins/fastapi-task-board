from fastapi import APIRouter
from app.models.db import engine
from app.models.board_model import Board
from sqlmodel import Session, select
router = APIRouter(prefix="/board", tags=["boards"])


@router.get("/")
async def list_boards():
    with Session(engine) as session:
        boards = select(Board)
        query_result = session.exec(boards)
        return list(query_result)


@router.post("/")
async def new_board(req_board: Board):
    with Session(engine) as session:
        new_board = Board(title=req_board.title)
        session.add(new_board)
        session.commit()
        return 'created'


@router.put("/{id}")
async def edit_board(id: int, req_board: Board):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == id)).one()
        board.title = req_board.title
        session.add(board)
        session.commit()
        session.refresh(board)
        return 'edited'


@router.delete("/{id}")
async def delete_board(id: int):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == id)).one()
        session.delete(board)
        session.commit()
        return 'deleted'
