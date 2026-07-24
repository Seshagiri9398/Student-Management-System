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

    def update_student(self):
        update_id = int(input("Enter the Update ID:"))

        for student in self.students:
            if update_id == student.student_id:
                new_name = input("Enter the New name:")
                new_age = int(input("Enter the New age:"))
                new_course = input("Enter the New course:")
                new_department = input("Enter the New department:")

                student.student_name = new_name
                student.age = new_age
                student.course = new_course
                student.department = new_department

                print("Student updated successfully.")
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
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.update_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")

