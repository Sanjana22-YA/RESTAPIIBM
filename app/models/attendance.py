from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)  # Date of attendance
    status = Column(String(20), nullable=False)  # e.g., Present, Absent, Leave