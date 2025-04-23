from models.users import Users
from sqlalchemy.orm import Session
from repos.users_repo import UsersRepository

class UsersService:
    def __init__(self, db: Session):
        self.db = db
        self.users_repo = UsersRepository(db)

    def create_user(self, email, password):
        return self.users_repo.create_user(email=email, password=password)