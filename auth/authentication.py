from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm 
from database.database import get_db
from auth import oauth2
from database.models import DBUser
from database.hashing import Hash

router = APIRouter(tags=["authentication"])

@router.post("/login")
def authenticate(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = oauth2.create_access_token(data = {"username":user.username})
    return {
        "access_token":access_token,
        "user_id":user.id,
        "username":user.username,
        "token-type":"bearer"
    }