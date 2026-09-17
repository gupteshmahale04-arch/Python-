# Conditional Statements in Python
Conditional statements allow your program to make decisions — run different parts of code based on certain conditions.
- What Are Conditions?
- A condition is simply a statement that can be either True or False.
- Example:
-        age = 18
         print(age == 18)  # True
If Statement 
- Used to run block of code only when the condition is True .
-        age = int(input("Enter your age :"))         
         if age >= 18 :
             print(" You are eligible to vote")
- if the condition is false , nothing happend .

If-else Statement 
- Used to run block of code only when the condition is foles with the crayteriya .
-              marks = int (input ("Enter your marks :"))
               
               if markes >= 40 : 
                   print("You passed !")
                eles :
                   print(  "  You failed")
        
If- elif-eles Statement 
-         Used when we have multiple conditions . 
# Conditional statement for grading
marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Your grade is A+")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your grade is B+")
elif marks >= 60:
    print("Your grade is B")
elif marks >= 50:
    print("Your grade is C+")
elif marks >= 40:
    print("Your grade is C")
else:
    print("You are fail")

# Lists in Python 
A list is built-in dataa type that can store multiple values in  a single variable     lists are mutable (Cen be changed) and can store different data types.
- Example :
-           marks = [ 87 , 64 , 68 , 67 , 89 ]
            foods = [ "Samosa ", "Pizza" , "Burger"]
            student = [ " guptesh mahale " , 18 , "betul" ]
# Accessing Elements (Indexing)
- Each item in a list has an index starting fr
-       foods = ["Samosa", "Pizza", "Burger" ]
        print(foods[0])    # Samosa
        print(foods[2])    # Burger

# Modifying Elements
Lists are changeable.
foods[0] = "GulabJamun"
print(foods)    #  [ 'GulabJamun', 'Pizza', 'Burger' ]
# List Slicing
You can extract parts of a list using slicing.
-            marks = [87, 64, 33, 95, 76]
             print(marks [1:4]) # [64, 33, 95]
             print(marks[ :3])  # [87, 64, 33]
             print(marks[-3 :- 1]) # [33, 95]


**List Functions**

| **Function**   | **Description**           | **Example**         |
|----------------|---------------------------|---------------------|
| `len(list)`    | Returns length of list    | `len(marks)` → 5    |
| `max(list)`    | Returns largest value     | `max(marks)` → 95   |
| `min(list)`    | Returns smallest value    | `min(marks)` → 33   |
.
Method           : .append(el)
Description      : Adds element at the end
Example          : marks.append(99)

Method           : .insert(i, el)
Description      : Inserts element at index
Example          : marks.insert(1, 80)

Method           : .remove(el)
Description      : Removes first occurrence
Example          : marks.remove(64)

Method           : .pop(i)
Description      : Removes element at index
Example          : marks.pop(2)

Method           : .sort()
Description      : Sorts list in ascending order
Example          : marks.sort()

Method           : .reverse()
Description      : Reverses the list
Example          : marks.reverse()

#  Tuples in Python
Definition
A tuple is a built-in data type that stores multiple values like a list, but it is
immutable (cannot be changed after creation).

-       tup = (87, 64, 33, 95, 76)
        print(tup[0])  # 87
