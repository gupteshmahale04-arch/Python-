# # primitiv aproch 

# # a=12
# # b=479
# # a+b


# # functional  aproch 
# # def add(a,b):
# #     return a+b  
# # add(12,479) 



# # oop aproch
# # class Calculator:
# #     def add(self,a,b):
# #         return a+b  
    

# """
# class SarmaVishnu:  #bluprint of object  

#     a="lala"

#     def sample():
#         print("This is the sempal :")


#     def sample2():
#         print("This is the sempal2 :")
# SarmaVishnu.sample2()
# SarmaVishnu.sample()  #class ke ander ke function ko  method  bolte hi

# print(SarmaVishnu.a) #class ke ander ke veriabul ko atribut bolte hi 

# print(SarmaVishnu.a)"""


# class Animul:
#     #Attribute
#     name="Animul"
#     #Method 
#     def greet(self): # jab bhi class ke andar ke function ko object ji ki help se call karoge toh ek parameter set karna hoga 
#         print("this is Animul Class")

# tau=Animul()
# tau.greet()
# print(tau.name)

# class  Ram :
#     def greed(self):
#         print("this is class ram 1")
#     def add(self):
#         a=12
#         b=45
#         c=45
#         print(a+b+c)
#     def add(self):
#         a=12
#         b=45
#         c=455
#         print(a+b+c)        
     
# obj=Ram()
# obj.greed()
# obj.add()  # jab bhi class ke andar ke function ko object ji ki help se call karoge toh ek parameter set karna hoga 
# obj.add() 




# #________________________________________________________________________________19/05/2026__________________________________________________________________________________________________________

# # constructer -> reperesent by __init__()(Dunder method)  constructer  sabse pehle oehle exicut hoga jo  


# class guptesh:
#     def __init__(self):  # constructer 
#         print("this is the constructer of class guptesh")

#     def greet(self):
#         print("this is the method of class guptesh")    

#     def __init__(self):  # constructer 
#         print("this is the constructer of class guptesh22")

# obj=guptesh()  # jab bhi class ke object ko call karoge toh constructer sabse pehle exicut hoga
# obj.greet()  # method ko call karne ke liye object ji ki help se call karna hoga    






"""class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        print(f"The tanth student :;{name}.thats age is::{age}")

    def deteal (self):
        print(self.name)
        print(self.age)

obj = student("gup",15)
obj.deteal()


class roro:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def greter(self):
        if self.a>self.b :
            print("a bada hi ")
        
        else:
            print("b bada hi ")

obj = roro(1,5)
obj.greter()"""

#---------------------------------------------------------------------------------------20/05/2026---------------------------------------------------------------------------------------------------------------------------------------

#


# class Animul:
#     name="dog" #class atribut
# # tochang atribut 
#     @classmethod
#     def change(cls,new): #self -> object
#         cls.name= new
#         print(cls.name)

# obj=Animul()
# obj.change("cat")


#

class Shayam :

    @staticmethod # obj bane ya  na  bane #
    def Manu():
        print("roti")
        print("Sabji")


obj=Shayam()
obj.Manu()
