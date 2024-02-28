from fastapi import FastAPI
from routes.login import router as user_login_route

app = FastAPI()

app.include_router(router=user_login_route)
