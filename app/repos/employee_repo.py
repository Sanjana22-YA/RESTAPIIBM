from sqlalchemy.orm import Session
from models.employee import Employee
from schemas.employee_schema import EmployeeCreate

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, employee: EmployeeCreate) -> Employee:
        db_employee = Employee(
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            phone=employee.phone,
        )
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

