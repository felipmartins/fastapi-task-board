from fastapi import APIRouter

router = APIRouter(prefix="/board", tags=["boards"])


@router.get("/")
async def list_boards():
    return ...


@router.post("/")
async def new_board():
    return ...


@router.put("/")
async def edit_board():
    return ...


@router.delete("/")
async def delete_board():
    return ...