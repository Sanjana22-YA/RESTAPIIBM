from pydantic import BaseModel, EmailStr, field_validator

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str



    @field_validator("email")
    def validate_email(cls, value):
        if not value.endswith("ibm.com"):
            raise ValueError("Email must be from the domain 'ibm.com'")
        return value
    
    @field_validator("phone")
    def validate_phone(cls, value):
        if len(value) < 10:
            print(f"invalid phone number")
            raise ValueError("Phone number must be at least 10 digits long")
        return value

    class Config:
        orm_mode = True #Enable ORM mode to work with SQLAlchemy models
   
class EmployeeCreate(EmployeeBase):
    password: str
    @field_validator("password")
    def validate_password(cls, value):
        if len(value) <=6 and len(value) >=8:
            raise ValueError("Password must be at least 8 characters long")
        return value
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
        # Enable ORM mode to work with SQLAlchemy models


class EmployeeIDResponse(BaseModel):
    employee_id: int