
# 🐍 Python Fundamentals: Conditional Statements, Lists, and Tuples

A comprehensive guide and reference workspace covering Python decision-making (`if-elif-else`), ordered mutable collections (`list`), ordered immutable collections (`tuple`), looping routines, and practice assignments.

---

## 📋 Table of Contents
* [1. Conditional Statements (Decision Making)](#1-conditional-statements-decision-making)
  * [Condition Fundamentals](#condition-fundamentals)
  * [if, if-else, and if-elif-else Hierarchies](#if-if-else-and-if-elif-else-hierarchies)
* [2. Python Lists (Mutable Sequences)](#2-python-lists-mutable-sequences)
  * [List Indexing & Slicing](#list-indexing--slicing)
  * [List Methods & Built-in Functions](#list-methods--built-in-functions)
* [3. Python Tuples (Immutable Sequences)](#3-python-tuples-immutable-sequences)
  * [Tuple Immutability & Methods](#tuple-immutability--methods)
  * [Single-Element Tuple Declaration](#single-element-tuple-declaration)
* [4. While Loop Control Flow](#4-while-loop-control-flow)
* [5. Practice Exercises & Assignments](#5-practice-exercises--assignments)
  * [Number Sign Identifier (Positive / Zero / Negative)](#number-sign-identifier-positive--zero--negative)
  * [Movie and Food Collectors](#movie-and-food-collectors)
  * [Marks Evaluation & Grading](#marks-evaluation--grading)
* [📂 Repository File Breakdown](#-repository-file-breakdown)

---

## 1. Conditional Statements (Decision Making)

Conditional statements control program flow by evaluating boolean expressions to either `True` or `False`.

### Condition Fundamentals
A condition performs comparison checks on variables and expressions:

```python
age = 18
print(age == 18)  # Returns True

```

### `if`, `if-else`, and `if-elif-else` Hierarchies

* **`if` Statement:** Runs an indented code block only if its condition evaluates to `True`.

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")

```

* **`if-else` Statement:** Provides a fallback execution path when the condition evaluates to `False`.

```python
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("You passed!")
else:
    print("You failed")

```

* **`if-elif-else` Statement:** Chains multiple alternative criteria sequentially.

```python
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

```

*Files: `Conditional Stetment.md`, `Conditionnal Stetment.py*`

---

## 2. Python Lists (Mutable Sequences)

A **list** is an ordered, mutable collection capable of holding items of heterogeneous data types.

```python
marks = [87, 64, 68, 67, 89]
foods = ["Samosa", "Pizza", "Burger"]
student = ["guptesh mahale", 18, "betul"]

```

### List Indexing & Slicing

Lists are zero-indexed, meaning elements start at index position `0`. Slices are extracted using `list[start:end]`, where the `end` index is non-inclusive.

```python
foods = ["Samosa", "Pizza", "Burger"]
print(foods[0])  # 'Samosa'
print(foods[2])  # 'Burger'

# In-place item modification (Mutability)
foods[0] = "GulabJamun"
print(foods)     # ['GulabJamun', 'Pizza', 'Burger']

# Slicing ranges
marks = [87, 64, 33, 95, 76]
print(marks[1:4])   # [64, 33, 95]
print(marks[:3])    # [87, 64, 33]
print(marks[-3:-1]) # [33, 95]

```

*File: `Conditional Stetment.md*`

### List Methods & Built-in Functions

| Function / Method | Action Performed | Syntax Example |
| --- | --- | --- |
| `len(list)` | Returns total item count | `len(marks)` $\rightarrow$ `5` |
| `max(list)` | Extracts the highest value | `max(marks)` $\rightarrow$ `95` |
| `min(list)` | Extracts the lowest value | `min(marks)` $\rightarrow$ `33` |
| `.append(el)` | Adds an element to the end of the list | `marks.append(99)` |
| `.insert(i, el)` | Inserts an element at index position `i` | `marks.insert(1, 80)` |
| `.remove(el)` | Removes the first occurrence of an element | `marks.remove(64)` |
| `.pop(i)` | Extracts and removes the item at index `i` | `marks.pop(2)` |
| `.sort()` | Sorts items in ascending order in place | `marks.sort()` |
| `.reverse()` | Inverts the sequence of elements in place | `marks.reverse()` |

---

## 3. Python Tuples (Immutable Sequences)

A **tuple** is an ordered collection that stores multiple items like a list, but cannot be modified, updated, or re-assigned after instantiation.

```python
tup = (87, 64, 33, 95, 76)
print(tup[0])  # Output: 87

# ❌ Mutating raises a TypeError:
# tup[2] = 9   # TypeError: 'tuple' object does not support item assignment

```

*Files: `Conditional Stetment.md`, `Tuples.py*`

### Tuple Immutability & Methods

* `.count(value)`: Counts how many times a value appears.
* `.index(value)`: Returns the first index where the value is found.

```python
roll = (1, 2, 3, 4, 4, 5, 6)
print(roll.count(4))  # 2
print(roll.index(4))  # 3
print(len(roll))      # 7

```

*File: `Tuples.py*`

### Single-Element Tuple Declaration

A single item enclosed in parentheses without a trailing comma is evaluated as a standard string or integer primitive, not a tuple.

```python
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

not_a_tuple = ("ram")
print(type(not_a_tuple))  # <class 'str'>

is_a_tuple = ("ram",)
print(type(is_a_tuple))   # <class 'tuple'>

```

*File: `Tuples.py*`

---

## 4. While Loop Control Flow

A `while` loop iterates continuously as long as its target condition evaluates to `True`.

```python
num = int(input("Enter The Number ::"))
num1 = 1

while num1 <= num:
    if num1 % 2 == 0:
        print("Number is Even", num1)
    num1 = num1 + 1

```

*File: `tempCodeRunnerFile_3.py*`

---

## 5. Practice Exercises & Assignments

### Number Sign Identifier (Positive / Zero / Negative)

Categorizes real numbers across boundary ranges:

```python
num = int(input("Enter the Number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

```

*File: `Prectice_2.py*`

### Movie and Food Collectors

Stores user input dynamically using list literal declarations and the `.append()` method:

```python
# Favorite movie collection list
FM1 = input("Enter 1st favorite movie: ")
FM2 = input("Enter 2nd favorite movie: ")
FM3 = input("Enter 3rd favorite movie: ")

movies = [FM1, FM2, FM3]
print("Favorite Movies:", movies)

```

*Files: `Assignment_3.py`, `Prectice_2.py*`

### Marks Evaluation & Grading

Finds extreme boundaries in tuple structures and assigns grade status:

```python
marks = (87, 64, 33, 95, 76)

print("Highest Mark:", max(marks))  # 95
print("Lowest Mark:", min(marks))   # 33

```

*File: `Assignment_3.py*`

---

## 📂 Repository File Breakdown

* `Assignment_3.py`: Implementation scripts for movie list storage, tuple min/max evaluations, and conditional grading.
* `Conditional Stetment.md`: Markdown reference covering boolean conditions, `if-elif-else` constructs, list operations, indexing, and tuple characteristics.
* `Conditionnal Stetment.py`: Script executing conditional statements and grade evaluations.
* `lists.py`: Demonstrations of list slicing, mutability, `len()`, `append()`, and `.sort()` operations.
* `Prectice_2.py`: Practice solutions for number classification, food list collections, and fruit tuple index inspections.
* `tempCodeRunnerFile_3.py`: Working draft code demonstrating counter loops and even number checks via a `while` loop.
* `Tuples.py`: Examples showing tuple indexing, immutability constraints, `.count()`, `.index()`, and single-element tuple syntax.

