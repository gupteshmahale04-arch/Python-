# Chapter 9 - OOPs (Object-Oriented Programming) 

Object-Oriented Programming (OOP) helps us structure programs using real-world concepts like objects, classes, attributes, and behaviors. Instead of writingeverything in one place, we organize code into objects - just like real-life entities.
- Example:
A Student, Car, Bank Account, Mobile Phone - each can be represented as an
object in Python.

# 1 What is OOP?
- OOP is a programming style where we use:
· Class -> Blueprint
· Object -> Real instance
· Attributes -> Data
· Methods -> Behaviors (functions inside classes)

- Using OOP makes code:
· Reusable
· Organized
· Esey to maintain
·Similar to real-world objects 
 
 # Class and Object
 - Class: A  biueprint/template
 - Object: A real entity created from the class
  - Example : 
-            class Student :
                    name="Guptesh Mahale " # attribute
              # creating object
              s1 = Student()
              print(s1.name)
- Output :
-      Guptesh Mahale

# Instance Attributes VS Class Attributes
- Class Attribute 
shared by all objects
-      class Student:
          college="XYZ Institute"

- Instance Attribute 
Unique for each object 
-         class Student :
               college="XYZ Institute"
               def _ _init_ _(self,name):
                   self.name=name
        s1=Student("Guptesh")
        s2=Student("Amne")

# 4 The_init__ () Constructor
The __ init __ () function runs automatically whenever an object is created. I
It is used to initialize attributes.
- Example
-     class Student :
            def __ init __ (self, name) :   
                    self.name = name
            s1 = Student("Saumya Singh")
            print(s1.name)

# Methods (Functions inside Class)
Methods define what an object can do.
- Example
-           class Student:
                def __ init __ (self, name) :
                    self.name = name
                def hello(self) :
                    print("Hello", self.name)
            s1 = Student("Saumya")
            s1. hello()



# Static Methods
Static methods do not use self.
They are used for utility-level functions.
- Example
-          class Student:
               @staticmethod
               def school() :
                     print("ABC Public School") # generic name


Practice Questions - Static Methods
1. Create static method to validate if a number is even.
7 OOP Concepts - Abstraction &
Encapsulation
Abstraction
Showing only essential details, hiding internal complexity.
Example:
You use Instagram without knowing its backend code.
In Python:
class Payment :
def pay(self):
print("Payment Successful")
Encapsulation
Wrapping data + methods inside a single unit (class).
Data is protected using private variables.
Example:
class Account:
def __ init __ (self, bal) ;
self .__ balance = bal
# private
def show_balance(self) :
print["Balance:", self .__ balance)


 
  




