from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from routers.schemas import PostDisplay, PostBase
from database.database import get_db
from sqlalchemy.orm import Session
from database import db_post
from typing import List
import random
import string
import shutil
from routers.schemas import OAuthUser
from auth.oauth2 import get_current_user

router = APIRouter(prefix="/post", tags=["post"])

url_type = ["absolute", "relative"]

@router.post("/", response_model=PostDisplay)
def post_create(request : PostBase, db : Session = Depends(get_db), current_user : OAuthUser = Depends(get_current_user)):
    if request.image_url_type not in url_type:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url type should be either Absolute or Relative")
    return db_post.create_post(db, request)

@router.get("/all", response_model=List[PostDisplay])
def post_get_all(db : Session = Depends(get_db)):
    return db_post.get_post(db)

@router.post("/image")
def upload_image(file : UploadFile = File(...), current_user : OAuthUser = Depends(get_current_user)):
    # print(file.filename)
    end = file.filename.split(".")
    string_char = string.ascii_letters
    r_str = []
    for i in range(6):
        r_str.append(random.choice(string_char))
    a = "".join(r_str)
    FINAL_PATH_NAME = f"images/{end[0]}_{a}.{end[1]}"
    # print(FINAL_PATH_NAME)

    with open(FINAL_PATH_NAME , "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename":FINAL_PATH_NAME}

@router.get("/delete/{id}")
def post_delete(id: int, db : Session = Depends(get_db), current_user : OAuthUser = Depends(get_current_user)):
    return db_post.delete_post(db, id, current_user.id)