from fastapi import FastAPI, HTTPException,status,Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse
from routers.students import router as student_router


app = FastAPI()

app.include_router(student_router)



