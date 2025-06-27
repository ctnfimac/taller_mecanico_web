"""
Este archivo se encarga de la conexión a la base de datos postgresql
la cual esta definida den el docker-compose.dev.yml
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_POSTGRES_URL = 'postgresql://authadmin:auth123@localhost:5435/authDb'

engine = create_engine(
    SQLALCHEMY_DATABASE_POSTGRES_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()