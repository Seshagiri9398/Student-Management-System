from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    student_name : str = Field(..., min_length=2, max_length=50)
    age : int = Field(..., ge=1, le=120)
    course : str = Field(..., min_length=2, max_length=50)
    department : str = Field(..., min_length=2, max_length=50) 

class StudentUpdate(BaseModel):
    student_name : str = Field(...,min_length=2, max_length=50)
    age : int = Field(..., ge=1, le=120)
    course : str = Field(..., min_length=2, max_length=50)
    department : str = Field(..., min_length=2, max_length=50)

class StudentResponse(BaseModel):
    student_id : int
    student_name : str
    age : int
    course : str
    department : str

    class Config:
        from_attributes = True
