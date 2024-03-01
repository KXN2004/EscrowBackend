from models.database import Base, database ,engine

from datetime import datetime
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
    hintcount = Column(Integer)

    def __init__(self, email):
        self.user = database.query(Users).filter_by(email=email).one()

    def get_start(self):
        return self.user.start

    def set_start(self):
        start = datetime.now().time()
        self.user.start = start.strftime("%H:%M:%S")
        database.commit()
        return start


