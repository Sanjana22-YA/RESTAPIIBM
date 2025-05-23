# import FastAPI
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from core.globalexception.exceptions import not_found_exception_handler
from core.globalexception.error_response import validation_exception_handler
from router.root_router import rootRouter
from database.session import Base, engine
from core.config.db_config import load_env_config
from models import employee, attendance, projects, department, role

app = FastAPI(title="FastAPI Emp CRUD")

#load env
# db_details = load_env_config()

mainrouter = rootRouter()
app.include_router(router = mainrouter)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, not_found_exception_handler)

@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    Base.metadata.create_all(bind=engine)
    
@app.get("/")
def read_root():
    return {"Hello": "World"}
