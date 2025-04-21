from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from schemas.projects_schema import ProjectsCreate, ProjectsResponse
from services.projects_service import ProjectService
from database.deps import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])

# end point : /api/projects/create
# type : public
# method : POST
# description : create projects
# request body : {
#     "project_name": "Project A",
#     "description": "Description of Project A",
#     "start_date": "2023-10-01",
#     "end_date": "2023-12-31",
#     "status": "ongoing",
#     "department_id": 1
# }
# response : {
#     "id": 1,      
#     "project_name": "Project A",
#     "description": "Description of Project A",
#     "start_date": "2023-10-01",
#     "end_date": "2023-12-31",
#     "status": "ongoing",
#     "department_id": 1
# }


@router.post("/create", response_model=ProjectsResponse)
def create_projects(projects: ProjectsCreate, db: Session = Depends(get_db)):
    """
    Create a new projects.
    """
    service = ProjectService(db)
    return service.create_projects(projects)