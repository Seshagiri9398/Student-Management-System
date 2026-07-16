#step 1
class Student:
    def __init__(self,student_id,student_name,age,course,department):
        self.student_id = student_id
        self.student_name = student_name
        self.age = age
        self.course = course
        self.department = department

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Age: {self.age}")
        print(f"Student Course: {self.course}")
        print(f"Student Department:{self.department}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []


    def add_student(self):
        student_id = int(input("Enter student id:"))
        student_name = input("enter the student name:")
        age = int(input("Enter the age:"))
        course = input("Enter your course:")
        department = input("Enter the department:")

        student = Student(student_id,student_name,age,course,department)

        self.students.append(student)
        print("student added Successfully ")
sms = StudentManagementSystem()
sms.add_student()

    