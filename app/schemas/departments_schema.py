from pydantic import BaseModel

class DepartmentsBase(BaseModel):
    dname: str
    location: str
    description: str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models


class DepartmentsCreate(DepartmentsBase):
    pass

class DepartmentsResponse(DepartmentsBase):
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models