from sqlalchemy import *
from config.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100))
    created = Column(DateTime)
    last_login = Column(DateTime)
    location = Column(String(100))

    def __str__(self):
        return f'{self.name}'