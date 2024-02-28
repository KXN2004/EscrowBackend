from fastapi import APIRouter , HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from models.users import Users
from models.database import database

router = APIRouter(prefix="/user")
SECRET = "3f4e1462c7bda198adf757f33f354e45672333c29613c645"
manager = LoginManager(SECRET, "/user/login", use_cookie=True)

@manager.user_loader()
def query_user(email: str):
    user = database.query(Users).filter(Users.email == email).first()
    return user


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"sub": email})
    manager.set_cookie(access_token)
    print(access_token)
    return {"status": "Success"}
