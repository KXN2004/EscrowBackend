from pydantic import BaseModel

from models.users import Users
from routes.login import manager
from models.games import *
from fastapi import APIRouter, Depends, status
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
    print(f"User: {user.name}")
    print(f"Story: {story}")
    print(f"Current Question: {question}")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
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
    print(f"User: {user.name}")
    print(f"Story: {story}")
    print(f"Expected Answer: {answer}")
    print(f"Correct Answer: {correct}")
    if answer == correct:
        database.query(Users).filter_by(email=user.email).update({"progress": progress + 1})
        print("Answer: Correct")
        print(f"Current Question: {progress}")
        if progress <= 7:
            next_question = database.query(story).filter_by(qnum=progress + 1).one().question
            print(f"Next Question: {next_question}")
        elif progress == 8:
            next_question = None
            ending = Users(email=user.email).set_end()
            print(f"Next Question: None")
            print(f"User: {user.name} - Ended at {ending.strftime('%H:%M:%S')}")
        database.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "Correct": True,
                "NextQuestion": next_question
            }
        )
    else:
        print("Answer: Incorrect")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "Correct": False
            }
        )
