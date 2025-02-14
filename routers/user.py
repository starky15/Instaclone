from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers.schemas import UserDisplay, UserBase
from database.database import get_db
from database import db_user

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", response_model=UserDisplay)
def user_add(request: UserBase, db : Session = Depends(get_db)):
    return db_user.user_add(db, request)