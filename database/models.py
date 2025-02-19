from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from database.database import Base
from sqlalchemy.orm import relationship

class DBUser(Base):
    __tablename__ = "user"
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    password=Column(String)
    email=Column(String)
    items = relationship('DBPost' ,back_populates='user')


class DBPost(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    Caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DBUser', back_populates='items')
    comments = relationship('DBComment', back_populates='post')
    

class DBComment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    timestamp = Column(DateTime)
    username = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('DBPost', back_populates='comments')
