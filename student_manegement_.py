#step 1
class Student:
    def __init__(self,id,name,age,course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

s1 = Student(1,"Seshagiri",23,"MCA")
s1.display()
