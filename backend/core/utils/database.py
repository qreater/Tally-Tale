from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DATABASE_URI = getenv("DATABASE_URI")

if DATABASE_URI is None:
    raise ValueError("DATABASE_URI environment variable is not set")

engine = create_engine(DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def save_and_refresh(db, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj        

