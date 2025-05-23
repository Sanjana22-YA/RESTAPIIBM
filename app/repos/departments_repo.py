from schemas.departments_schema import DepartmentUpdate, DepartmentsCreate
from database import session
from models.department import Department


class DepartmentRepository:
    def __init__(self, db: session):
        self.db = db

    def get_all(self):
        return self.db.query(Department).all()

    def get_by_id(self, dept_id: int):
        return self.db.query(Department).filter(Department.id == dept_id).first()
    
    def update_department(self, dept_id: int, dept_data: DepartmentUpdate):
        dept = self.get_by_id(dept_id)
        if not dept:
            return None
        for field, value in dept_data.dict().items():
            setattr(dept, field, value)
        self.db.commit()
        self.db.refresh(dept)
        return dept

    def create(self, dept: DepartmentsCreate):
        new_dept = Department(
            dname=dept.dname,
            location=dept.location,
            description=dept.description
        )
        self.db.add(new_dept)
        self.db.commit()
        self.db.refresh(new_dept)
        return new_dept

    def delete(self, dept_id: int):
        dept = self.get_by_id(dept_id)
        if dept:
            self.db.delete(dept)
            self.db.commit()
        return dept