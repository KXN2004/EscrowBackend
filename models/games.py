from models.database import Base, database, engine
from sqlalchemy import Column, Integer, String


class Zodiac(Base):
    __tablename__ = "zodiac"

    qnum = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class Pirates(Base):
    __tablename__ = "pirates"

    qnum = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class Digital(Base):
    __tablename__ = "digital"

    qnum = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class HarryPotter(Base):
    __tablename__ = "harrypotter"

    qnum = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

