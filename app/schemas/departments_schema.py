from pydantic import BaseModel
from datetime import datetime

class DepartmentsBase(BaseModel):
    dname: str
    location: str
    description: str

class DepartmentsCreate(DepartmentsBase):
    pass
class DepartmentUpdate(DepartmentsBase):
    pass

class DepartmentsResponse(DepartmentsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models