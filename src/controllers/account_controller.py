from fastapi import Depends
from sqlmodel import Session
from src.services.account_service import AccountService
from src.database.connection import get_session
from src.dto.account_dto import AccountCreate, AccountUpdate


service = AccountService()


def get_accounts(db: Session = Depends(get_session)):
    return service.get_accounts(db)


def get_account(account_id: int, db: Session = Depends(get_session)):
    return service.get_account(db, account_id)


def create_account(data: AccountCreate, db: Session = Depends(get_session)):
    return service.create_account(db, data)


def update_account(account_id: int, data: AccountUpdate, db: Session = Depends(get_session)):
    return service.update_account(db, account_id, data)


def delete_account(account_id: int, db: Session = Depends(get_session)):
    return service.delete_account(db, account_id)
