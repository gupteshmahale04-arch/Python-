
# 🐍 Python Fundamentals: Loops and Iterations

A complete learning module and reference workspace covering loop repetitions, `while` loops, sequence iterations using `for`, the `range()` function, control statements (`break`, `continue`, `pass`), nested iterations, practice problems, and mini projects.

---

## 📋 Table of Contents
* [1. Why Loops?](#1-why-loops)
* [2. The while Loop](#2-the-while-loop)
* [3. The for Loop](#3-the-for-loop)
  * [Iterating Over Collections](#iterating-over-collections)
  * [The range() Function](#the-range-function)
* [4. Loop Control Statements](#4-loop-control-statements)
  * [break Statement](#break-statement)
  * [continue Statement](#continue-statement)
  * [pass Statement](#pass-statement)
* [5. Nested Loops](#5-nested-loops)
* [6. Mini Projects](#6-mini-projects)
  * [Countdown Timer](#countdown-timer)
  * [Multiplication Tables](#multiplication-tables)
* [7. Practice Problems](#7-practice-problems)
* [📂 File Directory](#-file-directory)

---

## 1. Why Loops?

Loops execute a code block repeatedly without duplicating lines manually. They are ideal for:
* Printing repeated text messages or counters.
* Traversing lists, tuples, and strings.
* Generating numerical series or geometric patterns.

---

## 2. The `while` Loop

A `while` loop runs continuously as long as its target condition evaluates to `True`.

### Syntax
```python
while condition:
    # code block

```

### Examples

```python
# Counter loop
i = 1
while i <= 5:
    print("Hello, Saumya Singh!")
    i += 1

```

*File: `Loops.md*`

```python
# Iterating up to 100
num = 1
while num <= 100:
    print("Guptesh Mahale")
    num += 1

print("NOW we are out of the while loop")

```

*File: `Loops.py*`

---

## 3. The `for` Loop

A `for` loop iterates sequentially across items within a sequence (such as lists, tuples, strings, or number ranges).

### Iterating Over Collections

```python
# Iterating through a List
food_list = ["parate ", "Roti ", "Nan", "makaroto"]
for item in food_list:
    print(item)

# Iterating through a Tuple
food_tuple = ("parate ", "JavariRoti ", "Nan", "MAkaroto")
for each_item in food_tuple:
    print("Type of Rotis:", each_item)

```

*Files: `Loops.md`, `Loops.py*`

### The `range()` Function

Generates a sequence of integers: `range(start, stop, step)`.

* **`start`**: First integer in the sequence (defaults to `0`).
* **`stop`**: The ceiling boundary (always non-inclusive).
* **`step`**: The increment/decrement amount between values (defaults to `1`).

```python
# Range stepping by 10
for item in range(2, 21, 10):
    print(item)  # Prints: 2, 12

# Range stepping by 2 (Even numbers 0 to 20)
for item in range(0, 21, 2):
    print(item)

```

*Files: `Loops.py`, `Practice .py*`

---

## 4. Loop Control Statements

Alter default loop execution behavior dynamically.

### `break` Statement

Terminates the active loop immediately when encountered.

```python
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# Output: 1, 2, 3, 4

```

*Files: `Loops.md`, `Loops.py*`

### `continue` Statement

Skips the rest of the current iteration and jumps directly to the next loop cycle.

```python
# Skip printing the number 7
for i in range(1, 11):
    if i == 7:
        continue
    print(i)

```

*File: `Practice .py*`

### `pass` Statement

Acts as a syntactic placeholder when a code block requires an empty statement.

```python
for i in range(1, 2):
    pass

```

*Files: `Loops.md`, `Loops.py*`

---

## 5. Nested Loops

A loop defined inside another loop. The inner loop executes all its cycles for every single iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

```

*File: `Loops.md*`

---

## 6. Mini Projects

### Countdown Timer

Uses the `time` module alongside a descending `range()` to step through seconds:

```python
import time

count = int(input("Enter the no. of counter: "))
print("\nCountdown Start Now:")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("\nWOHOO! Happy New Year")

```

*File: `Mini Project.py*`

### Multiplication Tables

Generates custom tables based on user input:

```python
# Using a for loop
n = int(input("Enter the no.:: "))
for i in range(1, 11):
    print(i, "*", n, "=", i * n)

```

*Files: `Practice .py`, `Mini Project.py*`

---

## 7. Practice Problems

* **Print Numbers 10 down to 1 (`while`):**
```python
num = 10
while num >= 1:
    print(num)
    num -= 1

```


* **Dynamic Triangle Patterns:**
```python
n = int(input("Enter the number: "))
s = input("Enter the symbol: ")
i = 1
while i <= n:
    print(s * i)
    i += 1

```


* **Descending Range (Reverse Countdown):**
```python
for item in range(100, 0, -1):
    print(item)

```



---

## 📂 File Directory

* `Loops.md`: Markdown reference notes covering `while` loops, `for` loops, `range()` parameters, control statements, and nested loops.
* `Loops.py`: Working demonstrations of `while` counters, list/tuple iterations, stepped ranges, `break`, and `pass`.
* `Mini Project.py`: Countdown timer using `time.sleep()`.
* `Practice .py`: Practice exercises covering odd/even filters, descending loops, geometric pattern rendering, multiplication tables, and `continue` skips.


