from repos.employee_repo import EmployeeRepository
from sqlalchemy.orm import Session
from schemas.employee_schema import EmployeeCreate

class EmployeeService:
    def __init__(self, db: Session):
        self.db = db
        self.employee_repo = EmployeeRepository(db)

    def create_employee(self, employee: EmployeeCreate):
        return self.employee_repo.create_employee(employee)