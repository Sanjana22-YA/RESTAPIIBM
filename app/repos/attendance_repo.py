from sqlalchemy.orm import Session
from models.attendance import Attendance
from schemas.attendance_schema import AttendanceCreate


class AttendanceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_attendance(self, attendance: AttendanceCreate) -> Attendance:
        db_attendance = Attendance(date=attendance.date,status=attendance.status,remarks=attendance.remarks,employee_id=attendance.employee_id)
        self.db.add(db_attendance)
        self.db.commit()
        self.db.refresh(db_attendance)
        return db_attendance
