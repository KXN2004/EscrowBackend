import datetime
from models.database import database
from models.users import Users
from routes.login import manager
from datetime import datetime, date, time
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/time")


@router.get("/start")
async def start(user=Depends(manager)):
    starting = Users(email=user.email).set_start()
    print(f"User: {user.name} - Started at {starting.strftime('%H:%M:%S')}")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "start_time": {
                "hours": starting.hour,
                "minutes": starting.minute,
                "seconds": starting.second
            }
        }
    )


@router.get("/sendtime")
async def sendtime(user=Depends(manager)):
    starting_time = Users(email=user.email).get_start()
    ending_time = Users(email=user.email).get_end()
    hintused = Users(email=user.email).get_hintcount()
    penalty = hintused * 30
    today = date.today()
    starting = datetime.combine(today, starting_time)
    ending = datetime.combine(today, ending_time)
    total_seconds = (ending - starting).total_seconds()
    total_time_second = total_seconds + penalty
    hours = int(total_time_second // 3600)
    minutes = int((total_time_second % 3600) // 60)
    seconds = int(total_time_second % 60)
    # Format the total time as HH:MM:SS
    total_time_second = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    print(f"User: {user.email} - Total time taken {total_time_second}")
    database.query(Users).filter_by(email=user.email).update({"totaltime": total_time_second})
    database.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "total_time": total_time_second
        }
    )
