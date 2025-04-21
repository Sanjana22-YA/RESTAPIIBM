from pydantic import BaseModel

class AttendanceBase(BaseModel):
    date: str
    status: str

    class Config:
        orm_mode = True


class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
        