#Student Class
class Student:
    def __init__(self,student_id,student_name,age,course,department):
        self.student_id = student_id
        self.student_name = student_name
        self.age = age
        self.course = course
        self.department = department

    def display_details(self):
        print("\n-----Student Details-----")
        print(f"Student ID         : {self.student_id}")
        print(f"Student Name       : {self.student_name}")
        print(f"Student Age        : {self.age}")
        print(f"Student Course     : {self.course}")
        print(f"Student Department : {self.department}")


#Student Management System Class

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Helper Methods

    def get_valid_id(self):
            while True:
                try:
                    student_id = int(input("Enter Student ID:"))
    
                    duplicate =False
    
                    for student in self.students:
                        if student_id == student.student_id:
                            print("Student ID already exists!")
                            duplicate =True
                            break
    
                    if duplicate:
                        continue
                    return student_id
                
                except ValueError:
                    print("Invalid Input.Please enter a number.")

    def get_valid_age(self):
        while True:
            try:
                age = int(input("Enter Student Age:"))

                if age < 1 or age > 120:
                    print("Age must be between 1 and 120.")
                    continue

                return age
            
            except ValueError:
                print("Invalid input. Please enter a number.")


    def get_student_name(self):
        while True:
            student_name = input("Enter Student Name:").strip()

            if not student_name:
                print("Student name cannot be empty")
                continue
            return student_name

        
    def get_course(self):
        while True:
            course = input("Enter Student Course:").strip()

            if not course:
                print("Course cannot be empty.")
                continue
            return course

        
    def get_department(self):
        while True:
            department = input("Enter Student Department:").strip()

            if not department:
                print("Department cannot be empty.")
                continue
            return department
    def find_student_by_id(self,student_id):

        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_integer(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except ValueError:
                print("Invalid input. Please enter a number.")
    

    # CRUD Operations

    def add_student(self):

        student_id = self.get_valid_id()
        student_name = self.get_student_name()
        age = self.get_valid_age()
        course = self.get_course()
        department = self.get_department()

        student = Student(student_id,student_name,age,course,department)

        self.students.append(student)
        print("\nStudent added successfully.")


    def view_students(self):
            if len(self.students) == 0:
                print("No student found")
            else:
                for student in self.students:
                    student.display_details()


    def search_student(self):
        search_id = self.get_integer("Enter Student ID to Search:")

        student = self.find_student_by_id(search_id)

        if student:
            student.display_details()
        else:
            print("Student not found")



    def update_student(self):
        update_id = self.get_integer("Enter Student ID to Update:")

        student = self.find_student_by_id(update_id)

        if student is None:
            print("Student not found.")
            return 
        
        new_name = self.get_student_name()
        new_age = self.get_valid_age()
        new_course = self.get_course()
        new_department = self.get_department()

        student.student_name = new_name
        student.age = new_age
        student.course = new_course
        student.department = new_department

        print("\nStudent updated successfully.")
        student.display_details()


    def delete_student(self):

        delete_id = self.get_integer("Enter Student ID to Delete:")

        student = self.find_student_by_id(delete_id)

        if student is None:
            print("Student not found.")
            return

        conform = input("Are you sure you want to delete this student? (Y/N):")

        if conform.upper() == "Y":
            self.students.remove(student)
            print("Student delete successfully.")
        else:
            print("Delete operation cancelled.")


    
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

