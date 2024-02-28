from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/user")


class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    email: str
    password: str


@router.post("/login")
async def login(login_data: UserLoginRequest):
    print(login_data.email, login_data.password)
