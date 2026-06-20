 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, URL

db_url="postgresql://postgres:your_password@localhost:5432/telusko"

engine =create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=True,bind=engine)