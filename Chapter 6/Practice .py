# # # Write a program to print nummber from 1 to 10 using wile loop
# num=1
# while(num<=10):
#     print(num)
#     num=num+1

# #     # Write a program to print nummber from 10 to 1 using wile loop
# num_ =10
# while(num_>=1):
#     print(num_)
#     num_=num_-1

# #- Print all even numbers between 1 and 50 using a while loop.

# num=1

# while(num<=50,):
#     if(num%2==0):5
#     print(num)
#     num=num+1
    
    

# #- Print the sum of the first n natural numbers.
# n = int(input("Enter the number: "))
# sum = 0
# while n >= 1:
#     sum = sum + 1
#     n = n - 1

# print("sumis::", sum)

# # - Print the following pattern using a while loop:

# #(          *  
# #           *   *
# #           *   *    *
# #           *   *    *    * 
# #           *   *    *    *    *  )
# nn=1
# while nn<=5:
#     print("*"*nn)
#     nn=nn+1
# n=int(input("Enter the number "))
# s=input("Enter the simbol ")
# i=1
# # sum=0
# while(i<=n):
#     # sum = sum + 1
    
    
#     print(s * i) 
#     i = i + 1

# # "Saumya wants to print her name 5 times, but each time with a number in front of it. Write a program using a while loop that prints:"

# i= 1
# while i<=5:

#     print("guptesh",i)
#     i=i+1

# # Write a program to print the multiplication table of any number using a while loop.
# # (Hint: Start i = 1 and run the loop until i <= 10.)

# num = int(input("Enter the number: "))
# print("Table of :",num)
# i=1
# while(i<=10):
#    table=num*i
#    print( i,"*",num,"=" ,table)
#    i=i+1
# . Print all even numbers between 1 and 20 using for and range()
for item in range(0,21,2):
    print(item)
#  Print numbers from 1 to 50, but print "Saumya Singh" instead of multiples of 5
for item in range(1,51,1):
    print(item,"Guptesh mahale ")
#  Print the square of each number from 1 to 10
for item in range(1,21,1):
    print(item)
# Multiplication table of a number entered by the user
i=int(input("Enter the no.::"))
for item in range(1, 11):
    print( item,"*",i,"=",item*i)
#  Print numbers from 100 to 1 using for and range()
for item in range(1000,0,-1):
    print(item) 
# Print Saumya's username five times in uppercase
username = "Saumya"
for i in range(5):
    print(username.upper())

# Write a program that prints numbers 1 to 10, but skips the number 7 using the
# continue statement.
# Iterate through numbers 1 to 10
for i in range(1, 11):
    # Check if the number is 7
    if i == 7:
        continue  # Skip the rest of the code inside the loop for this iteration
    print(i)

# Write a program using nested loops to print this pattern:

# Practice Set (Quick Recap)
# 1. Print numbers from 1 to 100 using a for loop.
# 2. Print numbers from 100 to 1 using a while loop.
# 3. Print all numbers between 1 and 50 except multiples of 5.
# 4. Create a program that asks the user for 5 favorite foods and prints them one
# by one.



