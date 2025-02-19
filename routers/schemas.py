from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username: str
    password: str
    email: str

class UserDisplay(BaseModel):
    username: str
    email: str

class PostBase(BaseModel):
    image_url : str
    image_url_type :str
    Caption :str
    user_id : int

class User(BaseModel):
    username: str

# class Post(BaseModel):
#     post_id: int

#Comment Postdisplay
class Comment(BaseModel):
    username:str
    text : str
    timestamp: datetime
    class Config():
        from_attributes=True

class PostDisplay(BaseModel):
    id : int
    image_url : str
    image_url_type :str
    Caption :str
    timestamp : datetime
    comments : List[Comment]
    user : User
    class Config():
        from_attributes=True

class OAuthUser(BaseModel):
    id:int
    username:str
    email:str

class CommentBase(BaseModel):
    text: str
    username: str
    post_id: int
