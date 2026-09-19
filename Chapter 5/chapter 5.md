
# 🐍 Python Fundamentals: Dictionaries and Sets

A practical learning guide and code reference covering Python key-value mapping structures (`dict`), unique element collections (`set`), nested data storage, set operations, and mini school database projects.

---

## 📋 Table of Contents
* [1. Dictionaries in Python](#1-dictionaries-in-python)
  * [Key Characteristics](#key-characteristics)
  * [Accessing, Adding & Mutating Values](#accessing-adding--mutating-values)
  * [Common Dictionary Methods](#common-dictionary-methods)
  * [Nested Dictionaries](#nested-dictionaries)
* [2. Sets in Python](#2-sets-in-python)
  * [Key Properties](#key-properties)
  * [Common Set Methods](#common-set-methods)
  * [Mathematical Operations (Union & Intersection)](#mathematical-operations-union--intersection)
* [3. Dictionary vs. Set Comparison](#3-dictionary-vs-set-comparison)
* [4. Practice Exercises & Mini Projects](#4-practice-exercises--mini-projects)
  * [Student Information Storage](#student-information-storage)
  * [School Database with Roll Number Lookup](#school-database-with-roll-number-lookup)
  * [Unique Language Deduplicator](#unique-language-deduplicator)
  * [The Float/Integer Collision in Sets](#the-floatinteger-collision-in-sets)
* [📂 File Directory](#-file-directory)

---

## 1. Dictionaries in Python

A **dictionary** is an unordered, mutable collection that stores data in structured **key-value pairs** using curly braces `{}`.

```python
student = {
    "name": "Saumya Singh",
    "age": 25,
    "city": "Sultanpur"
}

```

*File: `Dictionary & Sets.md*`

### Key Characteristics

* **Unique Keys:** Keys cannot be duplicated; re-assigning an existing key overwrites its current value.
* **Mutable:** Values can be updated, new pairs added, or existing elements removed.
* **Key Restrictions:** Keys must be immutable types (e.g., strings, integers, tuples), whereas values can be any type.

### Accessing, Adding & Mutating Values

```python
# Accessing via key
print(student["name"])    # Output: Saumya Singh

# Adding a new key-value pair
student["year"] = 2007

# Mutating an existing key
student["age"] = 26

```

*Files: `Dictionary  .py`, `Dictionary & Sets.md*`

### Common Dictionary Methods

* `.keys()`: Returns all keys present in the dictionary.
* `.values()`: Returns all values stored across the pairs.
* `.items()`: Returns key-value pairs as tuple elements `(key, value)`.
* `.get(key)`: Safely fetches the value for a key without crashing if the key is missing.
* `.pop(key)`: Removes the specified key and its associated value.
* `.update(new_dict)`: Merges or updates key-value pairs into the dictionary.

```python
info = {"name": "Aman", "roll": "15"}
print(info.keys())    # dict_keys(['name', 'roll'])
print(info.values())  # dict_values(['Aman', '15'])
print(info.items())   # dict_items([('name', 'Aman'), ('roll', '15')])

```

*Files: `Dictionary  .py`, `Dictionary & Sets.md*`

### Nested Dictionaries

Dictionaries can nest inside other dictionaries to represent relational or hierarchical structures:

```python
profile = {
    "username": "saumyasingh",
    "details": {
        "followers": 1200,
        "verified": True
    }
}

```

*File: `Dictionary & Sets.md*`

---

## 2. Sets in Python

A **set** is an unordered collection of unique elements enclosed in curly braces `{}`. Duplicate values are automatically eliminated.

```python
food = {"patoddi", "roti", "chai", "roti"}
print(food)  # Output: {'patoddi', 'chai', 'roti'} -> duplicates removed

```

*File: `Sets.py*`

### Key Properties

* **Unique Elements:** Sets never hold duplicate values.
* **Unordered:** Items have no fixed position; you cannot access elements using indexing like `set[0]`.
* **Mutable:** Items can be added or removed dynamically.
* **Element Requirements:** Elements contained inside a set must be immutable (lists and dictionaries cannot be set elements).

### Common Set Methods

* `.add(element)`: Inserts a single item into the set.
* `.remove(element)`: Deletes an element; raises a `KeyError` if the item is absent.
* `.pop()`: Removes and returns an arbitrary element from the set.
* `.clear()`: Removes all elements, leaving an empty set `set()`.

```python
nums = {1, 2, 3}
nums.add(4)
nums.remove(2)
print(nums)  # Output: {1, 3, 4}

```

*Files: `Dictionary & Sets.md`, `Sets.py*`

### Mathematical Operations (Union & Intersection)

* **`.union(set2)`:** Produces a combined set containing all unique elements from both sets.
* **`.intersection(set2)`:** Produces a set containing only the elements common to both sets.

```python
setA = {1, 2, 3}
setB = {2, 3, 4}

print(setA.union(setB))         # Output: {1, 2, 3, 4}
print(setA.intersection(setB))  # Output: {2, 3}

```

*Files: `Assignmennt.py`, `Dictionary & Sets.md*`

---

## 3. Dictionary vs. Set Comparison

| Feature | 📖 Dictionary | 🧺 Set |
| --- | --- | --- |
| **Structure** | Stores data as key-value pairs | Stores standalone elements |
| **Syntax** | `{"key": value}` | `{value1, value2}` |
| **Duplicates** | Keys must be unique; values can repeat | All elements must be unique |
| **Mutability** | Mutable | Mutable |
| **Indexing** | Accessed via key (`dict["key"]`) | Unindexed (no `set[0]`) |

---

## 4. Practice Exercises & Mini Projects

### Student Information Storage

Accepts student attributes via input and constructs a single dictionary representation:

```python
name = input("Enter student name: ")
roll = input("Enter roll number: ")

student_record = {
    "name": name,
    "roll": roll
}

print(student_record)
print("Keys:", student_record.keys())

```

*File: `Dictionary  .py*`

### School Database with Roll Number Lookup

Stores multiple student records inside a master dictionary keyed by unique roll numbers, allowing immediate lookups:

```python
all_students = {}
num_students = 3

for i in range(num_students):
    roll_no = input("Enter the Roll No: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    all_students[roll_no] = {
        "Name": name,
        "Marks": marks
    }

# Query Database
search_roll = input("Enter Roll No to search: ")
if search_roll in all_students:
    print("Record Found:", all_students[search_roll])
else:
    print("Student not found.")

```

*File: `School Project.py*`

### Unique Language Deduplicator

Transforms a raw sequence containing duplicate entries into a unique set to count individual proficiencies:

```python
languages = ["Python", "Java", "C++", "Python", "Java", "C"]
unique_languages = set(languages)

print("Unique Languages:", unique_languages)
print("Total count:", len(unique_languages))

```

*File: `Prectice_3.py*`

### The Float/Integer Collision in Sets

In Python, boolean and numerical equivalents evaluate to the same hash if their numeric values match (e.g., `9 == 9.0` is `True`). Therefore, adding both `9` and `9.0` keeps only one entry. To retain both, store one as a different type such as a string:

```python
# Values collide because 9 == 9.0 evaluates to True:
numbers = {9, 9.0}
print(numbers)  # Output: {9}

# Solution: Cast one to string to preserve both:
numbers_fixed = {9, "9.0"}
print(numbers_fixed)  # Output: {9, '9.0'}

```

*File: `Assignmennt.py*`

---

## 📂 File Directory

* `Assignmennt.py`: Assignment tasks covering vocabulary dictionaries, set union/intersection, and integer/float set collision handling.
* `Dictionary  .py`: Script taking student metadata inputs, creating dictionaries, modifying keys, and displaying `.items()`.
* `Dictionary & Sets.md`: Comprehensive notes detailing dictionary methods, nested dictionaries, set properties, and structural comparisons.
* `Prectice_3.py`: Practice tasks for building subject mark tables and converting duplicate language lists to sets.
* `School Project.py`: Complete mini application storing multiple student dictionaries within a master database with search functionality.
* `Sets.py`: Code examples testing set uniqueness, `.add()`, `.remove()`, and type verification.


