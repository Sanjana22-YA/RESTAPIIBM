from pydantic import BaseModel

class ProjectsBase(BaseModel):
    project_name: str
    start_date: str
    end_date: str
    description: str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class ProjectsCreate(ProjectsBase):
    pass


class ProjectsResponse(ProjectsBase):
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models