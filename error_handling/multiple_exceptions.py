"""
Topic: Error Handling
File: multiple_exceptions.py
Description: Demonstrates how to handle multiple exception types in a single try/except block.

Learning Objectives:
    - Understand that different operations can raise different exceptions
    - Use multiple `except` clauses to handle each exception type specifically
    - Use a tuple of exceptions to handle several types in one clause
    - Write more robust programs that gracefully respond to unexpected input

Usage:
    python multiple_exceptions.py
"""

# ─────────────────────────────────────────────
# HANDLING MULTIPLE EXCEPTION TYPES
# ─────────────────────────────────────────────

# Python lets you have multiple `except` blocks after a single `try`.
# Each block catches a specific kind of error, so you can respond
# appropriately rather than giving the same generic message for everything.


def safe_divide(numerator, denominator):
    """Divide two numbers safely, handling bad input types and divide-by-zero."""
    try:
        # int() will raise ValueError if the string can't be converted
        # e.g., int("hello") → ValueError
        num = int(numerator)
        den = int(denominator)

        # ZeroDivisionError is raised when you divide by zero
        result = num / den
        return result

    except ValueError:
        # Catches the case where the input is not a valid integer string
        print(f"  [ValueError] Could not convert '{numerator}' or '{denominator}' to an integer.")
        return None

    except ZeroDivisionError:
        # Catches division by zero specifically
        print(f"  [ZeroDivisionError] Cannot divide {numerator} by zero.")
        return None


def access_list_item(data, index):
    """Retrieve an item from a list safely, handling index and type errors."""
    try:
        # TypeError is raised if `index` is not an integer (e.g., a string like "a")
        # IndexError is raised if `index` is out of range
        item = data[index]
        return item

    except IndexError:
        # The index number is valid (an int) but out of bounds for the list
        print(f"  [IndexError] Index {index} is out of range for a list of length {len(data)}.")
        return None

    except TypeError:
        # The index is not a valid type (e.g., passing a string as an index)
        print(f"  [TypeError] List indices must be integers, not '{type(index).__name__}'.")
        return None


def parse_user_age(raw_input):
    """
    Parse a user's age from a string, then validate it's a reasonable value.
    Shows how to combine multiple except clauses with a broad fallback.
    """
    try:
        age = int(raw_input)          # ValueError if not a number
        if age < 0 or age > 150:
            # Raise our own ValueError for logically invalid ages
            raise ValueError(f"Age {age} is out of the realistic range (0–150).")
        return age

    except ValueError as e:
        # Catches both the int() conversion failure AND our manual raise above
        # `e` holds the exception object, so we can print the actual message
        print(f"  [ValueError] Invalid age input: {e}")
        return None

    except Exception as e:
        # A broad catch-all for any unexpected error.
        # It's good practice to put this LAST so specific handlers run first.
        print(f"  [Unexpected error] {type(e).__name__}: {e}")
        return None


# ─────────────────────────────────────────────
# HANDLING MULTIPLE EXCEPTIONS IN ONE CLAUSE
# ─────────────────────────────────────────────

def risky_lookup(mapping, key):
    """
    Look up a key in a dict and return its integer value.
    Shows using a tuple in a single `except` to catch several exception types at once.
    """
    try:
        # KeyError if `key` doesn't exist in the dict
        raw = mapping[key]
        # ValueError if the stored value can't be converted to int
        return int(raw)

    except (KeyError, ValueError) as e:
        # A tuple of exceptions means: catch either of these two types.
        # Useful when your response to each error would be identical.
        print(f"  [KeyError or ValueError] {type(e).__name__}: {e}")
        return None


# ─────────────────────────────────────────────
# MAIN — RUNNABLE EXAMPLES
# ─────────────────────────────────────────────

if __name__ == "__main__":

    print("=" * 55)
    print("  Example 1: safe_divide()")
    print("=" * 55)

    # Normal successful division
    print(f"10 / 2 = {safe_divide(10, 2)}")

    # Denominator is zero → ZeroDivisionError
    print("Trying 5 / 0:")
    safe_divide(5, 0)

    # Non-numeric string → ValueError
    print("Trying 'abc' / 3:")
    safe_divide("abc", 3)

    print()
    print("=" * 55)
    print("  Example 2: access_list_item()")
    print("=" * 55)

    fruits = ["apple", "banana", "cherry"]

    # Valid access
    print(f"Index 1: {access_list_item(fruits, 1)}")

    # Index out of range → IndexError
    print("Trying index 10:")
    access_list_item(fruits, 10)

    # Wrong type for index → TypeError
    print("Trying index 'first':")
    access_list_item(fruits, "first")

    print()
    print("=" * 55)
    print("  Example 3: parse_user_age()")
    print("=" * 55)

    # Valid age
    print(f"Age '25': {parse_user_age('25')}")

    # Not a number → ValueError from int()
    print("Age 'twenty':")
    parse_user_age("twenty")

    # Out of realistic range → ValueError we raised manually
    print("Age '200':")
    parse_user_age("200")

    print()
    print("=" * 55)
    print("  Example 4: risky_lookup() — tuple of exceptions")
    print("=" * 55)

    config = {"timeout": "30", "retries": "five", "port": "8080"}

    # Successful lookup and conversion
    print(f"'timeout': {risky_lookup(config, 'timeout')}")

    # Key not found → KeyError
    print("Key 'host':")
    risky_lookup(config, "host")

    # Key found but value can't be converted → ValueError
    print("Key 'retries' (value='five'):")
    risky_lookup(config, "retries")

    print()
    print("✅ All examples completed — no unhandled exceptions!")
