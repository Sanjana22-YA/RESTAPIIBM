from sqlalchemy.orm import Session
from models.projects import Project
from schemas.projects_schema import ProjectsCreate


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: ProjectsCreate) -> Project:
        db_project = Project(
            name=project.name,
            description=project.description,
            start_date=project.start_date,
            end_date=project.end_date,
        )
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project