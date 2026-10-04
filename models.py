from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Boolean,ForeignKey

from database import Base

class Task(Base):
    __tablename__="tasks"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    description:Mapped[str]=mapped_column(String,nullable=False)
    completed:Mapped[bool]=mapped_column(Boolean,default=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)

class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    email:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)




