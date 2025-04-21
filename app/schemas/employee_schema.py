from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True #Enable ORM mode to work with SQLAlchemy models
   
class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
        # Enable ORM mode to work with SQLAlchemy models