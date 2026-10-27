# 🔲 Introduction to Functions
A function in Python is a block of reusable code that performs a specific task. Instead of writing the same lines repeatedly, we define a function once and use it multiple times.
- Example (without function):
         
                  print("Hello Saumya")
                  print("Hello Saumya")
                  print("Hello Saumya")

- Using a function:
               def greet():
                    print("Hello Saumya Singh")

               greet()
               greet()


# Function Definition and Calling in Python
- Definition: Use the def keyword to define a function.
- Calling: Call the function by writing its name followed by parentheses.
- Syntax:
-    def function_name():
          #code block 

- Example :
        def Welcoom_msg():
    print("WELCOOM TO MY LEPTOP")

        Welcoom_msg()
        Welcoom_msg()

 # Function Parameters & Arguments
Functions can accept parameters, which are data passed from outside. The values given when calling the function are called arguments.
- Example:
            def greet(name):
    print("Hello", name)

        greet("Saumya Singh")

        def add(a, b):
            print("Sum =", a + b)

        add(5, 10)

# Return Statement in Python
The return statement is used to send a value back from a function.After return, the function stops execution.
- Example:
            def add(a, b) :r
                return a + b
            result = add(10, 20)
                print("Result =", result)
#  Default & Keyword Arguments
Default Arguments
If no argument is provided, a default value is used.
def greet(name="Saumya") :
print ("Hello", name)
greet ()
greet ("Riya")


# Keyword Arguments
We can use the parameter name while passing values.
def student_info(name, age) :
    print(name, "is", age, "years old.")
student_info(age=21, name="Saumya Singh")


# Variable Scope (Local vs Global)
I
. Local Variable: Defined inside a function - accessible only within it.
· Global Variable: Defined outside any function - accessible everywhere.
Example:
            # global variable
X = 10
def show () :
#local variable
x = 5
print("Inside function:", x)
show()
print("Outside function:", x)
  

# None in Python
None means no value.
If a function does not return anything, it automatically returns None.
Example:
def greet():
print ("Hello Saumya!")
result = greet()
print(result)
Output:


