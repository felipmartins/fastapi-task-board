from datetime import datetime
from app.models.board_model import Board
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional

class Status(str, Enum):
    pending = "pending"
    doing = "doing"
    done = "done"


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    board_id: Optional[int] = Field(default=None, foreign_key="board.id")
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()
    title: str
    description: str
    status: Status = Field(default=Status.pending)