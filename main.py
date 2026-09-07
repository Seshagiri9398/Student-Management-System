from fastapi import FastAPI, HTTPException,status

from database import SessionLocal
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse

app = FastAPI()


#GET ALL STUDENTS
@app.get("/students",response_model=list[StudentResponse])
def get_students():
    db = SessionLocal()
    result = db.query(Student).all()
    db.close()
    return result

#GET STUDENT BY ID
@app.get("/students/{student_id}",response_model=StudentResponse)
def get_student(student_id : int):
    db = SessionLocal()
    result = db.query(Student).filter(Student.student_id == student_id).first()
    db.close()
    if not result:
        raise HTTPException(status_code= 404, detail= "student not found")
    return result

#CREATE STUDENT
@app.post("/students",status_code=status.HTTP_201_CREATED,response_model=StudentResponse)
def create_student(student: StudentCreate):
    db = SessionLocal()

    new_student = Student(
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


#UPDATE STUDENT
@app.put("/students/{student_id}",response_model=StudentResponse)
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

#DELETE STUDENT
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

