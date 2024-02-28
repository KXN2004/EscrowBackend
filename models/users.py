from database import Base, database

from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)
    phone = Column(String)
    storyline = Column(Integer)


vishal = Users()

vishal.name = "Vishal"
vishal.email = "vism06@gmail.com"
phone = "8999972216"
vishal.password = phone
vishal.phone = phone
vishal.storyline = 1

database.add(vishal)
database.commit()

