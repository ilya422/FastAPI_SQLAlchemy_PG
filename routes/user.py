from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from middlewares.db_conection import get_db
from database.models import User
from models.user import UserCreate

router = APIRouter()


@router.get('')
def get_all_users(request: Request, db: Session = Depends(get_db)):
    """
    Получение всех пользователей
    :param db:
    :return: USERS
    """
    return db.query(User).all()


@router.get('/{id}')
def get_user(request: Request, id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id
    :param id: ID
    :param db:
    :return: USER
    """
    return db.query(User).filter(User.id == id).first()


@router.post('')
def create_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, city_id=user.city_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

