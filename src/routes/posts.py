from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
from .auth import get_current_user
from ..models import User

router = APIRouter(prefix="/api/posts", tags=["Posts"])


@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # You could also associate the post with current_user.id here if needed
    return crud.create_post(db, post)


@router.get("/", response_model=list[schemas.PostOut])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


@router.get("/{post_id}", response_model=schemas.PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(
    post_id: int,
    post: schemas.PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_post = crud.update_post(db, post_id, post)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_post = crud.delete_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return None


@router.post("/{id}/like")
def like_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Only logged-in users will reach here
    return crud.like_post(db, post_id=id, user_id=current_user.id)
