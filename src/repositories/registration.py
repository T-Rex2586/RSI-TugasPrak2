from sqlmodel import Session, select
from src.database.model.models import Registration

class RegistrationRepository:

    def get_all(self, db: Session):
        return db.exec(select(Registration)).all()
        
    def get_by_id(self, db: Session, registration_id: int):
        return db.get(Registration, registration_id)
    
    def create(self, db: Session, registration: Registration):
        db.add(registration)
        db.commit()
        db.refresh(registration)
        return registration
    
    def update(self, db: Session, registration: Registration):
        db.add(registration)
        db.commit()
        db.refresh(registration)
        return registration
    
    def delete(self, db: Session, registration_id: int):
        registration = db.get(Registration, registration_id)
        if registration:
            db.delete(registration)
            db.commit()
            return True
        return False