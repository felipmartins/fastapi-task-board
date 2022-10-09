import pytest
from app.models.task_model import Task
from app.models.board_model import Board
from app.models.db import engine
from sqlmodel import Session, select

@pytest.mark.order(after="test_task_routes.py::test_delete_task_route")
def test_board_model():
    new_board = Board(title='test_title')
    assert hasattr(new_board, 'id')
    assert not hasattr(new_board, 'prazo_de_entrega')


mocked_board = Board(id=1000000000000000, title="string")


@pytest.mark.order(after="test_board_model")
def test_select_from_board_table():
    with Session(engine) as session:
        boards = list(session.exec(select(Board)))
        assert type(boards) == list


@pytest.mark.order(after="test_select_from_board_table")
def test_board_insertion_to_table():
    with Session(engine) as session:
        before_insertion_board = len(list(session.exec(select(Board))))
        session.add(mocked_board)
        session.commit()
        session.refresh(mocked_board)
        after_insertion_board = len(list(session.exec(select(Board))))

        assert after_insertion_board == before_insertion_board + 1


@pytest.mark.order(after="test_board_insertion_to_table")
def test_update_board_from_table():
    with Session(engine) as session:
        before_insertion_board = len(list(session.exec(select(Board))))
        board = session.exec(select(Board).where(Board.id == 1000000000000000)).one()
        board.title = "edited_test_title"
        session.add(board)
        session.commit()
        session.refresh(board)
        after_insertion_board = len(list(session.exec(select(Board))))
        
        assert after_insertion_board == before_insertion_board

@pytest.mark.order(after="test_delete_task_from_table")
def test_delete_board_from_table():
    with Session(engine) as session:
        before_insertion_board = len(list(session.exec(select(Board))))
        board = session.exec(select(Board).where(Board.id == 1000000000000000)).one()
        session.delete(board)
        session.commit()
        after_insertion_board = len(list(session.exec(select(Board))))
        
        assert after_insertion_board == before_insertion_board - 1

@pytest.mark.order(after="test_update_board_from_table")
def test_task_model():
    new_task = Task(title='test_title', description='test_description')
    assert hasattr(new_task, 'id')
    assert hasattr(new_task, 'create_date')
    assert hasattr(new_task, 'update_date')
    assert hasattr(new_task, 'status')
    assert not hasattr(new_task, 'prazo_de_entrega')


mocked_task = Task(id=1000000000000000, title="string", description= "string")

@pytest.mark.order(after="test_task_model")
def test_select_from_task_table():
    with Session(engine) as session:
        tasks = list(session.exec(select(Task)))
        assert type(tasks) == list

@pytest.mark.order(after="test_select_from_task_table")
def test_task_insertion_to_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        session.add(mocked_task)
        session.commit()
        session.refresh(mocked_task)
        after_insertion_tasks = len(list(session.exec(select(Task))))

        assert after_insertion_tasks == before_insertion_tasks + 1

@pytest.mark.order(after="test_task_insertion_to_table")
def test_update_task_from_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        task = session.exec(select(Task).where(Task.id == 1000000000000000)).one()
        task.title = "edited_test_title"
        task.description = "edited_test_title"
        session.add(task)
        session.commit()
        session.refresh(task)
        after_insertion_tasks = len(list(session.exec(select(Task))))
        
        assert after_insertion_tasks == before_insertion_tasks

@pytest.mark.order(after="test_update_task_from_table")
def test_delete_task_from_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        task = session.exec(select(Task).where(Task.id == 1000000000000000)).one()
        session.delete(task)
        session.commit()
        after_insertion_tasks = len(list(session.exec(select(Task))))
        
        assert after_insertion_tasks == before_insertion_tasks - 1