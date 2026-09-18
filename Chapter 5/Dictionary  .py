print("Enter the Informetion of 1 Roll no of student")

Name=input("enter the name of student " )
Roll=(input("enter the Roll No of student "))
Father =input("enter the name of father  of student " )
Mather =input("enter the name of mather  " )
Add =input("enter the Add of father   " )
add=input("enter the Add of student " )
marks=input("enter the mark" )

S1={ "name": Name, "roll":Roll,"father":Father,"mather":Mather,"add1":Add, "Add":add,"Marks":marks}
print(S1)
print(type(S1))
# find the 
print(S1["name"])
# chang the value of A KEY
S1["roll"]="15"  
print(S1)
# add the value and key
S1["yres"]="2007"
print(S1)
# detetion
S1.pop("yres")
print(S1)
# find keys 
print(S1.keys())

# find value
print(S1.values())

# item 
print(S1.items())