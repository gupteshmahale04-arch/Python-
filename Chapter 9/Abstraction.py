
# from abc import ABC, abstractmethod

# class Shapes(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(abc):
#         pass

# class Square(Shapes):

#     def __init__(self,radius):
#         self.radius=radius

#     def Area(self):
#         pass
    
#     def perimeter():
#         pass
         

# obj=Square(11)
# 
# 
# Dender methods     

class Robots():
    a=12
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"hello i am {self.name} "
    
obj1=Robots("dojo")
obj2=Robots("mojo")
print(obj1)
print(obj2)


class Numbers:
    def __init__(self,value):
        self.value=value

    def __add__(self, other):
        return self.value+other.value
    
    def __eq__(self, value):
        return self.value==value.value
    
a=Numbers(20)
b=Numbers(30)
print(a+b)
print(a==b)
    

#
# class Animal:
#     name = "lion" #public attribute
#     _age = 12 #protected attribute
#     __height = 120 #private attribute

#     def speak(self):   # public object method 
#         print("the lion roars")
    
#     def _walk(self):  #protected object method 
#         print("the lion is walking ")
    
#     def __sleep(self): #private method
#         print("the lion is sleeping ")



# obj1 = Animal()
# # print(obj1.__height)
# obj1.__sleep()

# #private attributes and methods cannot be accessed by 
# #your objects and inherited classes 




# def hello():
#     print("hello how are you")

# def hello():
#     print("hello again ")

# hello()


# class Animal:
#     a = "lion"
#     def speak(self):
#         print("animals are shouting ")

# class Human:
#     a = "harsh"
#     def speak(self):
#         print("humans are intelligent so they are speaking")

# obj1 = Animal()
# obj2 = Human()

# obj1.speak()
# obj2.speak()
# both the speak methods appears to be 
# same but both have different task and this is 
# known as polymorphism



class Reebok:
    def __init__(self,material,size):
        self.material = material 
        self.size = size 

    def details(self):
        print("your bag detail is : ")
        print(self.material)
        print(self.size)

class Campus(Reebok):
    def __init__(self, material, size,color):
        super().__init__(material, size)
        self.color = color
    
    def details(self):
        print(self.color)
        print(super().details())
        

obj1 = Campus("leather",10,"black")

obj1.details()

#a child class object has the power to call methods and 
#attributes of a parent class but he cannot call the details 
#method of his parent class cause that details methods 
#is overridden and this concept is known as method 
#overriding.


class animal:

    def hello(self,a):
        print("how are you ")
    
    def hello(self,a,b):
        print("how are you man ")

#method overloading is a concept where you define 
#similar name methods inside a single class with 
#different parameters 


# class Animal:
#     __name = "harsh"
#     def __init__(self,name):
#         self.name = name

#     @classmethod
#     def __detail(cls):
#         print(cls.__name)



# obj = Animal("harsh")

# obj.__detail()