from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.users import Users

router = APIRouter(prefix="/start")


@router.get("/")
async def start():
    starting = Users().get_start(),
    return JSONResponse(status_code=200, content=starting)
