from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.db import DB_CONNECT_URL

engine = create_engine(DB_CONNECT_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
