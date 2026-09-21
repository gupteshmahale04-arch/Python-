
# 📁 Python Fundamentals: File Handling & Operations

A structured guide and practice workspace covering file operations, open modes, context managers (`with`), reading line-by-line, file modification tasks, and hands-on coding exercises[cite: 67, 68, 69].

---

## 📋 Table of Contents
* [1. Introduction to File Handling](#1-introduction-to-file-handling)
  * [Real-World Use Cases](#real-world-use-cases)
  * [Text Files vs. Binary Files](#text-files-vs-binary-files)
* [2. Opening Modes & Syntax](#2-opening-modes--syntax)
* [3. Reading Files](#3-reading-files)
  * [Basic open() and close()](#basic-open-and-close)
  * [The with Context Manager](#the-with-context-manager)
  * [read(), readline(), and readlines()](#read-readline-and-readlines)
* [4. Writing & Creating Files](#4-writing--creating-files)
  * [Overwriting ("w") vs. Exclusive Creation ("x")](#overwriting-w-vs-exclusive-creation-x)
* [5. Automating File Tasks (os & shutil)](#5-automating-file-tasks-os--shutil)
* [6. Practice Exercises & Solutions](#6-practice-exercises--solutions)
  * [Search for a Target Word in a File](#search-for-a-target-word-in-a-file)
  * [Line Count Analyzer](#line-count-analyzer)
* [📂 File Directory](#-file-directory)

---

## 1. Introduction to File Handling

File handling allows Python programs to create, read, update, and manage persistent data saved on a computer's disk[cite: 67].

### Real-World Use Cases[cite: 67]
* Saving application and login event logs[cite: 67].
* Storing student databases and administrative records[cite: 67].
* Reading software configuration files[cite: 67].
* Exporting analytics and summary spreadsheets as CSV files[cite: 67].

### Text Files vs. Binary Files[cite: 67]

| File Type | Description | Common Extensions | Example |
| :--- | :--- | :--- | :--- |
| **Text Files** | Human-readable content encoded as text characters[cite: 67]. | `.txt`, `.csv`, `.log`[cite: 67] | `notes.txt` storing study notes[cite: 67]. |
| **Binary Files** | Data stored in raw, encoded byte format[cite: 67]. | `.png`, `.jpg`, `.pdf`, `.mp4`, `.exe`[cite: 67] | `profile.jpg` holding an image[cite: 67]. |

---

## 2. Opening Modes & Syntax

Files are initialized using the built-in `open()` function[cite: 67]:

```python
file = open("filename", "mode")

```

### Common File Access Modes



| Mode | Purpose & Behavior |
| --- | --- |
| **`"r"`** | **Read (Default):** Opens an existing file for reading; raises `FileNotFoundError` if missing.

 |
| **`"w"`** | **Write:** Opens a file for writing; creates it if missing, or overwrites existing data.

 |
| **`"a"`** | **Append:** Opens for writing; appends new content to the end without overwriting.

 |
| **`"x"`** | **Exclusive Creation:** Creates a new file; raises an error if the file already exists.

 |
| **`"t"`** | **Text Mode (Default):** Handles data as string characters.

 |
| **`"b"`** | **Binary Mode:** Handles raw data bytes (images, audio, PDFs).

 |

---

## 3. Reading Files

### Basic `open()` and `close()`

Files opened manually must be explicitly closed using `.close()` to free allocated memory and system handles.

```python
file = open("First.py", "r")
data = file.read()
print("Data of the file is: ", data)
file.close()

```

*Files: `File Handling.md`, `File Handling.py*`

### The `with` Context Manager

The `with` statement is the best practice approach because it automatically closes the file upon leaving the block, even if runtime errors occur.

```python
with open("First.py", "r") as f:
    data = f.read()
    print("File Data:", data)

```

*Files: `File Handling.md`, `File Handling.py*`

### `read()`, `readline()`, and `readlines()`

* **`.read()`:** Reads the entire contents of the file as a single continuous string.


* **`.readline()`:** Reads a single line ending at the nearest newline character (`\n`).


* **`.readlines()`:** Reads all lines and returns them collected into a list of strings.



```python
# 1. Read line-by-line
with open("First.py", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("Line 1:", line1)
    print("Line 2:", line2)

# 2. Read all lines into a list
with open("First.py", "r") as f:
    lines = f.readlines()
    print("All Lines as List:", lines)
    print("Total line count:", len(lines))

```

*Files: `File Handling.py`, `Practice.py*`

---

## 4. Writing & Creating Files

### Overwriting (`"w"`) vs. Exclusive Creation (`"x"`)

* `"w"` opens the file and wipes existing content before writing.


* `"x"` creates a new file safely, preventing accidental overwrites of existing files.



```python
# Write mode (overwrites/creates)
file_w = open("First2.py", "w")
file_w.write("Chapter 9 hi")
file_w.close()

# Exclusive creation mode (fails if file already exists)
file_x = open("saumya_info.txt", "x")
file_x.write("Chapter 9 hi")
file_x.close()

```

*File: `Practice.py*`

---

## 5. Automating File Tasks (`os` & `shutil`)

External standard library modules provide tools for administrative file operations without rewriting custom algorithms:

```python
import os
import shutil

# Copying a file from source to backup destination
shutil.copy("demo.txt", "backup_demo.txt")

# Renaming an existing file
os.rename("old_name.txt", "new_name.txt")

# Removing/deleting a file
os.remove("unwanted_file.txt")

```

*File: `File Handling.md*`

---

## 6. Practice Exercises & Solutions

### Search for a Target Word in a File

Opens a file dynamically, normalizes character casing, and evaluates membership checks:

```python
file_name = input("Enter the name of file: ")
target_word = input("Enter the search word: ").lower()

with open(file_name, "r") as f:
    content = f.read().lower()

if target_word in content:
    print(f"Yes, '{target_word}' is in the file.")
else:
    print(f"No, '{target_word}' is not in the file.")

```

*File: `Practice.py*`

### Line Count Analyzer

Reads document lines as a list sequence and prints the total number of lines present:

```python
with open("First.py", "r") as f:
    lines = f.readlines()
    print("Total lines present:", len(lines))

```

*File: `Practice.py*`

---

## 📂 File Directory

* `File Handling.md`: Notes outlining file concepts, text vs. binary types, access modes, context managers, and automation modules.


* `File Handling.py`: Code examples testing `.read()`, line-by-line `.readline()` calls, and list output via `.readlines()`.


* `Practice.py`: Coding exercises demonstrating word search algorithms, write modes (`"w"`, `"x"`), first-line readers, and line counters.




