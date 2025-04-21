from repos.attendance_repo import AttendanceRepository
from sqlalchemy.orm import Session
from schemas.attendance_schema import AttendanceCreate

class AttendanceService:
    def __init__(self, db: Session):
        self.db = db
        self.attendance_repo = AttendanceRepository(db)

    def create_attendance(self, attendance: AttendanceCreate):
        return self.attendance_repo.create_attendance(attendance)