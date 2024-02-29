from models.users import Users
from routes.login import manager

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/time")


@router.get("/start")
async def start(user=Depends(manager)):
    starting = Users(email=user.email).set_start()
    return JSONResponse(
        status_code=200,
        content={
            "start_time": {
                "hours": starting.hour,
                "minutes": starting.minute,
                "seconds": starting.second
            }
        }
    )
