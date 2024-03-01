from models.database import Base, database, engine
from sqlalchemy import Column, Integer, String


class Story:
    qnum = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class Zodiac(Base, Story):
    __tablename__ = "zodiac"


class Pirates(Base, Story):
    __tablename__ = "pirates"


class Digital(Base, Story):
    __tablename__ = "digital"


class HarryPotter(Base, Story):
    __tablename__ = "harrypotter"
