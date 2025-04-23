from fastapi import HTTPException
from services import users_service
from models.employee import Employee
from repos.employee_repo import EmployeeRepository
from sqlalchemy.orm import Session
from schemas.employee_schema import EmployeeCreate, EmployeeResponse

class EmployeeService:
    def __init__(self, db: Session):
        self.db = db
        self.employee_repo = EmployeeRepository(db)
        
    def update_employee(self, employee_id: int, employee: EmployeeCreate) -> Employee | None:
        db_employee = self.employee_repo.update_employee(employee_id, employee)
        if not db_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return db_employee
        
    def get_all_employees(self):
        return self.employee_repo.get_all_employees()
    

    
    def create_employee(self, employee: EmployeeCreate):
        emp = self.employee_repo.create_employee(employee)
        if not emp:
            raise HTTPException(status_code=400, detail="Employee already exists")
        else:
            user_service = users_service.UsersService(self.db)
            user = user_service.create_user(email=employee.email, password=employee.password)
        if not user:
                #rollback the transaction if user creation fails
                self.db.rollback()
                raise HTTPException(status_code=400, detail="User creation failed")
        else:
            return emp
        

    
    def get_employee_by_id(self, employee_id: int):
        employee = self.employee_repo.get_employee_by_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee