"""
Topic: Error Handling
File: custom_exceptions.py
Description: How to define and raise your own custom exception classes in Python.

Learning Objectives:
    - Understand why custom exceptions make code more readable and maintainable
    - Learn how to create custom exception classes by inheriting from Exception
    - Practice raising and catching custom exceptions with meaningful messages
    - See how to add extra attributes (like error codes) to custom exceptions

Usage:
    python custom_exceptions.py
"""

# ─────────────────────────────────────────────
# CUSTOM EXCEPTION BASICS
# ─────────────────────────────────────────────

# Python lets you create your own exception types by inheriting from Exception.
# This is useful when built-in exceptions (ValueError, TypeError, etc.) are
# too generic for your specific use case.

# ── Example 1: Simplest possible custom exception ──────────────────────────

class InsufficientFundsError(Exception):
    """Raised when a bank withdrawal exceeds the available balance."""
    pass  # 'pass' means we inherit everything from Exception as-is


def withdraw(balance, amount):
    """Attempt to withdraw 'amount' from 'balance'. Raises if funds are low."""
    if amount > balance:
        # We raise our custom exception with a helpful message
        raise InsufficientFundsError(
            f"Cannot withdraw ${amount:.2f} — only ${balance:.2f} available."
        )
    return balance - amount


print("=== Example 1: Simple Custom Exception ===")
try:
    new_balance = withdraw(100.00, 150.00)
except InsufficientFundsError as e:
    # 'e' holds the exception instance; str(e) gives the message we passed
    print(f"Caught InsufficientFundsError: {e}")

# Successful withdrawal — no exception raised
new_balance = withdraw(200.00, 50.00)
print(f"Withdrawal successful! New balance: ${new_balance:.2f}\n")


# ── Example 2: Custom exception with extra attributes ──────────────────────

# You can add your own __init__ to store extra data alongside the message.
# This makes it easy for callers to inspect the error programmatically.

class ValidationError(Exception):
    """Raised when user-supplied data fails validation rules."""

    def __init__(self, field, message):
        # Call the parent __init__ so the exception message is set correctly
        super().__init__(f"Validation failed on '{field}': {message}")
        # Store the field name so callers can query which field failed
        self.field = field


def validate_age(age):
    """Validates that age is a positive integer not exceeding 150."""
    if not isinstance(age, int):
        raise ValidationError("age", "must be an integer")
    if age < 0:
        raise ValidationError("age", "cannot be negative")
    if age > 150:
        raise ValidationError("age", "exceeds maximum realistic value of 150")


print("=== Example 2: Custom Exception with Attributes ===")
for test_age in [-5, 200, "thirty", 25]:
    try:
        validate_age(test_age)
        print(f"Age {test_age!r} is valid ✓")
    except ValidationError as e:
        # We can access the custom attribute 'field' from the exception object
        print(f"  field='{e.field}' | error: {e}")
print()


# ── Example 3: Exception hierarchy — multiple custom exceptions ─────────────

# You can build a hierarchy so callers can catch either a specific error
# or the whole family by catching the base class.

class AppError(Exception):
    """Base class for all application-level errors."""
    pass

class DatabaseError(AppError):
    """Raised when a database operation fails."""
    pass

class NetworkError(AppError):
    """Raised when a network request fails."""
    pass


def fetch_user(user_id, use_db=True):
    """Simulates fetching a user record — may fail for different reasons."""
    if user_id <= 0:
        raise DatabaseError(f"Invalid user_id={user_id}; must be positive.")
    if not use_db:
        raise NetworkError("Cannot reach database host — connection timed out.")
    return {"id": user_id, "name": "Naveen"}


print("=== Example 3: Exception Hierarchy ===")

# Catch the specific subclass
try:
    fetch_user(-1)
except DatabaseError as e:
    print(f"DatabaseError caught: {e}")

# Catch the base class — handles both DatabaseError and NetworkError
for uid, use_db in [(5, False), (7, True)]:
    try:
        user = fetch_user(uid, use_db=use_db)
        print(f"  User found: {user}")
    except AppError as e:
        # AppError catches any subclass: DatabaseError or NetworkError
        print(f"  AppError caught ({type(e).__name__}): {e}")
print()


# ── Example 4: Re-raising inside an except block ───────────────────────────

# Sometimes you want to log an error, then re-raise it so the caller
# still sees the exception.

class ConfigError(Exception):
    """Raised when a required configuration key is missing."""
    pass


def load_config(config: dict, required_key: str):
    """Load a value from config, raising ConfigError if it's missing."""
    if required_key not in config:
        raise ConfigError(f"Missing required config key: '{required_key}'")
    return config[required_key]


print("=== Example 4: Re-raising a Custom Exception ===")
config = {"host": "localhost", "port": 5432}

try:
    try:
        db_name = load_config(config, "db_name")
    except ConfigError as e:
        print(f"  [LOG] Configuration problem detected: {e}")
        raise  # Re-raise the same exception to the outer handler
except ConfigError as e:
    print(f"  [OUTER] Handled ConfigError: {e}")
print()


if __name__ == "__main__":
    print("All examples completed successfully.")
    print("Key takeaways:")
    print("  1. Inherit from Exception (or a subclass) to create custom exceptions.")
    print("  2. Add a custom __init__ to attach extra data to the exception.")
    print("  3. Build exception hierarchies to group related errors.")
    print("  4. Use 'raise' (no argument) inside except to re-raise the same error.")
