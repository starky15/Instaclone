from sqlalchemy import Column,String,Integer
from database.database import Base

class DBUser(Base):
    __tablename__ = "user"
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    password=Column(String)
    email=Column(String)