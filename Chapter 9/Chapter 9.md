
# 🏛️ Python Object-Oriented Programming (OOP): The Complete Architectural Guide

A comprehensive, production-ready reference and code repository covering Python Object-Oriented Programming fundamentals, core inheritance paradigms, access modifiers (encapsulation), polymorphism, dunder methods, abstraction, and real-world project implementations[cite: 73, 75, 76, 77, 80, 81, 82].

---

## 📋 Table of Contents
* [1. Core OOP Paradigms (The Blueprint Analogy)](#1-core-oop-paradigms-the-blueprint-analogy)
* [2. Classes, Objects, and Constructors](#2-classes-objects-and-constructors)
  * [The `__init__()` Constructor & Instance Attributes](#the-__init__-constructor--instance-attributes)
  * [The Role of `self`](#the-role-of-self)
  * [Class Methods vs. Static Methods](#class-methods-vs-static-methods)
* [3. The Four Pillars of OOP](#3-the-four-pillars-of-oop)
  * [Pillar 1: Inheritance](#pillar-1-inheritance)
    * [Single Inheritance](#single-inheritance)
    * [Multiple Inheritance](#multiple-inheritance)
    * [Multilevel Inheritance](#multilevel-inheritance)
    * [Hierarchical Inheritance](#hierarchical-inheritance)
  * [Pillar 2: Encapsulation (Access Modifiers)](#pillar-2-encapsulation-access-modifiers)
  * [Pillar 3: Polymorphism (Overriding vs. Overloading)](#pillar-3-polymorphism-overriding-vs-overloading)
  * [Pillar 4: Abstraction (Abstract Base Classes)](#pillar-4-abstraction-abstract-base-classes)
* [4. Operator Overloading & Dunder Magic Methods](#4-operator-overloading--dunder-magic-methods)
* [5. Real-World Capstone Project: School Admission Portal](#5-real-world-capstone-project-school-admission-portal)
* [📂 Repository File & Assignment Directory](#-repository-file--assignment-directory)

---

## 1. Core OOP Paradigms (The Blueprint Analogy)

* **Procedural/Primitive Approach:** Variables and logic operate in a loose, scattered script (`a = 12; b = 479; print(a + b)`)[cite: 81].
* **Functional Approach:** Encapsulates computations into reusable functions (`def add(a, b): return a + b`)[cite: 81].
* **Object-Oriented Programming (OOP):** Treats code like an **architectural factory**[cite: 81]. 
  * A **Class** is the **Architectural Blueprint** specifying the physical layout (attributes) and behavior (methods)[cite: 81].
  * An **Object (Instance)** is the actual **Physical Building** constructed according to that blueprint[cite: 81]. Each building occupies unique real estate in memory[cite: 73].

---

## 2. Classes, Objects, and Constructors

### The `__init__()` Constructor & Instance Attributes
The `__init__()` method is a special initialization function (known as a **dunder** or double-underscore method) executed automatically the moment an object is instantiated[cite: 78, 81].

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        print(f"Student enrolled: {self.name}, Age: {self.age}")

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Aman", 18)
student1.details()

```

*Files: `OOP.py`, `Demo.py*`

### The Role of `self`

Inside a class, `self` represents the specific instance invoking the method. It passes the calling object's memory address to ensure that actions or variable mutations affect only that specific instance and not other sibling objects.

### Class Methods vs. Static Methods

* **Class Methods (`@classmethod`):** Receive the class itself (`cls`) as their first parameter. Used when modifying class-level attributes that apply globally across all instances.


* **Static Methods (`@staticmethod`):** Independent utility functions grouped inside the class namespace that do not access or depend on `self` or `cls`.



```python
class Animal:
    species = "Canine"  # Class attribute

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species  # Alters class state globally[cite: 81]

class Utility:
    @staticmethod
    def show_menu():
        print("1. Add Record\n2. Exit")  # Executes without object state[cite: 81]

```

*File: `OOP.py*`

---

## 3. The Four Pillars of OOP

### Pillar 1: Inheritance

Inheritance allows a child (derived) class to acquire the properties, attributes, and methods of a parent (base) class, eliminating repetitive code.

#### A. Single Inheritance (1 Parent $\rightarrow$ 1 Child)

A single derived class inherits directly from one base class.

```python
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def show(self):
        print(f"Company: {self.name}, Model: {self.model}")

class Bike(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)  # Delegate setup up to base constructor[cite: 74]

    def display(self):
        print(f"Bike: {self.name} {self.model}")

bike = Bike("Yamaha", "R15")
bike.show()
bike.display()

```

*Files: `Demo.py`, `Inheritance.py`, `Python OOPs Assignment — Inheritance Basics.ipynb*`

#### B. Multiple Inheritance (Multiple Parents $\rightarrow$ 1 Child)

A derived class inherits features simultaneously from two or more parent classes.

```python
class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def greet_father(self):
        print(f"Father: {self.father_name}")

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def greet_mother(self):
        print(f"Mother: {self.mother_name}")

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)  # Explicit base initializations[cite: 76]
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def show(self):
        print(f"Child: {self.child_name}")

c = Child("Rajesh", "Sunita", "Aman")
c.greet_father()
c.greet_mother()
c.show()

```

*Files: `Inheritance.py`, `Python OOPs Assignment Inheritance 2.ipynb*`

#### C. Multilevel Inheritance (Grandparent $\rightarrow$ Parent $\rightarrow$ Child)

Inheritance organized in a vertical linear chain.

```python
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

class Father(Grandfather):
    def __init__(self, grandfather_name, father_name):
        super().__init__(grandfather_name)
        self.father_name = father_name

class Son(Father):
    def __init__(self, grandfather_name, father_name, son_name):
        super().__init__(grandfather_name, father_name)
        self.son_name = son_name

    def show(self):
        print(f"Grandfather: {self.grandfather_name}")
        print(f"Father: {self.father_name}")
        print(f"Son: {self.son_name}")

s = Son("Maruti", "Ambadas", "Deepanshu")
s.show()

```

*Files: `Inheritance.py`, `Python OOPs Assignment Inheritance 2.ipynb*`

#### D. Hierarchical Inheritance (1 Parent $\rightarrow$ Multiple Children)

A single parent class branches out to multiple independent child classes.

```python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def detail(self):
        print(f"Account: {self.name} | Balance: {self.balance}")

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

class Current(Account):
    def __init__(self, name, balance, account_type):
        super().__init__(name, balance)
        self.account_type = account_type

sav = Savings("Rahul", 10000)
curr = Current("Rahul", 50000, "Business")
sav.detail()
curr.detail()

```

*Files: `Inheritance.py`, `Python OOPs Assignment Inheritance 2.ipynb*`

---

### Pillar 2: Encapsulation (Access Modifiers)

Encapsulation bundles data (attributes) and behavior (methods) together while restricting direct access to an object's internal state.

| Modifier Type | Naming Convention | Accessibility | Behavior |
| --- | --- | --- | --- |
| **Public** | `name`<br> | Global

 | Accessible anywhere inside or outside the class.

 |
| **Protected** | `_age` (single underscore)

 | Class & Subclasses

 | Signifies protected internal scope by convention.

 |
| **Private** | `__height` (double underscore)

 | Declaring Class Only

 | Protected from outside access via Python name mangling.

 |

```python
class Animal:
    def __init__(self):
        self.name = "Lion"       # Public attribute[cite: 73, 75]
        self._age = 12           # Protected attribute[cite: 73, 75]
        self.__secret_id = 9981  # Private attribute[cite: 73, 75]

    def speak(self):
        print("The lion roars")  # Public method[cite: 73, 75]

    def _walk(self):
        print("The lion is walking")  # Protected method[cite: 73, 75]

    def __sleep(self):
        print("The lion is sleeping")  # Private method[cite: 73, 75]

a = Animal()
print(a.name)        # Allowed (Public)[cite: 73, 75]
print(a._age)        # Accessible, but marked protected by convention[cite: 73, 75]
# print(a.__secret_id) # Raises AttributeError: Private attribute is hidden[cite: 73, 75]

```

*Files: `Inceptuletion.py`, `Abstraction.py*`

---

### Pillar 3: Polymorphism (Overriding vs. Overloading)

Polymorphism means "many forms". It allows distinct classes to provide their own specific implementations for identically named methods.

#### Method Overriding

Occurs when a child class redefines a method inherited from its parent. The child's version takes precedence during object execution. You can call the parent's implementation using `super()`.

```python
class Reebok:
    def __init__(self, material, size):
        self.material = material
        self.size = size

    def details(self):
        print(f"Material: {self.material}, Size: {self.size}")

class Campus(Reebok):
    def __init__(self, material, size, color):
        super().__init__(material, size)
        self.color = color

    def details(self):
        super().details()  # Invokes the parent implementation[cite: 73, 75]
        print(f"Color: {self.color}")

bag = Campus("Leather", 10, "Black")
bag.details()

```

*Files: `poiymorphism.py`, `Abstraction.py*`

#### Method Overloading in Python

In languages like Java or C++, method overloading allows multiple methods in the same class to share a name if they have different parameter lists. In Python, defining a method multiple times simply overwrites earlier definitions with the most recent one. To achieve overloading, use variable positional arguments (`*args`) or default values.

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c  # Simulates overloading using default arguments[cite: 63, 64]

calc = Calculator()
print(calc.add(2, 3))     # Returns 5
print(calc.add(2, 3, 4))  # Returns 9

```

*Files: `Abstraction.py`, `poiymorphism.py*`

---

### Pillar 4: Abstraction (Abstract Base Classes)

Abstraction hides complex implementation details while exposing only the necessary interface to the user. An **Abstract Base Class (ABC)** serves as a strict structural template: child classes *must* implement every method decorated with `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement this method[cite: 73]

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

sq = Square(5)
print("Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())

```

*File: `Abstraction.py*`

---

## 4. Operator Overloading & Dunder Magic Methods

Dunder (Double Underscore) methods allow custom classes to hook into built-in Python behaviors, such as string formatting and mathematical operators.

* **`__str__()`:** Defines the user-friendly string representation displayed when passing an object to `print()`.


* **`__add__()`:** Overloads the addition operator (`+`).


* **`__eq__()`:** Overloads the equality comparison operator (`==`).



```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value: {self.value}"  # Called by print()[cite: 73]

    def __add__(self, other):
        return CustomNumber(self.value + other.value)  # Overloads '+'[cite: 73]

    def __eq__(self, other):
        return self.value == other.value               # Overloads '=='[cite: 73]

num1 = CustomNumber(20)
num2 = CustomNumber(30)
num3 = CustomNumber(20)

print(num1)              # Value: 20[cite: 73]
print((num1 + num2))     # Value: 50[cite: 73]
print(num1 == num3)      # True[cite: 73]
print(num1 == num2)      # False[cite: 73]

```

*File: `Abstraction.py*`

---

## 5. Real-World Capstone Project: School Admission Portal

Demonstrates hierarchical inheritance, `super()` constructor chaining, dynamic user selection, and boundary condition validation within an educational admissions portal.

```python
class Student:
    def __init__(self, name, age, email, phone_no):
        self.name = name
        self.age = age
        self.email = email
        self.phone_no = phone_no
        print("Welcome to SSSVM Bhopal Portal")

    def display(self):
        print(f"""
        --- Student Details ---
        Name: {self.name}
        Age: {self.age}
        Email: {self.email}
        Phone Number: {self.phone_no}
        """)

class Class10Th(Student):
    def __init__(self, name, age, email, phone_no):
        super().__init__(name, age, email, phone_no)
        if self.age <= 16:
            print("Status: Admission Successful for 10th Grade")
        else:
            print("Status: Admission Denied (Age exceeds limit)")

class Class12Th(Student):
    def __init__(self, name, age, email, phone_no):
        super().__init__(name, age, email, phone_no)
        if self.age <= 18:
            print("Status: Admission Successful for 12th Grade")
        else:
            print("Status: Admission Denied (Age exceeds limit)")

# Interactive execution driver[cite: 80]
print("Press 1 for Class 10th Admission")
print("Press 2 for Class 12th Admission")

choice = int(input("Enter your choice: "))
name = input("Enter name: ")
age = int(input("Enter age: "))
email = input("Enter email: ")
phone = input("Enter phone number: ")

if choice == 1:
    applicant = Class10Th(name, age, email, phone)
    applicant.display()
elif choice == 2:
    applicant = Class12Th(name, age, email, phone)
    applicant.display()
else:
    print("Invalid Selection.")

```

*File: `OOP Project.py*`

---

## 📂 Repository File & Assignment Directory

* **`OOP.py`:** Core introduction to class blueprints, attributes vs. methods, the `self` identifier, constructor execution flow, `@classmethod`, and `@staticmethod` utilities.


* **`Demo.py`:** Practical examples of base/derived constructor delegations using `super()` across vehicle and animal hierarchies.


* **`Inheritance.py`:** Reference implementations of Single, Multiple, Multilevel, and Hierarchical inheritance patterns.


* **`Inceptuletion.py`:** Demonstrations of public, protected (`_`), and private (`__`) access modifiers and name mangling behaviors.


* **`poiymorphism.py`:** Method overriding via `super()` alongside single-class method replacement behavior in Python.


* **`Abstraction.py`:** Abstract Base Classes (`abc`), `@abstractmethod` decorators, and dunder operator overrides (`__str__`, `__add__`, `__eq__`).


* **`OOP Project.py`:** Working interactive portal evaluating age criteria and student admissions through inherited class hierarchies.


* **`Python OOPs Assignment — Inheritance Basics.ipynb`:** Foundational assignment notebook covering basic inheritance problems (Animal/Dog, Vehicle/Bike, Person/Teacher, Bank/SavingsAccount).


* **`Python OOPs Assignment Inheritance 2.ipynb`:** Intermediate assignment notebook detailing real-world Single, Multilevel, Multiple, and Hierarchical models.


* **`Python OOPs Assignment — Inheritance Practice.ipynb`:** Practical lab challenges covering complex class structures (Country/State/City, Electronics/Laptop, Appliance/WashingMachine).


