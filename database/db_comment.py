from database.models import DBComment
from sqlalchemy.orm import Session
from datetime import datetime

def add_comment(db, request):
    comment = DBComment(
        text = request.text,
        username =request.username,
        post_id = request.post_id,
        timestamp = datetime.now()
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment