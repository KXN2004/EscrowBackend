from fastapi import FastAPI
from routes.login import router as user_login_route

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=user_login_route)
