from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.auth import register_user, authenticate_user
from app.schemas.user import UserCreate, UserLogin, UserResponse

router = APIRouter()


# Route for user registration
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)


# Route for user login
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(user, db)
