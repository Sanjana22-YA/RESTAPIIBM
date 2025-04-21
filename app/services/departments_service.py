from repos.departments_repo import DepartmentRepository
from sqlalchemy.orm import Session
from schemas.departments_schema import DepartmentsCreate

class DepartmentService:
    def __init__(self, db: Session):
        self.db = db
        self.department_repo = DepartmentRepository(db)

    def create_department(self, department: DepartmentsCreate):
        return self.department_repo.create_department(department)
