class Animal:
    name = "lion" #public attribute
    _age = 12 #protected attribute
    __height = 120 #private attribute

    def speak(self):   # public object method 
        print("the lion roars")
    
    def _walk(self,a):  #protected object method 
        self.a=a
        print("the lion is walking ")
    
    def __sleep(self): #private method
        print("the lion is sleeping ")

class B(Animal):
    def Show(self,a):
        super()._walk(a)
        print(self.a)
        print("This is class B Show method")


obj1 = Animal()
obj1._walk(444)
obj2=B()
obj2.Show(5655)
# print(obj1.__height)
# obj1.__sleep()