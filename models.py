from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "students"

    student_id    = Column(Integer, primary_key= True)
    student_name  = Column(String, nullable=False)
    age           = Column(Integer,nullable=False)
    course        = Column(String)
    department    = Column(String)
