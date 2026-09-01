from database import add_student_to_db,get_all_students,update_student_in_db,delete_student_in_db,check_student_id,get_student_by_id


# Student Class
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


# Student Management System Class

class StudentManagementSystem:


    # Helper Methods

    def get_valid_id(self):
            while True:
                try:
                    student_id = int(input("Enter Student ID:"))
    
                    find_student = check_student_id(student_id)

                    if find_student:
                        print("Student exists.Try another ID.")
                        continue
                    else:
                        print("Student does not exist.")
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

        row = get_student_by_id(student_id)

        if not row:
            return None
        
        student = Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
        return student


    def get_integer(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except ValueError:
                print("Invalid input. Please enter a number.")


    def pause(self):
        input("\nPress Enter to continue...")


    def get_confirmation(self,message):
        while True:
            answer = input(message).strip().upper()

            if answer in ["Y","YES","N","NO"]:
                return answer
            print("Invalid input. Please enter Y/Yes or N/No.")


    def get_menu_choice(self):
        while True:
            choice = input("Enter Your Choice: ")

            if choice not in ["1","2","3","4","5","6"]:
                print("Invalid choice.")
                continue
            return choice

    # User Interface

    def display_menu(self):
        print("\n===Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")


    # CRUD Operations

    def add_student(self):

        student_id = self.get_valid_id()
        student_name = self.get_student_name()
        age = self.get_valid_age()
        course = self.get_course()
        department = self.get_department()

        student = Student(student_id,student_name,age,course,department)

        add_student_to_db(student)

        print(f"\nStudent {student_id} added successfully.")
        self.pause()


    def view_students(self):
        rows = get_all_students()

        if not rows:
            print("\nNo students found.")
            self.pause()
            return
        print(f"\nTotal students:{len(rows)}")

        for row in rows:

            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

            student.display_details()
        self.pause()
            


    def search_student(self):
        search_id = self.get_integer("Enter Student ID to Search:")

        student = self.find_student_by_id(search_id)

        if student:
            student.display_details()
            self.pause()
        else:
            print("Student not found")
            self.pause()



    def update_student(self):
        update_id = self.get_integer("Enter Student ID to Update:")

        student = self.find_student_by_id(update_id)

        if not student:
            print("Student not found.")
            self.pause()
            return 
        confirm = self.get_confirmation("Are you sure you want to update this student? (Y/N): ")

        if confirm in ["Y","YES"]:

            new_name = self.get_student_name()
            new_age = self.get_valid_age()
            new_course = self.get_course()
            new_department = self.get_department()

            student.student_name = new_name
            student.age = new_age
            student.course = new_course
            student.department = new_department
            update_student_in_db(student)

            print(f"\nStudent {update_id} updated successfully.")
            student.display_details()
            self.pause()
        else: 
            print("\nUpdate operation cancelled.")
            self.pause()


    def delete_student(self):

        delete_id = self.get_integer("Enter Student ID to Delete:")

        student = self.find_student_by_id(delete_id)

        if not student:
            print("\nStudent not found.")
            self.pause()
            return

        confirm = self.get_confirmation("Are you sure you want to delete this student? (Y/N):")

        if confirm in ["Y","YES"]:
            delete_student_in_db(student)
            print(f"\nStudent {delete_id} deleted successfully.")
            self.pause()
        else:
            print("\nDelete operation cancelled.")
            self.pause()


# Main Program

    
sms = StudentManagementSystem()

while True:
    sms.display_menu()

    choice = sms.get_menu_choice()

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
        print("\nThank You!")
        break

