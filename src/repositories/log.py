from sqlmodel import Session, select
from src.database.model.models import Log

class LogRepository:

    def get_all(self, db: Session):
        return db.exec(select(Log)).all()
        
    def get_by_id(self, db: Session, log_id: int):
        return db.get(Log, log_id)
    
    def create(self, db: Session, log: Log):
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
    
    def update(self, db: Session, log: Log):
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
    
    def delete(self, db: Session, log_id: int):
        log = db.get(Log, log_id)
        if log:
            db.delete(log)
            db.commit()
            return True
        return False