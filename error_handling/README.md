# Error Handling

> Learn how to write resilient Python programs that handle unexpected situations gracefully using `try`, `except`, `finally`, and custom exceptions.

## What You'll Learn

Error handling is a critical skill for writing production-quality Python. Instead of letting your program crash when something goes wrong, you'll learn to anticipate errors, catch them, and respond in a controlled way — making your code more robust and user-friendly.

## Examples

| File | Description | Key Concepts |
|------|-------------|--------------|
| [try_except_basic.py](try_except_basic.py) | Introduction to try/except blocks | `ZeroDivisionError`, `ValueError`, `TypeError`, `FileNotFoundError`, `except as e` |

## How to Run

```bash
python3 try_except_basic.py
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
