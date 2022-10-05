from fastapi import APIRouter

router = APIRouter(prefix="/board", tags=["tasks"])


@router.get("/{board_id}")
async def list_tasks_from_board():
    return ...


@router.post("/{board_id}")
async def add_task_to_board():
    return ...

@router.put("/{board_id}/{task_id}{")
async def edit_task_from_board():
    return ...

@router.delete("/{board_id}/{task_id}{")
async def delete_task_from_board():
    return ...