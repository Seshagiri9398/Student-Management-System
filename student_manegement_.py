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
        student_id = int(input("Enter Student Id:"))

        #duplicate ID validation
        for student in self.students:
            if student_id == student.student_id:
                print("Student ID already exists!")
                return
        
        student_name = input("Enter Student Name:")
        age = int(input("Enter Student Age:"))

        #Validation Age
        if age < 1 or age > 120:
            print("Invalid age. Age must be between 1 and 120.")
            return
        
        course = input("Enter Student Course:")
        department = input("Enter Student Department:")

        student = Student(student_id,student_name,age,course,department)

        self.students.append(student)
        print("student added Successfully ")

    def search_student(self):
        search_id = int(input("Enter Student ID to Search:"))


        for student in self.students:
            if search_id == student.student_id:
                student.display_details()
                return 
        print("Student not found")

    def update_student(self):
        update_id = int(input("Enter Student ID to Update:"))

        for student in self.students:
            if update_id == student.student_id:
                new_name = input("Enter New Name:")
                new_age = int(input("Enter New Age:"))
                new_course = input("Enter New Course:")
                new_department = input("Enter New Department:")

                student.student_name = new_name
                student.age = new_age
                student.course = new_course
                student.department = new_department

                print("Student Updated Successfully.")
                student.display_details()
                return
            
        print("Student Not Found")

    def delete_student(self):

        delete_id = int(input("Enter Student ID to Delete:"))

        for student in self.students:
            if delete_id == student.student_id:
                self.students.remove(student)
                print("Student Delete Successfully.")
                return
        print("No Student Found")


    def view_students(self):
        if len(self.students) == 0:
            print("No Student Found")
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
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice:")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.update_student()
    elif choice == "5":
        sms.delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")

