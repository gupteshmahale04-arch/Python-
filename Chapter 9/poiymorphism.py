""""class Animul:
    def Speek(self):
        print("This is Animul class")

class Human:
    def Speek(self):
        print("This is Human Class ")

obj1=Animul()
obj2=Human()
obj1.Speek()
obj2.Speek()
#"""
#methed over writing

class Reebok:
    def __init__(self,Material,Size):
        self.Material=Material
        self.Size=Size
    
    def Details(self):
        print("your bag Details")
        print(f"Material:{self.Material}")
        print(f"Size : {self.Size}")

class Campus(Reebok):
    def __init__(self, Material, Size,color):
        super().__init__(Material, Size)
        self.color=color
    def Details(self):
        print(f"Color: {self.color}")
        print(super().Details())

obj_1 =Campus("lether","5L","bleck")

obj_1.Details

# a child class obj

#method overloading  

class POP:
    def rop(self,a):
        print('Class pop 1')    

    def rop(self,a,b):
        print('Class pop 1')   

# method overloding is a concept where you define similar name methods inside a singl class 


