from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,declarative_base


url=f"postgresql+psycopg2://postgres:root@localhost:5432/taskmanagement"
engine=create_engine(url)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()