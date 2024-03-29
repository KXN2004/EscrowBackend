from datetime import datetime, timedelta

from models.database import database
from models.users import Users
from config import SECRET

from pydantic import BaseModel
from sqlalchemy.exc import NoResultFound
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

router = APIRouter(prefix="/user")
manager = LoginManager(SECRET, "/user/login")


class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    email: str
    password: str


@manager.user_loader()
def query_user(email_id):
    try:
        return database.query(Users).filter_by(email=email_id).one()
    except NoResultFound:
        raise NoResultFound("User not found")


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username.lower()
    password = data.password

    try:
        user = query_user(email)
    except NoResultFound:
        print("User not found")
        raise InvalidCredentialsException

    if password != user.password:
        print(f"User: {user.name} - Incorrect password")
        raise InvalidCredentialsException
    else:
        access_token = manager.create_access_token(data={"sub": email}, expires=timedelta(hours=3))
        starting = Users(email=user.email).get_start()
        now = datetime.utcnow() + timedelta(hours=5, minutes=30)
        print(f"User: {user.name} - Logged in at {now.strftime('%H:%M:%S')}")
        if not starting:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": access_token,
                    "token_type": "bearer",
                    "start_time": None
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": access_token,
                    "token_type": "bearer",
                    "start_time": {
                        "hours": starting.hour,
                        "minutes": starting.minute,
                        "seconds": starting.second
                    }
                }
            )


@router.post("/verify")
async def data(user=Depends(manager)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="You are logged in as " + user.email
    )
