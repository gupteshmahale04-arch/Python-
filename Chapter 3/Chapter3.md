
# 🐍 Python Chapter 3: Strings, Slicing & String Methods

A structured repository containing reference notes, practical scripts, practice questions, assignments, and a mini emoji converter project focused on Python strings.

---

## 📋 Table of Contents
* [1. String Fundamentals & Creation](#1-string-fundamentals--creation)
* [2. String Immutability](#2-string-immutability)
* [3. String Indexing & Slicing](#3-string-indexing--slicing)
  * [Positive Indexing](#positive-indexing)
  * [Negative Indexing](#negative-indexing)
  * [Slicing Windows](#slicing-windows)
* [4. Common String Methods](#4-common-string-methods)
* [5. Formatted Strings (f-Strings) & Escape Characters](#5-formatted-strings-f-strings--escape-characters)
* [6. String Operations & Properties](#6-string-operations--properties)
* [7. Mini Project: Emoji Converter](#7-mini-project-emoji-converter)
* [8. Practice & Assignment Tasks](#8-practice--assignment-tasks)
* [📂 File Directory](#-file-directory)

---

## 1. String Fundamentals & Creation

A string is a standard Python data type representing a sequence of characters (letters, numbers, or symbols) enclosed in single (`'`), double (`"`), or triple (`'''` / `"""`) quotes.

```python
str1 = 'Hello'
str2 = "guptesh"
str3 = '''this is guptesh, it is like patodi'''
print(str1, str2, str3)

```

*Files: `Strings .py`, `Strings.md*`

---

## 2. String Immutability

Strings in Python are **immutable**, meaning once created, individual characters cannot be modified or replaced in place:

```python
name = "guptesh"
# ❌ Attempting to mutate throws an error:
# name[0] = "r"  # TypeError: 'str' object does not support item assignment

```

---

## 3. String Indexing & Slicing

### Positive Indexing

Indexing starts from `0` at the beginning of the string:

```python
Str = "guptesh"
print(Str[0])  # 'g'
print(Str[5])  # 's'

```

*Files: `Strings .py`, `Strings.md*`

### Negative Indexing

Negative indices count backwards starting from `-1` at the end:

| Character | G | u | l | a | b | J | a | m | u | n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Index** | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
str__ = "GulabJamun"
print(str__[-5:-1])  # Output: Jamu

```

*Files: `Strings .py`, `Strings.md*`

### Slicing Windows

Extract substrings using the syntax `string[start:end]` (where the `end` index is excluded):

```python
food = "GulabJamun"
print(food[0:5])  # "Gulab"
print(food[:6])   # "GulabJ"
print(food[5:])   # "Jamun"

```

*Files: `Strings .py`, `Strings.md*`

---

## 4. Common String Methods

Built-in methods provide formatting, search, and replacement transformations:

| Method | Description | Example |
| --- | --- | --- |
| `.upper()` | Converts all characters to uppercase | `"samosa".upper()` $\rightarrow$ `'SAMOSA'` |
| `.lower()` | Converts all characters to lowercase | `"Saumya".lower()` $\rightarrow$ `'saumya'` |
| `.title()` | Capitalizes the first letter of each word | `"hello world".title()` $\rightarrow$ `'Hello World'` |
| `.capitalize()` | Capitalizes only the first character | `"python".capitalize()` $\rightarrow$ `'Python'` |
| `.find(sub)` | Returns the lowest index of the substring | `"banana".find("na")` $\rightarrow$ `2` |
| `.count(sub)` | Counts occurrences of a substring | `"mango".count("a")` $\rightarrow$ `1` |
| `.replace(old, new)` | Substitutes all target occurrences | `"Python is cool".replace("cool", "awesome")` |
| `.endswith(suffix)` | Verifies if string ends with suffix | `"coder.".endswith(".")` $\rightarrow$ `True` |

---

## 5. Formatted Strings (f-Strings) & Escape Characters

### f-Strings

Embed variables and expressions cleanly into output text:

```python
name = "Saumya Singh"
age = 21
print(f"My name is {name} and I am {age} years old.")

```

*File: `Strings.md*`

### Escape Sequences

Control characters for whitespace and punctuation formatting:

* `\n` : Line feed (new line)
* `\t` : Horizontal tab
* `\\` : Backslash
* `\'` : Single quote
* `\"` : Double quote

```python
print("Hello\nWorld")  # Two lines
print("Hello\tWorld")  # Tab spaced

```

*Files: `Strings .py`, `Strings.md*`

---

## 6. String Operations & Properties

* **Concatenation (`+`):** Merges strings together (`"Hello " + "World"` $\rightarrow$ `'Hello World'`).
* **Repetition (`*`):** Duplicates a string multiple times (`"Yum! " * 3`).
* **Membership (`in`):** Checks for existence (`"lo" in "Hello"` $\rightarrow$ `True`).
* **Length (`len()`):** Returns total character count (`len("GulabJamun")` $\rightarrow$ `10`).

---

## 7. Mini Project: Emoji Converter

A beginner-friendly script converting text emoticons into visual emojis using sequential `.replace()` calls:

```python
msg = input("Enter your message: ")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😢")
msg = msg.replace(":D", "😃")
msg = msg.replace("<3", "❤️")

print(msg)

```

*Files: `mini project .py`, `Strings.md*`

---

## 8. Practice & Assignment Tasks

### Character Extraction & Length

Accepts user input and inspects boundary characters alongside total length:

```python
name = input("Enter your name: ")
print("The first character is:", name[0])
print("The last character is:", name[-1])
print("The total length of the name is:", len(name))

```

*File: `Practice Q.py*`

### Text Slicing & Replacements

Accesses specific slices and applies text transformations:

```python
food = input("Enter your favorite food name: ")
print("The middle characters:", food[2:7])
print("The last characters:", food[-6:-4])

sentence = input("Enter sentence: ")
print("Upper:", sentence.upper())
print("Lower:", sentence.lower())
print("Replaced:", sentence.replace(" ", "_"))

```

*File: `Practice Q.py*`

---

## 📂 File Directory

* `Assignment_2.py`: Assignment specifications for character length, casing, and extraction exercises.
* `mini project .py`: Emoji converter script replacing text emoticons with unicode characters.
* `Practice Q.py`: Practice solutions for index boundaries, middle character slicing, and casing methods.
* `Strings .py`: Code examples for concatenation, indexing, slicing ranges, and escape characters.
* `Strings.md`: Detailed notes covering string definitions, immutability, methods, formatting, and operations.

```

```
