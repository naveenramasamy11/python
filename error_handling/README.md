# Error Handling

> Learn how to write resilient Python programs that handle unexpected situations gracefully using `try`, `except`, `finally`, and custom exceptions.

## What You'll Learn

Error handling is a critical skill for writing production-quality Python. Instead of letting your program crash when something goes wrong, you'll learn to anticipate errors, catch them, and respond in a controlled way — making your code more robust and user-friendly.

## Examples

| File | Description | Key Concepts |
|------|-------------|--------------|
| [try_except_basic.py](try_except_basic.py) | Introduction to try/except blocks | `ZeroDivisionError`, `ValueError`, `TypeError`, `FileNotFoundError`, `except as e` |
| [multiple_exceptions.py](multiple_exceptions.py) | Handling multiple exception types in one try block | Multiple `except` clauses, tuple of exceptions, `except as e`, broad fallback with `Exception` |
| [finally_block.py](finally_block.py) | Using `finally` for guaranteed cleanup code | `try/except/finally`, resource cleanup, file/DB connection patterns, finally without except |
| [custom_exceptions.py](custom_exceptions.py) | Defining and raising your own custom exception classes | `class MyError(Exception)`, custom `__init__`, exception hierarchies, re-raising with `raise` |
| [exception_chaining.py](exception_chaining.py) | Chaining exceptions with `raise ... from` to preserve error context | `raise X from Y`, `raise X from None`, `__cause__`, `__context__`, `__suppress_context__` |

## How to Run

```bash
python3 try_except_basic.py
python3 multiple_exceptions.py
python3 finally_block.py
python3 custom_exceptions.py
python3 exception_chaining.py
```

## Prerequisites

- Python 3.7+
- No external libraries required
- Recommended: complete `functions/` examples first

## Common Built-in Exceptions

| Exception | When It Occurs |
|-----------|----------------|
| `ZeroDivisionError` | Dividing by zero |
| `ValueError` | Invalid value for a type (e.g. `int("abc")`) |
| `TypeError` | Operation on incompatible types |
| `FileNotFoundError` | File or directory does not exist |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `AttributeError` | Object has no such attribute |
| `NameError` | Variable used before being defined |
