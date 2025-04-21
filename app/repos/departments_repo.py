from sqlalchemy.orm import Session
from models.department import Department 
from schemas.departments_schema import DepartmentsCreate 

class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_department(self, department: DepartmentsCreate) -> Department:
        db_department = Department(
            name=department.name,
            description=department.description
        )
        self.db.add(db_department)
        self.db.commit()
        self.db.refresh(db_department)
        return db_department



