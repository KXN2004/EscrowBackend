from pydantic import BaseModel

from models.users import Users
from routes.login import manager
from models.games import *
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/question")

stories = {
    "Digital": Digital,
    "Harry Potter": HarryPotter,
    "Pirates": Pirates,
    "Zodiac": Zodiac,
}


class Answer(BaseModel):
    answer: str


@router.get("/")
async def question_progress(user=Depends(manager)):
    storyline = database.query(Users).filter_by(email=user.email).one().storyline
    story = stories[storyline]
    progress = database.query(Users).filter_by(email=user.email).one().progress
    question = database.query(story).filter_by(qnum=progress).one().question
    return JSONResponse(
        status_code=200,
        content={
            "Question": question,
        }
    )


@router.post("/{progress}")
async def answer_progress(progress: int, answer_data: Answer, user=Depends(manager)):
    print(answer_data)
    storyline = database.query(Users).filter_by(email=user.email).one().storyline
    story = stories[storyline]
    correct = set(database.query(story).filter_by(qnum=progress).one().answer.lower().split(","))
    answer = set("".join(answer_data.answer.lower().split()).split(","))

    if answer == correct:
        database.query(Users).filter_by(email=user.email).update({"progress": progress + 1})

        if progress <= 7:
            next_question = database.query(story).filter_by(qnum=progress + 1).one().question
        elif progress == 9:
            Users(email=user.email).set_end()
        else:
            next_question = None

        database.commit()

        return JSONResponse(
            status_code=200,
            content={
                "Correct": True,
                "NextQuestion": next_question
            }
        )
    else:
        return JSONResponse(
            status_code=200,
            content={
                "Correct": False
            }
        )
