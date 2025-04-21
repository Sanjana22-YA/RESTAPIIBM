from repos.projects_repo import ProjectRepository
from sqlalchemy.orm import Session
from schemas.projects_schema import ProjectsCreate

class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, project: ProjectsCreate):
        return self.project_repo.create_project(project)