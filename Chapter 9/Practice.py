# Create a class Car with attribute brand = "Scorpio"
class Car :
    brand="Scorpio"

obj1=Car()
print("Brand name is -",obj1.brand)

# Create a class Leptop with attributes : brand ,Ram ,Price

class leptop:
    brand="hp"
    Ram="16GB"
    price="55k" 

leptop1=leptop()
leptop1.brand="mac"
leptop1.Ram="8"
leptop1.price="56k"
print("Laptop1 Brand=",leptop1)

leptop2=leptop()
leptop2.brand="msi"
leptop2.Ram="86"
leptop2.price="66k"

print("Laptop2 Brand=",leptop2)

# Create class Student that takes 3 marks and has a method average().
class Student:

    def __init__(self,name,listofmark):
        self.name=name
        self.listofmark=listofmark

    def average( self) :
        sum=0
        for eachvalue in self.listofmark:
            sum=sum+eachvalue
        average=sum/3
        print("Average is : ",average)
Student1=Student("Aditya",[58,56,54])
print("Average Marks :",Student1.average() )
