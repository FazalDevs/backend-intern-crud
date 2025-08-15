from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from .auth import get_current_user
from ..models import User
from .. import schemas

router = APIRouter(prefix="/api/posts", tags=["Likes"])


@router.post("/{id}/like")
def like_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if post exists
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Check if already liked
    existing_like = (
        db.query(models.Like)
        .filter(models.Like.post_id == id, models.Like.user_id == current_user.id)
        .first()
    )
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this post")

    # Create a new like
    like = models.Like(user_id=current_user.id, post_id=id)
    db.add(like)
    db.commit()
    db.refresh(like)

    return {
        "message": "Post liked successfully",
        "like_id": like.id,
        "post_id": id,
        "user_id": current_user.id,
    }


@router.get("/{post_id}/likes", response_model=list[schemas.LikeResponse])
def get_post_likes(post_id: int, db: Session = Depends(get_db)):
    likes = db.query(models.Like).filter(models.Like.post_id == post_id).all()
    return likes
