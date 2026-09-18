
# 🐍 Python Fundamentals: Data Types, Operators, and Type Conversion

A complete guide and code reference covering Python built-in data types, keyword restrictions, operators, type casting mechanisms, and real-world calculation scripts[cite: 52, 53, 54, 55, 56, 57, 59].

---

## 📋 Table of Contents
* [1. Python Data Types & type()](#1-python-data-types--type)
* [2. Python Keywords](#2-python-keywords)
* [3. Operators Overview](#3-operators-overview)
  * [Arithmetic Operators](#arithmetic-operators)
  * [Comparison Operators](#comparison-operators)
  * [Logical Operators](#logical-operators)
  * [Identity Operators](#identity-operators)
* [4. Type Conversion (Casting)](#4-type-conversion-casting)
  * [Implicit Conversion](#implicit-conversion-automatic)
  * [Explicit Conversion](#explicit-conversion-manual)
* [5. Practice Exercises & Calculations](#5-practice-exercises--calculations)
  * [Smart Temperature Converter](#smart-temperature-converter)
  * [Bill Split Calculator](#bill-split-calculator)
  * [Number Statistics & Logic Checks](#number-statistics--logic-checks)
* [📂 Repository File Directory](#-repository-file-directory)

---

## 1. Python Data Types & `type()`

Python automatically assigns and identifies data types based on the assigned value[cite: 53, 54]. Use the `type()` built-in function to inspect the data type of any variable[cite: 53, 54]:

```python
food = " samosa "    # String (str)
age = 12             # Integer (int)
area = 123.321       # Floating-point number (float)

print(type(age))     # Output: <class 'int'>
print(type(area))    # Output: <class 'float'>

```

*File: `Data Types .py*`

---

## 2. Python Keywords

Keywords are reserved words that carry dedicated meanings in Python and **cannot** be used as variable identifiers. Attempting to declare a variable using a keyword triggers an `Expected expression` syntax error.

* View the complete list of system keywords in Python:


```python
help("keywords")

```


*File: `KeyWords.py*`

* **Common Keywords:** `False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`.



---

## 3. Operators Overview

Operators execute mathematical, logical, and relational evaluations on operands.

### Arithmetic Operators

Perform numerical computations:

* `+` : Addition


* `-` : Subtraction


* `*` : Multiplication


* `/` : Division (always returns a float)


* `%` : Modulus (returns the division remainder)


* `**` : Exponentiation (power)



```python
x = 454
y = 455

print(x + y)    # 909
print(x - y)    # -1
print(x * y)    # 206570
print(x / y)    # 0.9978...
print(x % y)    # 454
print(x ** y)   # Exponentiation result

```

*File: `Operators  .py*`

### Comparison Operators

Evaluate expressions and return a boolean (`True` or `False`):

* `==` : Equal to


* `!=` : Not equal to


* `>`  : Greater than


* `<`  : Less than


* `>=` : Greater than or equal to


* `<=` : Less than or equal to



### Logical Operators

Combine conditional statements:

* `and` : Returns `True` if both conditions are true


* `or`  : Returns `True` if at least one condition is true


* `not` : Inverts the boolean state



```python
print(x < y or y < x)     # True
print(x < y and y < x)    # False
print(not x < y)          # False

```

*File: `Operators  .py*`

### Identity Operators

* `is` : Checks if both variables reference the exact same memory object.


```python
print(x is y)

```


*File: `Operators  .py*`


---

## 4. Type Conversion (Casting)

### Implicit Conversion (Automatic)

Python automatically converts smaller data representations to broader types to prevent data loss:

```python
x = 12       # int
y = 15.3     # float
a = x + y    # Automatically cast to float: 27.3
print(a)

```

*File: `Type Conversion.py*`

### Explicit Conversion (Manual)

Converting values manually using built-in casting functions: `int()`, `float()`, `str()`, and `bool()`.

```python
x = "15"

y_int = int(x)      # str -> int (Output: 20)
print(y_int + 5)

y_float = float(x)  # str -> float (Output: 20.0)
print(y_float + 5)

y_bool = bool(x)    # Non-empty string evaluates to True (1 + 5 = 6)
print(y_bool + 5)

```

*File: `Type Conversion.py*`

---

## 5. Practice Exercises & Calculations

### Smart Temperature Converter

Accepts temperature in Celsius and computes the equivalent values in Fahrenheit and Kelvin using explicit conversion formulas:

* $\text{Fahrenheit} = (C \times \frac{9}{5}) + 32$

* $\text{Kelvin} = C + 273.15$


```python
tempr_ = input("Enter the Temperature (in Celsius ::)")
tempr_c = float(tempr_)

tempr_f = (tempr_c * 9/5) + 32
tempr_K = tempr_c + 273.15 

print("Temperature in Fahrenheit : ", tempr_f)
print("Temperature in Kelvin : ", tempr_K)

```

*File: `Assignment.py*`

### Bill Split Calculator

Calculates individual payments by dividing total expenses across a group while logging tracking types:

```python
B = input(" Enter total bill amount ::")
P = input(" Enter the person :: ")

BillA = float(B)
Person = float(P)

calculator = BillA / Person
print("Bill Split amount :: ", calculator)

```

*File: `Assignment.py*`

### Number Statistics & Logic Checks

Collects two numbers and evaluates fundamental mathematics alongside comparison benchmarks:

```python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("Sum:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Is 1st greater than 2nd?:", a > b)

```

*File: `Prectice.py*`

---

## 📂 Repository File Directory

* `Assignment.py`: Scripts implementing the Celsius converter and group bill splitter.


* `Data Types .py`: Examples demonstrating `type()` checks on strings, integers, and floats.


* `DT&O.md`: Notes covering data type definitions, Python keywords, type conversions, and operators.


* `KeyWords.py`: Helper script running `help("keywords")` to inspect Python reserved names.


* `Operators  .py`: Implementations of arithmetic, comparison, logical, and identity operators.


* `Prectice.py`: Exercises covering user age input, type casting, two-number sums, averages, and comparisons.


* `Type Conversion.py`: Demonstration of implicit conversion and explicit casting (`int`, `float`, `bool`).



```

```
