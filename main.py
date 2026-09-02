from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from student_manegement_ import Student
from database import get_all_students,get_student_by_id,add_student_to_db,update_student_in_db


app = FastAPI()

class StudentCreate(BaseModel):
    student_id : int
    student_name : str
    age : int
    course : str
    department : str

class StudentUpdate(BaseModel):
    student_name : str
    age : int
    course : str
    department : str


@app.get("/")
def home():
    return {"message": "Student Management API is running"}
    
@app.get("/students")
def get_students():
    rows = get_all_students()
    return rows

@app.get("/students/{student_id}")
def get_student(student_id):
    result = get_student_by_id(student_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result

@app.post("/students",status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    add_student_to_db(student)
    return {"message":"student created successfully"}


@app.put("/students/{student_id}")
def update_student(student : StudentUpdate,student_id : int):
    result = get_student_by_id(student_id)
    if not result:
        raise HTTPException(status_code=404, detail="student not found")

    updated_student = Student(
        student_id,
        student.student_name,
        student.age,
        student.course,
        student.department
    )

    update_student_in_db(updated_student)
    return {"message":"student updated successfully"}
