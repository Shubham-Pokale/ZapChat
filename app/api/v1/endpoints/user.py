from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import logging
from app.schemas.user import UserCreate, UserBase
from app.db.models.user import User as DBUser
from app.db.base import get_db


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info(f"Fetching users with skip = {skip}, limit = {limit}")
    users = db.query(DBUser).offset(skip).limit(limit).all()
    logger.debug(f"Found {len(users)} users")
    return users


@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # In next steps we'll add password hashing and proper error handling
    logger.info(f"Creating new user with email: {user.email}")
    logger.debug(f"User details: {user.model_dump}")
    try: 
        db_user = DBUser(
            email=user.email,
            username=user.username ,
            hashed_password=user.password + "_notreallyhashed"  # Temporary
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))