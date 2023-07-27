from sqlalchemy.exc import OperationalError
from fastapi import Request, HTTPException

from database.core import SessionLocal


def get_db(request: Request = None):
    db = SessionLocal()
    try:
        yield db
    except OperationalError:
        raise HTTPException(detail="No connect DB", status_code=500)
    finally:
        db.close()
