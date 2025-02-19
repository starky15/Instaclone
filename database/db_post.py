from database.models import DBPost
from datetime import datetime
from fastapi import HTTPException, status

def create_post(db, request):
    new_post = DBPost(
    image_url  = request.image_url,
    image_url_type = request.image_url_type,
    Caption = request.Caption,
    user_id = request.user_id,
    timestamp = datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post(db):
    return db.query(DBPost).all()

def delete_post(db, id, user_id):
    post = db.query(DBPost).filter(DBPost.id == id).first()

    if not post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    if not post.user_id == user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User not authorised to delete this post!")
    db.delete(post)
    db.commit()

    return{"status": "deleted successfully"}