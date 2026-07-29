class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

    def role(self):
        print("I am a person.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studing {self.course}.") 

    def role(self):
        print("I am a student.") 


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.") 

    def role(self):
        print("I am a teacher.")


class Principal(Person):
    def __init__(self, name, age, school_name):
        super().__init__(name, age)
        self.school_name = school_name

    def manage_school(self):
        print(f"{self.name} is managing {self.school_name}.")

    def role(self):
        print("I am the principal.")


#Creating objects
student = Student("Gilion",25, "Computer science")
teacher = Teacher("Mr.Job", 35, "Python")
principal = Principal("Mrs.Mary", 50, "Coding Time Academy")

#Testing Student
student.introduce()
student.study()
student.role()
print()

#Testing Teacher
teacher.introduce()
teacher.teach()
teacher.role()
print()

#Testing Principal
principal.introduce()
principal.manage_school()
principal.role()

                                          

                        