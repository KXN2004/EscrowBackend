from models.database import database
from models.users import Users
from config import SECRET

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from pydantic import BaseModel

router = APIRouter(prefix="/user")
manager = LoginManager(SECRET, "/user/login")


class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    email: str
    password: str


@manager.user_loader()
def query_user(email_id):
    return database.query(Users).filter_by(email=email_id).one()


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        print("User not found")
        raise InvalidCredentialsException
    elif password != user.password:
        print("Password does not match")
        raise InvalidCredentialsException
    else:
        access_token = manager.create_access_token(data={"sub": email})
        return JSONResponse(
            content={"access_token": access_token, "token_type": "bearer"}
        )


@router.post("/verify")
async def data(user=Depends(manager)):
    return JSONResponse(
        status_code=200,
        content="You are logged in as " + user.email
    )
