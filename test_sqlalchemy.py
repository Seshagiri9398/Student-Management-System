from database import SessionLocal
from models import Student

db = SessionLocal()
students = db.query(Student).all()

for student in students:
    print(student.student_id,student.student_name,student.age)

db.close()