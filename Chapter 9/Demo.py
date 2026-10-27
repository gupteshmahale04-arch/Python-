"""class Animul:
    def __init__(self,Name,Breed):
        self.Name=Name
        self.Breed=Breed

    
    def Show(self):
        print (f"Animul Name :{self.Name} ")
        print(f"Breed : {self.Breed}")

class Dog(Animul):
    def __init__(self):
        print("This is Dog Class Constructor")
        
    def Deteal(self):
        print("this is class Dog")
    

obj=Dog("Ramu","Jarmensepart")
obj.Show()
obj.Deteal()"""

"""class Vehicle:
    def __init__(self, Name, Model):
        self.Name = Name
        self.Model = Model  
        print("This is class Vehicle Constructor")
        
    def show(self):
        print(f"Company : {self.Name}")  
        print(f"Model : {self.Model}")

class Bike(Vehicle):
    # 1. Accept Name and Model here so you can capture '4' and '8'
    def __init__(self, Name, Model):
        # 2. Pass those values straight up to the Vehicle constructor
        super().__init__(Name, Model)
        print("This is Bike Class Constructor")
        
    def Display(self):  # Fixed typo from 'Disply'
        print(f"Bike is {self.Name} and Model is {self.Model}")

# Now this will run perfectly
obj = Bike(4, 8)
obj.show()
obj.Display()

class Vehicle:
    def __init__(self,Name,Model):
        self.Name=Name
        self.Model=Model  
        print("This is  calss Vehicle Constructer   ")
    def show(self):
        print(f"Company : {self.Name} ")  
        print(f"Model : {self.Model}")
class Bike(Vehicle):
    def __init__(self,Name,Model):
        super().__init__(Name,Model)

        print("This is Bike  Class  Constructer ")
    def Disply(self):
        print(f"Bike is {self.Name} and Modul is {self.Model}")

obj=Bike(4,8)
obj.show()
obj.Disply()"""