class Student:
    def __init__(self,name,age,email,phone_NO):
        self.name=name
        self.age=age
        self.email=email
        self.phone_NO=phone_NO

        print('Welcome SSSVM Bhopal ')
    def Display(self):
        print(f""" Detals Of Student
        Name={self.name}
        Age={self.age}
        Email={self.email}
        Phone_Number={self.phone_NO}""")

class Class_10Th (Student):
    def __init__(self, name, age, email, phone_NO):
        super().__init__(name, age, email, phone_NO)
        if self.age <=14:
            print('Admission Successful')
        else:
            print('Admission Feld')

class Class_12TH (Student):
    def __init__(self, name, age, email, phone_NO):
        super().__init__(name, age, email, phone_NO)
        if self.age <=16:
            print('Admission Successful')
        else:
            print('Admission Feld')

print("Press 1 for Class 10th Admission")
print("Press 2 for Class 12th Admission")

choice=int(input("Enter Your Choice:"))
name=input("Enter Your name: ")
age=int(input("Enter Your age: "))
email=input("Enter Your email :")
phone_NO=input("Enter Your Phone Number: ")

if choice==1:

    Student1=Class_10Th(name,age,email,phone_NO)
    Student1.Display()
if choice==2:
    Student1=Class_12TH(name,age,email,phone_NO)
    Student1.Display()

 