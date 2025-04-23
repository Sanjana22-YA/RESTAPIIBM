from ast import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database.deps import get_db
from repos.departments_repo import DepartmentRepository
from schemas.departments_schema import DepartmentsCreate, DepartmentsResponse
from services.departments_service import DepartmentService


router = APIRouter(prefix="/department", tags=["Departments"])

@router.post("/create", response_model=DepartmentsResponse)
def create_department(dept: DepartmentsCreate, db: Session = Depends(get_db)):
    return DepartmentService(DepartmentRepository(db)).create(dept)

@router.get("/get_all", response_model=list[DepartmentsResponse])
def get_all_departments(db: Session = Depends(get_db)):
    return DepartmentService(DepartmentRepository(db)).get_all()

@router.get("/get_by_id", response_model=DepartmentsResponse)
def get_department_by_id(dept_id: int, db: Session = Depends(get_db)):
    return DepartmentService(DepartmentRepository(db)).get_by_id(dept_id)

@router.put("/{dept_id}", response_model=DepartmentsResponse)
def update_department(dept_id: int, dept: DepartmentsCreate, db: Session = Depends(get_db)):
    return DepartmentService(DepartmentRepository(db)).update(dept_id, dept)