 
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = os.getenv("postgresql://inventory_db_wcf7_user:bHu7UHXstmwDMOpvat6sTMpypNZHxsFV@dpg-d8tn98og4nts73d3rp00-a/inventory_db_wcf7")
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)