
# Practice Question 1
# Write a Python program that takes a number as input and prints:
# · "Positive" if number > 0
# · "Zero" if number == 0
# · "Negative" if number < 0

num = int ( input("Enter the Number"))

if (num>0):
    print("Positive ")
elif (num==0):
    print("Zero")
else:
    print("Nagative")
# Practice Question 2
# Write a program that takes names of 3 favorite foods from the user and stores
# them in a list. Then print the list and its length.
# Example:
# Input: Samosa, Pizza, IceCream
# Output: ['Samosa', 'Pizza', 'IceCream' ]
# Total items: 3
#MATHOD 1
F1=input("Enter food 1")
F2=input("Enter food 2")
F3=input("Enter food 3")
Sabji=[F1 ,F2,F3]
print(Sabji)
#MATHOD2
Sabji.append(F1)
Sabji.append(F2)
Sabji.append(F3)
print(Sabji)

# Practice Question 3
# Create a tuple of your favorite 5 fruits.
# Then print:
# 1. The total number of fruits
# 2. The index of one selected fruit
# Example:
# fruits = ("Mango", "Apple", "Banana", "Grapes", "Orange")
# Output :

F_1=input("Enter fruits 1")
F_2=input("Enter fruits 2")
F_3=input("Enter fruits 3")
F_4=input("Enter fruits 4")
F_5=input("Enter fruits 5")

fruits=(F_1,F_2,F_3,F_4,F_5)
print(fruits)


print(len(fruits))
print(fruits.index(1))