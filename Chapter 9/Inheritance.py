#-----------------------------------------------21/05/2026--------------------------------------------------------------------------------------------------------------------------------
# 

# # Type of in heritance: 
# Single Inheritance {1 parent ,1 chaild)
# Multiple Inheritance{2 parent ,1 chaild)
# Multilevel Inheritance   {1 So, 1parent ,1 chaild} 
# Hierarchical Inheritance{1parent ,n chaild}





# Single Inheritance 
"""class Parent:

    def __init__(self):
        print(" this is parent class constructor ")

    def greet(self):
        print("this is parent class")


class Child(Parent):

    def __init__(self):
        print("this is child class Constructor")

    def show(self):
        print("this is child class ")

obj=Child()
obj.greet()
obj.show()"""

"""
class Factory:
    def _init_(self,name,color):
        self.name = name
        self.color = color
    
    def show(self):
        print(f'Bag has {self.name} and {self.color} color')
    
        
class Bata(Factory):
    def _init_(self,name,color,zip,pockets):
        super()._init_(name,color)
        self.zip = zip
        self.pockets = pockets
    
    def display(self):
        print(f'Bag has {self.name} , {self.color} color , {self.zip} zip and {self.pockets} pockets')
Rahul = Bata('Rahul','Purple',4,10)
Rahul.display()

"""




# Multiple Inheritance

"""
class Father :# 1 parent 
    def __init__(self):
        print("This is Father Class Constructerr ")


    def greet_father (self):
        print("This is Father Class ")

class Mather : #2 parent
    def __init__(self):
        print("This is Mather Class Constructerr ")


    def greet_mather (self):
        print("This is Mather Class ")

class child(Father,Mather) :  # 1 chaild
    def __init__(self):

        Father.__init__(self) # pahle 
        Mather.__init__(self)
    #     print("This is Child Class Constructerr ")



    # def greet_child(self):
    #     print("This is Chaild  Class")


obj=child()
# obj.greet_child()
obj.greet_father()
obj.greet_mather()"""

#----------------------------------------22/05/2026----------------------------------------------

# Multilevel Inheritance  (Class A -> Class B -> Class C)

"""class A:
    print("a")
    def Show(self):
        print ("This is class A")

class B(A):
    print("b")
    def greed( self):
         print ("This is class B")

class c(B):
    print("c")
    def Display( self):
         print ("This is class C")

obj=c()
obj.Display()
obj.greed()
obj.Show()

"""


"""class CEO:
    def __init__(self):
        print("this is CEO Class Constructer ")

class Manager(CEO):
    def __init__(self):
        super().__init__()
        print("this is Manager Class Constructer ")
class Employee(Manager):
    def __init__(self):
        super().__init__()
        print("this is Employee Class Constructer ")
ram=Employee()"""


### Hierarchical Inheritance 

"""class Parent:
    def greet(self):
        print("This is Perent Class")


class Child1(Parent):
    def greet(self):
        print("This is Child1 Class")


class Child2(Parent):
    def greet(self):
        print("This is Child2 Class")

obj1=Child1()
obj1.greet()

obj2=Child2()
obj2.greet()"""


class Accunt:
    def __init__(self,name,Balance):
        self.name=name
        self.Balance=Balance

    def Dateil(self):
        print(f"hello{self.name} you have{self.Balance}")

class Saving(Accunt):
    def __init__(self, name, Balance):
        super().__init__(name, Balance)
        print(f"This is Saving Class Constructer {self.name} ,{self.Balance}")

class Current(Accunt):
    def __init__(self, name, Balance,type):
        super().__init__(name, Balance)
        self.type=type
        print(f"This is Current Class Constructer {self.name} ,{self.Balance} ,{self.type}")

obj1=Saving("Rahul",10000)
obj2=Current("Rahul",10000,"Saving")