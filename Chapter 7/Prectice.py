# - Practice Question:
# Write a function named welcome_message() that prints "Welcome to Python Programming!" three times.
def Welcoom_msg():
    print("WELCOOM TO MY LEPTOP")

Welcoom_msg()
Welcoom_msg()
Welcoom_msg()
Welcoom_msg()

# 2. Define a function inspire() that prints a motivational quote with your name.
def inspire():
    print("You rar the master of your destiny : Guptesh Mahale")

inspire()

# 3. Create a function good_morning() that prints "Good Morning, Saumya!". Call it twice.

def good_morning():
    print("Good Morning, Guptesh!")

good_morning( )

# 4. Why are functions used in programming? Write two advantages.
def advantages():
    print( "make more efesiant " )

advantages()

# - Write a function display_python() that prints "Python is Fun!".

def display_python() :
    print("Python is Fun!")

# - Create a function learn() that prints three Python topics.

def learn():
    print("""Python Basics
Introduction to Python & Installation
Syntax, Indentation, and Comments
Variables & Data Types (int, float, str, bool, complex)
Type Conversion & Casting
Input and Output (input(), print())
Operators (Arithmetic, Relational, Logical, Bitwise, Assignment, Membership, Identity)""")

learn()
# - Explain what happens if you call a function before defining it.

# iambest()

# - Function to show age
# Write a function show_age(name, age) that prints:
# "Saumya Singh is 21 years old."
def show_age(name,age):
    print(f"{name}is{age}year old ")

show_age("guptesh",18)





# - Function to add and subtract numbers
# Create a function add_numbers(a, b) that prints both the sum and the difference

def AS_numbers(a, b) :
    add=a+b
    sub=a-b
    print(add,sub) 

AS_numbers(5,2)
AS_numbers(6,2)
AS_numbers(9,2)
AS_numbers(7,2)


# Write a function fav_food(food) that prints:
# "Saumya loves <food>"
# Replace <food> with the actual value passed to the function.

def fav_food(food):
    print(food)

fav_food( "chavel")

# Return Statement
# 1. Write a function square(num) that returns the square of a number.
def square(num):
    square_=num**num
    print(square_)

square(5)

# 2. Write a function that takes a string and returns the count of vowels and
# separately. consonants
def func(userInput):

    vowels="aeiouAEIOU"#define vowels 

    countVowel=0
    countConsonants=0
#GUPTEAH
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel=countVowel+1
            else :
                countConsonants+=1
    return countConsonants,countVowel

# Function Call
vowels,consonants=countVowConso ("Guptesh Mahale")
print(vowels,consonants )

# 3. Define a function convert_to_upper (word) that returns the uppercase
# version of the string.
# 4. Create a function full_name (fname, Iname) that returns the full name
# joined with a space.




# Practice Questions
# 1. Define a function message(text="Keep Learning! ") and call it with and
# without an argument.
# 2. Create a function login(username, password="1234") that prints the
# credentials.

