from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.employee_schema import EmployeeCreate, EmployeeResponse
from services.employee_service import EmployeeService
from database.deps import get_db

router = APIRouter(prefix="/employee", tags=["Employee"])

## end point : /api/employee/create
# type : public
# method : POST
# description : create employee
#request body : {
#    "first_name": "John",
#    "last_name": "Doe",
#    "email": "john.doe@example.com"
#     "phone": "1234567890",
#}
# response : {
#    "id": 1,
#    "first_name": "John",
#    "last_name": "Doe",
#    "email": "john.doe@example.com"
#    "phone": "1234567890",
#}



@router.post("/create", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee.
    """
    service = EmployeeService(db)
    return service.create_employee(employee)


# end point : /api/employee/
# type : public
# method : GET
# description : get all employee
# response : [
#    {
#        "id": 1,
#        "first_name": "John",
#        "last_name": "Doe",
#        "email": "
#        "phone": "1234567890",
#    },


@router.get("/", response_model=EmployeeResponse)
def get_all_employee(db: Session = Depends(get_db)):
    #want to send the fake object
    response ={
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
    }
    return response