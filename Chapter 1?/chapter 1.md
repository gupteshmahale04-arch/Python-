
# 🐍 Python Basics: Variables, Memory, and Execution

A foundational guide and code repository covering basic Python execution, user inputs, variable memory models, expressions, statements, comments, indentation, and practice scripts[cite: 48, 49, 50, 51].

---

## 📋 Table of Contents
* [1. Code Execution Flow](#1-code-execution-flow)
* [2. Variables & Memory Concepts](#2-variables--memory-concepts)
  * [Naming Rules](#naming-rules)
  * [Memory Reference & id()](#memory-reference--id)
* [3. Taking User Input](#3-taking-user-input)
* [4. Expressions vs. Statements](#4-expressions-vs-statements)
* [5. Comments in Python](#5-comments-in-python)
* [6. Indentation](#6-indentation)
* [7. Practice Assignment: Circle Calculation](#7-practice-assignment-circle-calculation)
* [📂 File Directory](#-file-directory)

---

## 1. Code Execution Flow

Python executes programs sequentially, line by line, from top to bottom[cite: 48].

```python
print("line 01 ")
print("line 02 ")
print("line 03 ")
print("line 04 ")
print("line 05 ")
print("line 06 ")

```

*File: `Code Execution .py*`



## 2. Variables & Memory Concepts

* A **variable** is a reserved name/label that stores a value in memory during program execution.


* Python automatically infers the data type based on the assigned value.



```python
x = 10         # Integer type inferred
y = "hello "   # String type inferred

```

### Naming Rules

* A variable name can contain letters, numbers, and underscores (`_`).


* A variable name **cannot** start with a number.


* It cannot be a reserved Python keyword (such as `if`, `for`, `while`, `import`).



| Valid Names | Invalid Names |
| --- | --- |
| `name1`<br> | `123` (starts with a number)

 |
| `AGE`, `aGE`<br> | `test!` (contains special character `!`)

 |
| `a111111`<br> | `name%` (contains special character `%`)

 |
| `my_name`, `__name`<br> | `for`, `while` (reserved keywords)

 |

### Memory Reference & `id()`

Variables are labels pointing to objects in memory. Use `id()` to inspect an object's memory address:

```python
x = 10
print(id(x))

```

---

## 3. Taking User Input

* The `input()` function captures user input as a string.


* Convert the input using type casting (e.g., `int()`) when performing numerical calculations.



```python
print(" Enter Your Good Information ")
name = input("Enter Your Name :")
age = int(input('Enter Your Age :'))
print(name, age)

```

*File: `Input by User.py*`

---

## 4. Expressions vs. Statements

* **Expression:** A combination of operands and operators that evaluates to a value.


* `x + 3` $\rightarrow$ Expression with two operands (`x`, `3`) and one operator (`+`).




* **Statement:** An instruction or action performed on a value.


* `name = "ram"` $\rightarrow$ Assignment statement.


* `print(name)` $\rightarrow$ Output statement.




* Multiple statements can be written on a single line separated by a semicolon (`;`):


```python
name = "ram "; print(name)

```



---

## 5. Comments in Python

* Text following a hash symbol (`#`) is ignored by the interpreter.


* Comments explain the logic and flow of code for developers.


* **Shortcut:** `Ctrl + /` toggles single-line comments in most editors.



```python
# This is an addition code of two numbers
a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
print("Addition is:", a + b)

```

---

## 6. Indentation

* Indentation in Python defines code blocks (functions, loops, conditional branches, or classes).


* Unlike languages using braces `{ }`, Python requires consistent indentation and disallows arbitrary spaces before statements:



```python
# ❌ Incorrect (causes IndentationError)
name = "guptesh"
    print(name)

#  Correct
name = "guptesh"
print(name)

```

---

## 7. Practice Assignment: Circle Calculation

A simple program that accepts user input to compute circle measurements:

```python
# Area of a circle practice script
D = int(input("Enter the Diameter :"))
print("Diameter is :", D)
area = 2 * 3.12 * D
print(" Area of a circule :", area)

```

*Files: `NOV&MC.md`, `tempCodeRunnerFile.py*`

---

## 📂 File Directory

* `Code Execution .py`: Script illustrating sequential line-by-line execution.


* `Input by User.py`: Example demonstrating user input collection and type conversion.


* `NOV&MC.md`: Comprehensive notes covering variables, expressions, memory locations, comments, and indentation.


* `tempCodeRunnerFile.py`: Working draft code for user input calculations.



```

```
