from fastapi import HTTPException, status
from schemas.departments_schema import DepartmentsCreate
from repos.departments_repo import DepartmentRepository


class DepartmentService:
    def __init__(self, repo: DepartmentRepository):
        self.repo = repo
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, dept_id: int):
        dept = self.repo.get_by_id(dept_id)
        if not dept:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return dept

    def update(self, dept_id: int, dept_data: DepartmentsCreate):
        dept = self.repo.update_department(dept_id, dept_data)
        if not dept:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return dept
    
    def create(self, dept: DepartmentsCreate):
        return self.repo.create(dept)

    def get_by_id(self, dept_id: int):
        dept = self.repo.get_by_id(dept_id)
        if not dept:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return dept
    
    def delete(self, dept_id: int):
        deleted = self.repo.delete(dept_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return deleted