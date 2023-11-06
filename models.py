from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)
    last_login = Column(DateTime())
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    role = relationship("Role", backref="users")

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    #...
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", backref="profile", uselist=False)
    
class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    
class AutorLibro(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, primary_key=True)
    libro_id = Column(Integer, ForeignKey('libros.id'), nullable=False, primary_key=True)