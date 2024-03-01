from models.users import Users
from routes.login import manager
from models.database import database
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/hintcount")


@router.get("/count")
async def get_hintcount(user=Depends(manager)):
    hintcount = database.query(Users).filter_by(email=user.email).one().hintcount
    print(hintcount)
    newhintcount = hintcount +1
    database.query(Users).filter_by(email=user.email).update({"hintcount": newhintcount})
    database.commit()
    return JSONResponse(
        status_code=200,
        content={
            "hintcount": newhintcount
        }
    )
