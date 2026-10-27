#class creation
class Vehicle :
    color="Black"
    fiul="Petrol"
    mileage="60"

    def start(): #mathods
        print("When you press clutch and accelerator then vehicle is started  ")

#object creation
car=Vehicle()
print(car.color)

bike=Vehicle()
print(bike.color)


aeroplane=Vehicle()
print(aeroplane.mileage)

# We created 3 objects

# _ _init_ _

class Student :
    schoolName="ABC School"

    def __init__(self,name,course ):
         print("When a new object")
         self.name=name
         self.course=course  
         print(self.name)
         print(self.course)

Student1=Student("Guptesh","m tech")#init method will be called
print("Student 1 Name-", Student1.name)   
print("Student1 Course-",Student1.course)                                     

Student2=Student("ram","b tech")
print("Student 2 Name-", Student2.name)   
print("Student 2  Course-",Student2.course)                                     
