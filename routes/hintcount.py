from models.users import Users
from routes.login import manager
from models.database import database
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/hintcount")


@router.get("/count")
async def get_hintcount(user=Depends(manager)):
    hintcount = database.query(Users).filter_by(email=user.email).one().hintcount
    hintcount += 1
    print(f"User: {user.email} - New hint count: {hintcount}")
    database.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "hintcount": hintcount
        }
    )
