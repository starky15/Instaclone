from sqlalchemy.orm import Session
from routers.schemas import UserBase
from database.models import DBUser
from database.hashing import Hash

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