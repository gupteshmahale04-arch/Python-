
# 🐍 Python Fundamentals: Functions and Modular Programming

A structured reference guide and practice repository covering function declarations, parameter passing, return mechanisms, argument types, variable scope, the `None` type, and practical coding exercises[cite: 63, 64, 65].

---

## 📋 Table of Contents
* [1. Introduction to Functions](#1-introduction-to-functions)
* [2. Defining and Calling Functions](#2-defining-and-calling-functions)
* [3. Parameters vs. Arguments](#3-parameters-vs-arguments)
* [4. The return Statement & the None Object](#4-the-return-statement--the-none-object)
* [5. Argument Variations](#5-argument-variations)
  * [Default Arguments](#default-arguments)
  * [Keyword Arguments](#keyword-arguments)
* [6. Variable Scope: Local vs. Global](#6-variable-scope-local-vs-global)
* [7. Practice Exercises & Solutions](#7-practice-exercises--solutions)
  * [Basic Printing Functions](#basic-printing-functions)
  * [Mathematical Operations](#mathematical-operations)
  * [Vowel and Consonant Counter](#vowel-and-consonant-counter)
* [📂 Repository File Directory](#-repository-file-directory)

---

## 1. Introduction to Functions

A **function** in Python is a reusable block of code designed to execute a specific task[cite: 63]. Instead of duplicating the same lines repeatedly throughout a program, you define a function once and invoke it as often as needed[cite: 63, 64].

### Core Advantages[cite: 63, 65]
* **Eliminates Repetition:** Reduces code duplication (DRY principle).
* **Improves Organization:** Breaks down large programs into smaller, manageable, and readable modules.
* **Simplifies Debugging:** Errors can be isolated and corrected in a single function rather than across multiple program locations.

---

## 2. Defining and Calling Functions

* **Definition:** Functions are declared using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`[cite: 63].
* **Calling:** Functions are executed by calling their identifier followed by parentheses[cite: 63].

```python
# Definition
def welcoom_msg():
    print("WELCOOM TO MY LEPTOP")

# Calling the function multiple times
welcoom_msg()
welcoom_msg()

```

*Files: `Function.md`, `Prectice_4.py*`

> ⚠️ **Execution Order:** A function must always be defined *before* it is called in Python; calling an undefined function raises a `NameError`.
> 
> 

---

## 3. Parameters vs. Arguments

* **Parameters:** Variables listed inside the parentheses during the function definition. They serve as placeholders for incoming data.


* **Arguments:** The actual values passed into the function when it is invoked.



```python
# 'a' and 'b' are parameters
def as_numbers(a, b):
    add = a + b
    sub = a - b
    print("Sum:", add, "Difference:", sub)

# 5 and 2 are arguments
as_numbers(5, 2)

```

*Files: `Function.md`, `Prectice_4.py*`

---

## 4. The `return` Statement & the `None` Object

### The `return` Statement

The `return` statement sends a calculated result back to the caller. Once encountered, function execution terminates immediately.

```python
def multiply(a=10, b=89):
    return a * b

result = multiply(5, 54)
print("Result =", result)  # Output: 270

```

*Files: `Function.md`, `Function.py*`

### The `None` Return Value

If a function completes its execution without an explicit `return` statement, it automatically returns `None`.

```python
def greet():
    print("Hello Saumya!")

output = greet()
print(output)  # Output: None

```

*File: `Function.md*`

---

## 5. Argument Variations

### Default Arguments

Default parameters provide fallback values if an argument is omitted during the function call.

```python
def average(a=6, b=8):
    average_value = (a + b) / 2
    print("Average is:", average_value)

average(4, 6)  # Uses passed values (5.0)
average()      # Uses defaults (7.0)

```

*Files: `Function.md`, `Function.py*`

### Keyword Arguments

Values can be explicitly mapped to parameter names during invocation, allowing arguments to be passed in any order.

```python
def student_info(name, age):
    print(name, "is", age, "years old.")

student_info(age=21, name="Saumya Singh")

```

*File: `Function.md*`

---

## 6. Variable Scope: Local vs. Global

Variable scope determines the accessibility of identifiers across a program:

* **Local Variable:** Declared inside a function block; accessible only within that specific function.


* **Global Variable:** Declared outside any function; accessible throughout the entire file.



```python
# Global variable
x = 10

def show():
    # Local variable
    x = 5
    print("Inside function:", x)  # Prints: 5

show()
print("Outside function:", x)      # Prints: 10

```

*File: `Function.md*`

---

## 7. Practice Exercises & Solutions

### Basic Printing Functions

Practice routines demonstrating simple definitions and repeated invocation:

```python
# Greeting message
def good_morning():
    print("Good Morning, Guptesh!")

good_morning()
good_morning()

# Simple quote display
def inspire():
    print("You are the master of your destiny : Guptesh Mahale")

inspire()

```

*File: `Prectice_4.py*`

### Mathematical Operations

Functions that process numbers via parameters, calculations, and returns:

```python
# Addition and subtraction logic
def as_numbers(a, b):
    add = a + b
    sub = a - b
    print("Addition:", add, "Subtraction:", sub)

as_numbers(5, 2)
as_numbers(7, 2)

# Calculation using power operator
def square(num):
    square_val = num ** 2
    print("Square:", square_val)

square(5)

```

*File: `Prectice_4.py*`

### Vowel and Consonant Counter

Iterates through an input string to categorize alphabetical characters into vowel and consonant frequency totals:

```python
def count_vowels_and_consonants(user_input):
    vowels = "aeiouAEIOU"
    count_vowel = 0
    count_consonant = 0

    for char in user_input:
        if char.isalpha():
            if char in vowels:
                count_vowel += 1
            else:
                count_consonant += 1

    return count_consonant, count_vowel

consonants, vowels = count_vowels_and_consonants("Guptesh Mahale")
print("Consonants:", consonants, "Vowels:", vowels)

```

*File: `Prectice_4.py*`

---

## 📂 Repository File Directory

* `Function.md`: Conceptual documentation detailing function syntax, parameters, return behaviors, default/keyword arguments, variable scope, and `None` returns.


* `Function.py`: Examples covering basic zero-parameter functions, parameter defaults, and value-returning routines.


* `Prectice_4.py`: Coding solutions for motivational displays, string inspection, multi-operator mathematics, and vowel/consonant counter algorithms.


* `Return Statement.py`: Script workspace dedicated to return-statement testing.


