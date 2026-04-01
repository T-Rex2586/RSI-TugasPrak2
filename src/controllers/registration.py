from fastapi import Depends
from sqlmodel import Session
from src.services.registration import RegistrationService
from src.database.connection import get_session
from src.dto.registration import RegistrationCreate

service = RegistrationService()

def get_registrations(db: Session = Depends(get_session)):
    return service.get_registrations(db)

def get_registration(registration_id: int, db: Session = Depends(get_session)):
    return service.get_registration(db, registration_id)

def create_registration(data: RegistrationCreate, db: Session = Depends(get_session)):
    return service.create_registration(db, data)

def update_registration(registration_id: int, data: RegistrationCreate, db: Session = Depends(get_session)):
    return service.update_registration(db, registration_id, data)

def delete_registration(registration_id: int, db: Session = Depends(get_session)):
    return service.delete_registration(db, registration_id)