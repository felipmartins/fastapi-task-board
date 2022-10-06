from fastapi import APIRouter
from app.models.db import engine
from app.models.board_model import Board
from sqlmodel import Session, select
router = APIRouter(prefix="/board", tags=["boards"])


@router.get("/")
async def list_boards():
    with Session(engine) as session:
        boards = select(Board)
        return list(session.exec(boards))


@router.post("/")
async def new_board(req_board: Board):
    with Session(engine) as session:
        session.add(Board(title=req_board.title))
        session.commit()
        return 'created'


@router.put("/{board_id}")
async def edit_board(board_id: int, req_board: Board):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == board_id)).one()
        board.title = req_board.title
        session.add(board)
        session.commit()
        session.refresh(board)
        return 'edited'


@router.delete("/{board_id}")
async def delete_board(board_id: int):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == board_id)).one()
        session.delete(board)
        session.commit()
        return 'deleted'
