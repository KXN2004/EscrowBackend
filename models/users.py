from models.database import Base, database

from sqlalchemy import Column, Integer, String,Time



class Users(Base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)
    phone = Column(String)
    storyline = Column(Integer)
    start = Column(Time)
    end = Column(Time)
    progress = Column(Integer)

    def get_start(self):
        return database.query(Users).filter_by(email=self.email).first().start


