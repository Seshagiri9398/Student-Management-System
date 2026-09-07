from pydantic import BaseModel

class StudentCreate(BaseModel):
    student_name : str
    age : int
    course : str
    department : str

class StudentUpdate(BaseModel):
    student_name : str
    age : int
    course : str
    department : str

class StudentResponse(BaseModel):
    student_id : int
    student_name : str
    age : int
    course : str
    department : str

    class Config:
        from_attributes = True
