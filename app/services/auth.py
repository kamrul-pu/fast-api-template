from sqlalchemy.orm import Session

from app.models.user import User

# from core.security import create_access_token, hash_password, verify_password
from app.schemas.user import UserCreate, UserLogin
from fastapi import HTTPException
from app.core.security import create_access_token, hash_password, verify_password


# Register a new user
def register_user(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    db_user = User(
        email=user.email, full_name=user.full_name, hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Authenticate user and create JWT token
def authenticate_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
