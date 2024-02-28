from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
from config import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)
database = Session(bind=engine)

Base.metadata.create_all(engine, checkfirst=True)
