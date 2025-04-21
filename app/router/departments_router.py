from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.departments_schema import DepartmentsCreate, DepartmentsResponse
from services.departments_service import DepartmentService
from database.deps import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

## end point : /api/departments/create
# type : public
# method : POST
# description : create departments
# request body : {
#     "department_name": "HR",
#     "location": "New York",
#     "manager_id": 1
# }
# response : {
#     "id": 1,
#     "department_name": "HR",      
#     "location": "New York",
#     "manager_id": 1
# }
#
@router.post("/create", response_model=DepartmentsResponse)
def create_departments(departments: DepartmentsCreate, db: Session = Depends(get_db)):
    """
    Create a new departments.
    """
    service = DepartmentService(db)
    return service.create_departments(departments)

