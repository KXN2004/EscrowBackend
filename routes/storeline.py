from pydantic import BaseModel

from models.users import Users
from routes.login import manager
from models.database import database
from models.games import *
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/question")

@router.get("/")
async def question(user=Depends(manager)):
    progress = database.query(Users).filter_by(email=user.email).one().progress
    return JSONResponse(
        status_code=200,
        content={
            "Question Number": progress
        }
    )


@router.get("/{progress}")
async def question_progress(progress: int, user=Depends(manager)):
    storyline = database.query(Users).filter_by(email=user.email).one().storyline
    stories = {
        "digital" : Digital,
        "harrypotter" : HarryPotter,
        "pirates" : Pirates,
        "zodiac" : Zodiac,
    }
    question = database.query(stories[storyline]).filter_by(qnum=progress).one().question
    return JSONResponse(
        status_code=200,
        content={
            "Question": question
        }
    )


class Answer(BaseModel):
    answer: str

@router.post("/{progress}")
async def answer_progress(progress: int, answer_data: Answer, user=Depends(manager)):
    storyline = database.query(Users).filter_by(email=user.email).one().storyline
    stories = {
        "digital" : Digital,
        "harrypotter" : HarryPotter,
        "pirates" : Pirates,
        "zodiac" : Zodiac,
    }
    correct = database.query(stories[storyline]).filter_by(qnum=progress).one().answer
    if answer_data.answer.lower() == correct.lower():
        database.query(Users).filter_by(email=user.email).update({"progress": progress+1})
        database.commit()
        return JSONResponse(
            status_code=200,
            content={
                "Correct": True
            }
        )
    else:
        return JSONResponse(
            status_code=200,
            content={
                "Correct": False
            }
        )
