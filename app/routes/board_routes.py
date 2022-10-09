from fastapi import APIRouter
from app.models.db import engine
from app.models.board_model import Board
from sqlmodel import Session, select
router = APIRouter(prefix="/board", tags=["boards"])


@router.get("/", status_code=200)
async def list_boards():
    with Session(engine) as session:
        boards = select(Board)
        return list(session.exec(boards))


@router.post("/", status_code=201)
async def new_board(req_board: Board):
    with Session(engine) as session:
        session.add(req_board)
        session.commit()
        session.refresh(req_board)
        return {'message':'board created',
                'board': req_board}


@router.put("/{board_id}", status_code=200)
async def edit_board(board_id: int, req_board: Board):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == board_id)).one()
        board.title = req_board.title
        session.add(board)
        session.commit()
        session.refresh(board)
        return {'message':'board edited',
                'board': board}


@router.delete("/{board_id}", status_code=200)
async def delete_board(board_id: int):
    with Session(engine) as session:
        board = session.exec(select(Board).where(Board.id == board_id)).one()
        session.delete(board)
        session.commit()
        return {'message':'board deleted'}
