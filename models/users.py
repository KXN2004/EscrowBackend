from config import DB_URL

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
engine = create_engine(DB_URL)
database = Session(bind=engine)


class Users(Base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)
    phone = Column(String)
    storyline = Column(Integer)


Base.metadata.create_all(engine, checkfirst=True)
