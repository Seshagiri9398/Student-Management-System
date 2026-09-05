from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from student_manegement_ import Student
from database import get_all_students,get_student_by_id,add_student_to_db,update_student_in_db,delete_student_in_db,SessionLocal
from models import Student

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
    db = SessionLocal()
    result = db.query(Student).all()
    db.close()
    return result

@app.get("/students/{student_id}")
def get_student(student_id : int):
    db = SessionLocal()
    result = db.query(Student).filter(Student.student_id == student_id).first()
    db.close()
    if not result:
        raise HTTPException(status_code= 404, detail= "student not found")
    return result

@app.post("/students",status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    db = SessionLocal()

    new_student = Student(
        student_id = student.student_id,
        student_name = student.student_name,
        age = student.age,
        course = student.course,
        department = student.department
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    return new_student



@app.put("/students/{student_id}")
def update_student(student : StudentUpdate,student_id : int):
    db = SessionLocal()
    result = db.query(Student).filter(Student.student_id == student_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="student not found")

    result.student_name = student.student_name
    result.age = student.age
    result.course = student.course
    result.department = student.department

    db.commit()
    db.close()

    return result


@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    db = SessionLocal()
    result = db.query(Student).filter(Student.student_id == student_id).first()

    if not result:
        raise HTTPException(status_code= 404, detail= "student not found")
    db.delete(result)
    db.commit()
    db.close()

    return result

