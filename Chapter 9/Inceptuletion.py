

class Animul:
     name="lion"#public attribute
     _age=55
     __M_no=411

     def speek(self): #public object metheds
          print("Lion is good")

     def _Troke(self):#protected object metheds
          print("troke")

     def __mep(self):#privet object metheds
          print("location")

obj=Animul()
obj.__M_no

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