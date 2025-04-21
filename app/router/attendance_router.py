from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.attendance_schema import AttendanceCreate, AttendanceResponse
from services.attendance_service import AttendanceService
from database.deps import get_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# end point : /api/attendance/create
# type : public
# method : POST
# description : create attendance
# request body : {
#     "employee_id": 1,
#     "check_in": "2023-10-01T09:00:00",
#     "check_out": "2023-10-01T17:00:00",   
#     "status": "present"
# } 
# response : {
#     "id": 1,      
#     "employee_id": 1,
#     "check_in": "2023-10-01T09:00:00",
#     "check_out": "2023-10-01T17:00:00",
#     "status": "present"
# }
#
@router.post("/create", response_model=AttendanceResponse)
def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """
    Create a new attendance record.
    """
    service = AttendanceService(db)
    return service.create_attendance(attendance)