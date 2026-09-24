
# 🐍 Python Mastery: From Fundamentals to Object-Oriented Programming & Practical Projects

Welcome to the central repository for **Python Learning and Development**. This repository documents an end-to-end learning journey through core Python programming, data structures, functional paradigms, object-oriented software engineering, file handling, and full interactive projects.

---

## 📋 Table of Contents
* [Repository Overview](#-repository-overview)
* [Curriculum & Module Roadmap](#-curriculum--module-roadmap)
  * [1. Fundamentals, Memory & Execution Flow](#1-fundamentals-memory--execution-flow)
  * [2. Data Types, Operators & Type Casting](#2-data-types-operators--type-casting)
  * [3. Strings, Slicing & Built-in Methods](#3-strings-slicing--built-in-methods)
  * [4. Control Flow, Lists & Tuples](#4-control-flow-lists--tuples)
  * [5. Dictionaries & Sets](#5-dictionaries--sets)
  * [6. Iterations & Loops](#6-iterations--loops)
  * [7. Modular Functions & Scope](#7-modular-functions--scope)
  * [8. File Handling & System Operations](#8-file-handling--system-operations)
  * [9. Object-Oriented Programming (OOP)](#9-object-oriented-programming-oop)
* [Highlighted Projects](#-highlighted-projects)
  * [🎨 Image Filter Studio & CLI Explorer](#-image-filter-studio--cli-explorer)
  * [🧩 Sudoku Master (Terminal & Web App)](#-sudoku-master-terminal--web-app)
  * [🏫 School Admission Portal](#-school-admission-portal)
  * [😊 Emoji Emotion Converter](#-emoji-emotion-converter)
* [Installation & Workspace Setup](#-installation--workspace-setup)
* [Repository Structure](#-repository-structure)

---

## 🔍 Repository Overview
This repository serves as a structured repository of hands-on practice, assignments, comprehensive markdown notes, and deployable applications. It traces the progression from baseline command execution to intermediate data structures, object-oriented system design, and graphical/web application development with Streamlit.

---

## 🗺️ Curriculum & Module Roadmap

### 1. Fundamentals, Memory & Execution Flow
* **Sequential Execution:** Understanding line-by-line script processing.
* **Variable References & Memory:** Variables as labels referencing memory objects, verified via `id()`.
* **Input & Syntactic Rules:** Interactive prompts with `input()`, indentation blocks, single-line multiple statements (`;`), and comment conventions (`#`).

### 2. Data Types, Operators & Type Casting
* **Primitives:** Numeric forms (`int`, `float`), textual strings (`str`), and truth values (`bool`).
* **Operator Families:** Arithmetic (`+`, `-`, `*`, `/`, `%`, `**`), comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), logical (`and`, `or`, `not`), and identity (`is`).
* **Casting Mechanisms:** Implicit promotion (automatic float widening) and explicit casting (`int()`, `float()`, `str()`, `bool()`).

### 3. Strings, Slicing & Built-in Methods
* **Immutability:** Structural permanence of string data in memory.
* **Bi-directional Indexing & Slices:** Forward (`0` to `n-1`) and negative (`-1` to `-n`) offsets with `[start:end]` substring extraction.
* **String Methods:** Text transformations including `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.replace()`, `.find()`, and `.count()`.
* **String Formatting:** String interpolation using f-strings and escape sequences (`\n`, `\t`).

### 4. Control Flow, Lists & Tuples
* **Conditional Logic:** Multi-branch decisions using `if`, `elif`, and `else`.
* **Lists (Mutable Collections):** Item indexing, in-place element assignment, slicing, and methods (`.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`).
* **Tuples (Immutable Sequences):** Fixed tuple structures, single-element tuple syntax `(item,)`, and methods (`.count()`, `.index()`).

### 5. Dictionaries & Sets
* **Dictionaries (Key-Value Mappings):** Unique hashable keys, nested mappings, record updates, and dictionary utilities (`.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`).
* **Sets (Unique Collections):** Deduplication mechanisms, element addition/removal (`.add()`, `.remove()`), and set mathematics (`.union()`, `.intersection()`).

### 6. Iterations & Loops
* **Loop Paradigms:** Condition-controlled `while` loops and sequence iteration with `for`.
* **The `range()` Utility:** Stepped integer generation (`start`, `stop`, `step`).
* **Control Jump Statements:** Early termination with `break`, cycle skipping with `continue`, and block placeholders with `pass`.

### 7. Modular Functions & Scope
* **Function Architecture:** Modularization with `def`, argument passing, and output handling via `return`.
* **Argument Modifiers:** Positional, default fallback parameters, and explicit keyword arguments.
* **Variable Scope:** Distinguishing local function scopes from global execution namespaces.

### 8. File Handling & System Operations
* **Open Modes:** Read (`"r"`), write (`"w"`), append (`"a"`), exclusive create (`"x"`), text (`"t"`), and binary (`"b"`).
* **Context Management:** Safe file workflows with automatic file closing via `with open(...)`.
* **File Processing:** Whole content reading (`.read()`), single-line traversal (`.readline()`), and collection reads (`.readlines()`).

### 9. Object-Oriented Programming (OOP)
* **Foundational OOP:** Classes as blueprints, instantiated objects, constructor initialization (`__init__`), and the instance pointer `self`.
* **Inheritance Models:** Practical patterns covering Single, Multilevel, Multiple, and Hierarchical class structures.
* **Encapsulation:** Public attributes, protected notations (`_`), and private variable name mangling (`__`).
* **Polymorphism & Methods:** Method overriding via `super()`, method overloading techniques, class methods (`@classmethod`), and static methods (`@staticmethod`).
* **Dunder Methods & Abstraction:** Operator overloading (`__str__`, `__add__`, `__eq__`) and Abstract Base Classes using `abc.ABC` and `@abstractmethod`.

---

## 🚀 Highlighted Projects

### 🎨 Image Filter Studio & CLI Explorer
* An image processing tool built with **NumPy**, **Matplotlib**, **Pillow**, and **Streamlit**.
* Implements channel separation (R, G, B) and luminosity grayscale conversion ($0.2989R + 0.5870G + 0.1140B$).
* Provides both a terminal CLI and an interactive web app to preview and download Matplotlib colormaps applied to images.

### 🧩 Sudoku Master (Terminal & Web App)
* A dual-interface puzzle platform using **NumPy**, **Tabulate**, and **Streamlit**.
* Features a terminal validator that computes row/column sums and an embedded dark-themed web game with real-time conflict highlights, pencil notation, a timer, and a recursive backtracking solver.

### 🏫 School Admission Portal
* An interactive Python script applying hierarchical class inheritance to validate student admissions against class-specific age limits for 10th and 12th grades.

### 😊 Emoji Emotion Converter
* A clean text-processing utility that replaces common ASCII emoticons (`:)`, `:(`, `:D`, `<3`) with visual Unicode emojis.

---

## 💻 Installation & Workspace Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gupteshmahale04-arch/Python-.git](https://github.com/gupteshmahale04-arch/Python-.git)
   cd Python-

```

2. **Set up a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install project dependencies:**
```bash
pip install streamlit matplotlib numpy Pillow tabulate

```


4. **Launch interactive applications:**
* **Sudoku Web App:**
```bash
streamlit run app.py

```


* **Image Filter Studio:**
```bash
streamlit run "app (2).py"

```





---

## 📂 Repository Structure

```plaintext
Python-/
├── 01_Basics_and_Variables/
│   ├── Code Execution .py          # Sequential flow demonstration
│   ├── Input by User.py            # User inputs and basic type casting
│   ├── NOV&MC.md                   # Notes on variables, memory, and indentation
│   └── tempCodeRunnerFile.py       # Circle geometry calculations
│
├── 02_DataTypes_and_Operators/
│   ├── Assignment.py               # Temperature & bill split calculators
│   ├── Data Types .py              # Type verification with type()
│   ├── DT&O.md                     # Notes on keywords, casting, and operators
│   ├── KeyWords.py                 # Keyword inspection utility
│   ├── Operators  .py              # Arithmetic, comparison, and logical checks
│   ├── Prectice.py                 # Mathematical and comparison challenges
│   └── Type Conversion.py          # Implicit and explicit type conversion
│
├── 03_Strings_and_Text_Processing/
│   ├── Assignment_2.py             # String analysis and character extraction tasks
│   ├── mini project .py            # Emoji converter utility
│   ├── Practice Q.py               # String methods, casing, and index extraction
│   ├── Strings .py                 # Slicing, negative indices, and escape sequences
│   └── Strings.md                  # Reference notes on string methods and immutability
│
├── 04_Conditionals_Lists_and_Tuples/
│   ├── Assignment_3.py             # Movie list storage and grading logic
│   ├── Conditional Stetment.md     # Reference notes on conditionals, lists, and tuples
│   ├── Conditionnal Stetment.py    # Grade calculation using if-elif-else
│   ├── Lists ,py                   # List mutability, methods, and slicing
│   ├── Prectice_2.py               # Number sign classifier and sequence challenges
│   └── Tuples.py                   # Tuple methods and single-element declarations
│
├── 05_Dictionaries_and_Sets/
│   ├── Assignmennt.py              # Dictionary tasks and set collision exercises
│   ├── Dictionary  .py             # Dictionary modification, keys, and values
│   ├── Dictionary & Sets.md        # Reference notes on dict/set operations
│   ├── Prectice_3.py               # Subject dictionaries and list deduplication
│   ├── School Project.py           # Multi-record student lookup dictionary
│   └── Sets.py                     # Set operations, mutations, and properties
│
├── 06_Loops_and_Iterations/
│   ├── Loops.md                    # Reference notes on while/for loops and range()
│   ├── Loops.py                    # Sequence traversal, ranges, and break/pass
│   ├── Mini Project.py             # Countdown timer with time.sleep()
│   └── Practice .py                # Multiplication tables and pattern printing
│
├── 07_Functions_and_Modularity/
│   ├── Function.md                 # Notes on parameters, returns, and variable scope
│   ├── Function.py                 # Default values and mathematical functions
│   ├── Prectice_4.py               # Vowel/consonant counters and utility functions
│   └── Return Statement.py         # Demonstrations of function return values
│
├── 08_File_Handling/
│   ├── File Handling.md            # Notes on file modes and context managers
│   ├── File Handling.py            # Whole file and line-by-line reading methods
│   └── Practice.py                 # Word search in files and line counting
│
├── 09_Object_Oriented_Programming/
│   ├── Abstraction.py              # Abstract classes and dunder operator overloading
│   ├── Demo.py                     # Constructor chaining with super()
│   ├── Inceptuletion.py            # Access modifiers: public, protected, and private
│   ├── Inheritance.py              # Single, Multiple, Multilevel, and Hierarchical models
│   ├── OOP Project.py              # School admission evaluation system
│   ├── OOP.py                      # Classes, instance methods, and static methods
│   ├── poiymorphism.py             # Method overriding and parameter handling
│   ├── inheritance_assignment_1.ipynb  # Basic inheritance practice notebook
│   ├── Inheritance_assignment_2.ipynb  # Intermediate inheritance notebook
│   └── Inheritance_assignment_3.ipynb  # Advanced inheritance notebook
│
├── 10_Applications_and_Projects/
│   ├── app (2).py                  # Image Filter Studio (Streamlit app)
│   ├── Img_project.py              # Image Filter Studio (CLI version)
│   ├── app.py                      # Sudoku Master (Interactive Streamlit app)
│   ├── main.py                     # Sudoku Terminal Solver & Validator
│   └── requirements.txt            # Project dependencies list
│
└── README.md                       # Repository master documentation

```

```

```
