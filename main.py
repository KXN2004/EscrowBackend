from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.login import router as login_route
from routes.start import router as start_route
from routes.storeline import router as storeline_route
from routes.hintcount import router as hintcount_route

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=login_route)
app.include_router(router=start_route)
app.include_router(router=storeline_route)
app.include_router(router=hintcount_route)
