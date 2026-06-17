# Multi-Utility Toolkit

## Overview

The Multi-Utility Toolkit is a Python-based menu-driven application developed to demonstrate the use of:

* Built-in Python modules
* Custom packages and modules
* File handling
* Date and time operations
* Mathematical calculations
* Random data generation
* UUID generation
* Dynamic module exploration using `dir()`
* Modular programming concepts

The project follows a structured approach by separating functionalities into different modules and packages, making the code reusable, organized, and easy to maintain.

---

# Project Structure

```
my_toolkit/
│
├── main.py
│
└── custom_utils/
    ├── __init__.py
    ├── file_ops.py
    └── math_utils.py
```

### Description

| File          | Purpose                       |
| ------------- | ----------------------------- |
| main.py       | Main controller program       |
| **init**.py   | Initializes custom package    |
| file_ops.py   | File handling operations      |
| math_utils.py | Custom mathematical utilities |

---

# Modules Used

## Built-in Modules

### datetime

Used for:

* Displaying current date and time
* Formatting dates
* Calculating date differences

### time

Used for:

* Stopwatch functionality
* Countdown timer

### math

Used for:

* Factorial calculations
* Trigonometric functions
* Compound interest
* Geometric calculations

### random

Used for:

* Random number generation
* Random lists
* Password generation
* OTP generation
* Dataset sampling

### uuid

Used for:

* Generating unique identifiers
* Session token simulation

### string

Used for:

* Password generation
* Character collections

---

# Custom Package

## custom_utils

A user-defined package created to demonstrate modular programming.

### file_ops.py

Contains:

* create_file()
* write_to_file()
* read_from_file()
* append_to_file()

### math_utils.py

Contains:

* celsius_to_fahrenheit()
* kilometers_to_miles()
* calculate_cylinder_volume()

---

# Features

## 1. Datetime and Time Operations

### Available Functions

1. Display current date and time
2. Calculate difference between two dates
3. Format dates using strftime()
4. Stopwatch
5. Countdown timer

### Example

```
Current Date and Time:
2026-06-16 20:30:15
```

---

## 2. Mathematical Operations

### Available Functions

1. Factorial calculation
2. Compound interest calculation
3. Trigonometric calculations
4. Area of geometric shapes
5. Advanced custom utilities

### Example

```
Enter number: 5

Factorial = 120
```

---

## 3. Random Data Generation

### Available Functions

1. Random number generation
2. Random list creation
3. Password generation
4. OTP generation
5. Dataset sampling

### Example

```
Generated OTP: 582941
```

---

## 4. UUID Generation

### Available Functions

1. UUID4 generation
2. Session token simulation

### Example

```
Generated UUID:
4e8f57d0-33a9-4d34-90a1-f1d3d47cb8f1
```

---

## 5. File Operations

### Available Functions

1. Create file
2. Write data
3. Read data
4. Append data

### Example

```
File created successfully!
```

---

## 6. Dynamic Module Exploration

The application allows users to inspect loaded modules using Python's `dir()` function.

### Supported Modules

* math
* datetime
* random
* uuid
* file_ops
* math_utils

### Example

```
Enter module name: math

['acos', 'acosh', 'asin', 'asinh', 'atan', ...]
```

---

# Program Flow

```
Main Menu
│
├── Datetime Operations
├── Mathematical Operations
├── Random Data Generation
├── UUID Generation
├── File Operations
├── Module Exploration
└── Exit
```

Each menu contains submenus that execute the corresponding functionality.

---

# Concepts Demonstrated

This project demonstrates:

* Functions
* Modules
* Packages
* Imports
* Loops
* Conditional Statements
* Exception Handling
* File Handling
* User Input Validation
* Menu-Driven Programming
* Built-in Python Libraries
* Custom Module Creation
* Dynamic Introspection using dir()

---

# Use of **name** == "**main**"

```python
if __name__ == "__main__":
    main()
```

Purpose:

* Ensures the program runs only when executed directly.
* Prevents automatic execution when imported into another Python file.
* Supports code reusability.

---

# Error Handling

The project includes exception handling for:

* Invalid numerical input
* Invalid date format
* Missing files
* File access issues
* Invalid menu choices

Example:

```python
try:
    num = int(input())
except ValueError:
    print("Invalid input")
```

---

# Installation

## Step 1

Install Python 3.x

Check installation:

```bash
python --version
```

---

## Step 2

Create project structure exactly as shown.

---

## Step 3

Place all files in their respective folders.

---

## Step 4

Open terminal in project folder.

---

## Step 5

Run:

```bash
python main.py
```

---

# Sample Main Menu

```
Welcome to Multi-Utility Toolkit

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
```

---

# Learning Outcomes

After completing this project, students will understand:

* Python modular programming
* Package creation
* Built-in module usage
* File handling techniques
* Date and time manipulation
* Mathematical computations
* Randomized data generation
* UUID implementation
* Dynamic module inspection
* Structured software development

---

# Conclusion

The Multi-Utility Toolkit is a comprehensive Python application that combines multiple utilities into a single menu-driven system. It demonstrates practical use of Python built-in modules, custom packages, file handling, mathematical processing, and modular software design principles.

This project serves as an excellent example of real-world Python programming using both built-in and user-defined modules.
