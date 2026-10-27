# Practice Question 1
# Write a Python program that takes a user's name as input and prints:
# 1. The first character
# 2. The last character
# 3. The total length of the name

name = input( " Enter your name ::")

print( "The first character is :: " , name[0]) 

print("The last character is ::" , name[-1] )
 
print( " The total length of the name is  ::", len(name) )


# Practice Question 2
# Write a program that takes your favorite food name as input and prints:
# . The middle 3 characters
# . The last 2 characters
FF=input("Enter your favorite food name ")
middle=FF[2:7]
last=FF[-6:-4]
print("The middle 3 characters",middle)
print("The last 2 characters",last)
  

# Practice Question 3
# Write a program that:
# - Takes a sentence as input
# - Converts it to lowercase
# - Replaces all spaces " " with underscores "_"
# - Prints the new string 

sentence= input("Enter sentence ::") 
print( sentence.count())
print( sentence.upper())
print( sentence.lower())
print( sentence.title())
print( sentence.capitalize())
replace=input("Replace Charectur")
replaced=input("Replace Charectur")
print( sentence.replace( (replace) ,(replaced) ))

find=input("Find the charectur")
print( sentence.find(find))

print( sentence.endswith())




 

