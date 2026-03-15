"""
Topic: Error Handling
File: try_except_basic.py
Description: Learn how to gracefully handle errors using Python's try/except block.

Learning Objectives:
    - Understand what exceptions are and why they occur
    - Use try/except to catch and handle errors without crashing your program
    - Identify common built-in exceptions (ZeroDivisionError, ValueError, TypeError)

Usage:
    python try_except_basic.py
"""

# ─────────────────────────────────────────────
# WHAT IS AN EXCEPTION?
# ─────────────────────────────────────────────
# An exception is an error that happens during program execution.
# Without handling it, Python stops the program and shows a traceback.
# With try/except, we can catch that error and respond gracefully.

# ─────────────────────────────────────────────
# EXAMPLE 1: ZeroDivisionError
# ─────────────────────────────────────────────
# Dividing any number by zero is mathematically undefined.
# Python raises a ZeroDivisionError when this happens.

print("=" * 50)
print("EXAMPLE 1: Handling ZeroDivisionError")
print("=" * 50)


def safe_divide(a, b):
    try:
        # This line might raise a ZeroDivisionError if b is 0
        result = a / b
        print(f"  {a} / {b} = {result}")
    except ZeroDivisionError:
        # This block runs only if a ZeroDivisionError is raised above
        print(f"  Error: Cannot divide {a} by zero!")


safe_divide(10, 2)   # Works fine → 5.0
safe_divide(7, 0)    # Triggers ZeroDivisionError → handled gracefully
safe_divide(100, 4)  # Works fine → 25.0


# ─────────────────────────────────────────────
# EXAMPLE 2: ValueError
# ─────────────────────────────────────────────
# A ValueError occurs when a function receives the right type
# but an inappropriate value — e.g., converting "abc" to an int.

print()
print("=" * 50)
print("EXAMPLE 2: Handling ValueError")
print("=" * 50)


def convert_to_int(value):
    try:
        # int() will raise ValueError if the string isn't a valid number
        number = int(value)
        print(f"  Converted '{value}' → {number}")
    except ValueError:
        # Catch it and tell the user what went wrong
        print(f"  Error: '{value}' is not a valid integer.")


convert_to_int("42")     # Valid   → 42
convert_to_int("hello")  # Invalid → ValueError caught
convert_to_int("7")      # Valid   → 7
convert_to_int("3.14")   # Invalid → "3.14" is a float string, not int


# ─────────────────────────────────────────────
# EXAMPLE 3: TypeError
# ─────────────────────────────────────────────
# A TypeError happens when an operation is applied to the wrong type.
# e.g., adding a string and an integer without conversion.

print()
print("=" * 50)
print("EXAMPLE 3: Handling TypeError")
print("=" * 50)


def add_values(a, b):
    try:
        # This will fail if a and b are incompatible types (e.g., int + str)
        result = a + b
        print(f"  {a!r} + {b!r} = {result}")
    except TypeError as e:
        # `as e` captures the exception object so we can print its message
        print(f"  TypeError caught: {e}")


add_values(5, 10)              # int + int = 15 ✓
add_values("Hello", " World")  # str + str = "Hello World" ✓
add_values(5, " apples")       # int + str → TypeError caught


# ─────────────────────────────────────────────
# EXAMPLE 4: Catching the Exception Message
# ─────────────────────────────────────────────
# Using `except ExceptionType as e` lets you access the error message.
# This is useful for logging or showing users a helpful message.

print()
print("=" * 50)
print("EXAMPLE 4: Capturing the Error Message")
print("=" * 50)


def open_file(filename):
    try:
        # Attempt to open a file that may not exist
        with open(filename, "r") as f:
            content = f.read()
            print(f"  File content: {content[:50]}")
    except FileNotFoundError as e:
        # Print the actual error message from Python
        print(f"  File not found: {e}")


open_file("nonexistent_file.txt")  # Will raise FileNotFoundError → caught


# ─────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────
print()
print("=" * 50)
print("SUMMARY: Common Exceptions")
print("=" * 50)
exceptions = [
    ("ZeroDivisionError", "Dividing by zero"),
    ("ValueError",        "Wrong value for the type (e.g., int('abc'))"),
    ("TypeError",         "Wrong type for an operation (e.g., 5 + 'a')"),
    ("FileNotFoundError", "File or directory does not exist"),
    ("IndexError",        "List index out of range"),
    ("KeyError",          "Dictionary key not found"),
]
for name, description in exceptions:
    print(f"  {name:<22} → {description}")
