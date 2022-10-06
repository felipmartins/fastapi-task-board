from . import board_model, task_model
from sqlmodel import  SQLModel, create_engine, Session


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

def test_board_insertion():
    board = board_model.Board(title='Board do Felps')
    with Session(engine) as session:
        session.add(board)
        session.commit()

def test_task_insertion():
    task = task_model.Task(board_id = 1, title='Task do Felps', description='Description of Task do Felps')
    with Session(engine) as session:
        session.add(task)
        session.commit()

test_board_insertion()
test_task_insertion()