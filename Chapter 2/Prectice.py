# W A PP that takes your age as input and print 
# ** The value entered
# ** its type  
age = int(input("enter your age"))

print(type(age))

print = ( " User age is :",age)


 


#  try to create a variable named for in python .What error do you  get and why?
# for3 = "name"(Expected expression )
    

    # Print sum program and average  program 
    #  Example program to input two numbers and print their sum : 
num1=int(input("Enter 1st Number :"))  

num2=int(input("Enter 2ed  Number :"))
 
sum =num1+num2



print("Sum of 1st & 2ed Number is :",sum)
 
avr = sum/2

print("average of 1st & 2ed Number is :",avr)

#  Take a number as input , convert it to a float and print both the original and converted values with their data types .
num =input("Enter Data :")
print(type(num))
num_1 = int(num)
num_2 = float(num)
num_3 = bool(num)
num_4 = str(num) 

print( "Data is orignal  :",num ,"Data type is :",type(num))
print( "Data is  in integer :",num_1,num ,"Data type is :",type(num_1))
print( "Data is float :",num_2,num ,"Data type is :",type(num_2))
print( "Data is  booliun:",num_3,num ,"Data type is :",type(num_3))
print( "Data is  string :",num_4,num ,"Data type is :",type(num_4))

#  Practice Question:
# Write a program that takes two numbers and prints:
# . Their sum, difference, and product
# . Whether the first number is greater than the second
 
a=int(input(" Enter 1st number"))
b=int(input(" Enter 2ed number"))
print( " Enter 1st number:",a)
print( " Enter 2ed number:",b)
print(a+b)
print(a/b)
print(a%b)
print (a>b)
