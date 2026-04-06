from fastapi import Depends
from sqlmodel import Session
from src.services.user import UserService
from src.database.connection import get_session
from src.dto.user import UserCreate

service = UserService()

def get_users(db: Session = Depends(get_session)):
    return service.get_users(db)

def get_user(user_id: int, db: Session = Depends(get_session)):
    return service.get_user(db, user_id)

def create_user(data: UserCreate, db: Session = Depends(get_session)):
    return service.create_user(db, data)

def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_session)):
    return service.update_user(db, user_id, data)

def delete_user(user_id: int, db: Session = Depends(get_session)):
    return service.delete_user(db, user_id)