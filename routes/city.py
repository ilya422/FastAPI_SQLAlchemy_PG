from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from middlewares.db_conection import get_db
from database.models import City
from models.city import CityCreate

router = APIRouter()


@router.get('')
def get_all_cities(request: Request, db: Session = Depends(get_db)):
    """
    Получение всех городов
    :param db:
    :return: USERS
    """
    return db.query(City).all()


@router.get('/{id}')
def get_city(request: Request, id: int, db: Session = Depends(get_db)):
    """
    Получение города по id
    :param id: ID
    :param db:
    :return: USER
    """
    return db.query(City).filter(City.id == id).first()


@router.post('')
def create_city(request: Request, body: CityCreate, db: Session = Depends(get_db)):
    db_city = City(name=body.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

