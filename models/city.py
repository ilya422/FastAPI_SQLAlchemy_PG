from pydantic import BaseModel


class CityCreate(BaseModel):
    name: str


class City(CityCreate):
    id: int
