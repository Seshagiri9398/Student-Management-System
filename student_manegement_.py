#step 1
class Student:
    def __init__(self,student_id,student_name,age,course,department):
        self.student_id = student_id
        self.student_name = student_name
        self.age = age
        self.course = course
        self.department = department

    def display_details(self):
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

    def search_student(self):
        search_id = int(input("Enter the Search ID:"))


        for student in self.students:
            if search_id == student.student_id:
                student.display_details()
                return 
        print("Student not found")


    def view_students(self):
        if len(self.students) == 0:
            print("no Student Found")
        else:
            for student in self.students:
                student.display_details()

    
sms = StudentManagementSystem()

while True:
    print("\n ==Student Management System ==")
    print("1. Add Student")
    print("2. View Students")
    print("3. search Student")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")

