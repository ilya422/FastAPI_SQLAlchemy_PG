from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.core import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    city = relationship("City")
