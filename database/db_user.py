from sqlalchemy.orm import Session
from routers.schemas import UserBase
from database.models import DBUser
from database.hashing import Hash
from fastapi import HTTPException,status


def user_add(db: Session, request: UserBase):
    user = DBUser(
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db:Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"username {username} not found in system")
    return user