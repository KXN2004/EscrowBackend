from database import Base, database

from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, primary_key=True)
    phone = Column(String)
    storyline = Column(Integer)
