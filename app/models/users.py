from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class Users(Base):
    __tablename__ = 'users_table' # Define the table name in the database
    id = Column(Integer, primary_key=True, index=True) # Define the primary key column
    email = Column(String, unique=True, index=True) # Define the email column with unique constraint
    password = Column(String(100), nullable=False) # Define the password column with a maximum length of 100 characters