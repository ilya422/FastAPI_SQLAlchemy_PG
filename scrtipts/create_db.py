from database.core import engine, Base

Base.metadata.create_all(engine)
