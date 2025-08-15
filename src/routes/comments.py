from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Comment, Post, User
from ..schemas import CommentCreate, CommentOut
from .auth import get_current_user

router = APIRouter(prefix="/api/posts", tags=["Comments"])


# Add a comment to a post
@router.post(
    "/{post_id}/comment", response_model=CommentOut, status_code=status.HTTP_201_CREATED
)
def add_comment(
    post_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    new_comment = Comment(
        content=comment.content, user_id=current_user.id, post_id=post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


# Get comments for a post
@router.get("/{post_id}/comments", response_model=list[CommentOut])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return db.query(Comment).filter(Comment.post_id == post_id).all()
