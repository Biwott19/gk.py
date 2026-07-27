#DAY 8
#PYTHON CLASSES 

#HOOP - object oriented programming.

#class - a blueprint for creating object 

#PHONE
#Has a battery,brand,RAM,storage - ATTRIBUTES(characteristics)

#can call,charge,take a video,play music - METHODS(actions)

#FACEBOOK
#users have name, email, password, age

#users can log in, log out, post


#gilion
#name = gilion
#email = gilionbiwott@gmail.com


#TOYOTA
#Wheels, doors, engine. seats, - design
#class
#each car is an object

#class student:
    #pass

#class tells python that you are creating a class
#students is the class name
#: starts the class body
#pass it tells python that you are not adding anything

#object
#student1 = student()
#student stores an object in a variable
#students()creates a new student

#THE CONSTRUCTOR
#_init_()

#class student:
    #def_init_(self,name,course):
      #self.name = Name
      #self.course = Course

#self
#self allows each object  to keep it's own data

#student1 = student("gilion","cyber security")
#python thinks like
#self.name = "gilion"

#ATTRIBUTES
#variables inside an object

#ACCESSING ATTRIBUTES
#print(self.name)

#METHODS
#functions inside classes 



class student:
   def __init__(self, name, course):
      self.name = name 
      self.course = course
      
      
   def introduce (self):
      
       print(f"my name is {self.name}")
       print(f"i studed {self.course}")


student1 = student("GILION","IT") 
student2 = student("SANDRA","CYBER SECURITY")
student3 = student("IRINE","COMPUTER SCIENCE")
student4 = student("MERCY","SOFTWARE ENGINERING")
student5 = student("ALEX","DATA SCIENCE")

student1.introduce()
student2.introduce()
student3.introduce()
student4.introduce()
student5.introduce()


