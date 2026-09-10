from fastapi import APIRouter , Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Literal

from database import get_db
from models import Student
from schemas import StudentResponse, StudentCreate, StudentUpdate

router = APIRouter()

#GET ALL STUDENTS
@router.get("/students",response_model=list[StudentResponse])
def get_students(
    page: int = Query(1,ge=1), 
    limit: int = Query(10,ge=1, le=100),
    sort_by: Literal["student_id", "student_name"] = Query("student_id"),
    order: Literal["asc","desc"] = Query("asc"),
    db: Session = Depends(get_db)
    ):

    offset = (page - 1) * limit

    query = db.query(Student)


    if sort_by == "student_name":
        column = Student.student_name
    else:
        column = Student.student_id

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())


    result = (query.offset(offset).limit(limit).all())

    return result
    


# SEARCH STUDENTS BY NAME
@router.get("/students/search", response_model=list[StudentResponse])
def search_students(name: str, db: Session = Depends(get_db)):
    students = db.query(Student).filter(Student.student_name.ilike(f"%{name}%")).all()

    return students


#GET STUDENT BY ID
@router.get("/students/{student_id}",response_model=StudentResponse)
def get_student(student_id : int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()

    if not student:
        raise HTTPException(status_code= 404, detail= "student not found")
    return student


#CREATE STUDENT
@router.post("/students",status_code=status.HTTP_201_CREATED,response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        student_name = student.student_name,
        age = student.age,
        course = student.course,
        department = student.department
    )

    db.add(new_student)

    try:
        db.commit()
        db.refresh(new_student)
    except Exception:
        db.rollback()
        raise
    
    return new_student


#UPDATE STUDENT
@router.put("/students/{student_id}",response_model=StudentResponse)
def update_student(student_id : int,student : StudentUpdate, db: Session = Depends(get_db)):

    result = db.query(Student).filter(Student.student_id == student_id).first()

    if not result:
        raise HTTPException(status_code=404, detail="student not found")

    result.student_name = student.student_name
    result.age = student.age
    result.course = student.course
    result.department = student.department

    try:
        db.commit()
        db.refresh(result)
    except Exception:
        db.rollback()
        raise

    return result


#DELETE STUDENT
@router.delete("/students/{student_id}")
def delete_student(student_id : int, db: Session = Depends(get_db)):
    
    result = db.query(Student).filter(Student.student_id == student_id).first()

    if not result:
        raise HTTPException(status_code= 404, detail= "student not found")
    db.delete(result)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return {"message": "Student deleted successfully"}

