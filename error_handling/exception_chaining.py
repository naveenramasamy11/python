"""
Topic: Exception Chaining
File: exception_chaining.py
Description: Demonstrates how to chain exceptions using 'raise ... from ...' to preserve the original cause.

Learning Objectives:
    - Understand why exception chaining is useful for debugging
    - Use 'raise NewException from original_exception' to chain errors
    - Use 'raise NewException from None' to suppress the original cause
    - Read chained tracebacks to understand the full error story

Usage:
    python exception_chaining.py
"""

# ─────────────────────────────────────────────
# EXCEPTION CHAINING WITH raise ... from ...
# ─────────────────────────────────────────────

# In real applications, low-level errors (like an IOError) are often caught
# and re-raised as higher-level, more meaningful errors.
# Exception chaining lets you preserve the *original* error as context,
# so developers can trace the full problem when debugging.


# ─────────────────────────────────────────────
# EXAMPLE 1: Basic Exception Chaining
# ─────────────────────────────────────────────

class DatabaseConnectionError(Exception):
    """Raised when the application cannot connect to the database."""
    pass


def connect_to_database(host):
    """Simulate attempting a database connection."""
    try:
        # Simulate a low-level network failure
        if host != "localhost":
            raise ConnectionRefusedError(f"No route to host: {host}")
    except ConnectionRefusedError as original_error:
        # 'raise X from Y' chains the new exception to the original one.
        # This means: "DatabaseConnectionError happened BECAUSE OF ConnectionRefusedError"
        raise DatabaseConnectionError(
            f"Failed to connect to database at '{host}'"
        ) from original_error


print("=" * 55)
print("EXAMPLE 1: Basic Exception Chaining")
print("=" * 55)

try:
    connect_to_database("remote-server.example.com")
except DatabaseConnectionError as e:
    print(f"[Caught] {type(e).__name__}: {e}")
    # __cause__ holds the original exception that was chained
    print(f"[Root Cause] {type(e.__cause__).__name__}: {e.__cause__}")

print()


# ─────────────────────────────────────────────
# EXAMPLE 2: Chaining Through Multiple Layers
# ─────────────────────────────────────────────

class ConfigFileError(Exception):
    """Raised when the configuration file cannot be loaded."""
    pass


class AppStartupError(Exception):
    """Raised when the application fails to start."""
    pass


def load_config(path):
    """Simulate loading a config file that doesn't exist."""
    try:
        raise FileNotFoundError(f"File not found: {path}")
    except FileNotFoundError as e:
        # Wrap the low-level file error in a domain-specific error
        raise ConfigFileError(f"Cannot load config from '{path}'") from e


def start_application():
    """Simulate app startup that depends on config."""
    try:
        load_config("/etc/myapp/config.yaml")
    except ConfigFileError as e:
        # Chain again: AppStartupError was caused by ConfigFileError
        raise AppStartupError("Application startup failed") from e


print("=" * 55)
print("EXAMPLE 2: Chaining Through Multiple Layers")
print("=" * 55)

try:
    start_application()
except AppStartupError as e:
    print(f"[Caught] {type(e).__name__}: {e}")
    # Walk the chain to find the root cause
    cause = e.__cause__
    depth = 1
    while cause is not None:
        print(f"  {'  ' * depth}Caused by: {type(cause).__name__}: {cause}")
        cause = cause.__cause__
        depth += 1

print()


# ─────────────────────────────────────────────
# EXAMPLE 3: Suppress the Original Cause with 'raise ... from None'
# ─────────────────────────────────────────────

# Sometimes the original exception contains sensitive details (passwords,
# internal paths, etc.) that you don't want to expose to end users.
# Using 'raise X from None' suppresses the chained cause entirely.

class UserFacingError(Exception):
    """A clean, user-safe error message with no internal details."""
    pass


def fetch_secret_data():
    """Simulate fetching data that fails with an internal/sensitive error."""
    try:
        # Imagine this contains a real connection string with credentials
        raise RuntimeError("DB connect failed: user=admin password=s3cr3t host=internal-db")
    except RuntimeError:
        # Suppress the original cause — hide sensitive info from the user
        raise UserFacingError("Data retrieval failed. Please try again later.") from None


print("=" * 55)
print("EXAMPLE 3: Suppressing the Cause (raise ... from None)")
print("=" * 55)

try:
    fetch_secret_data()
except UserFacingError as e:
    print(f"[Caught] {type(e).__name__}: {e}")
    # __cause__ is None because we used 'from None'
    print(f"[Root Cause hidden?] __cause__ = {e.__cause__}")
    # __suppress_context__ is True when 'from None' is used
    print(f"[Context suppressed?] __suppress_context__ = {e.__suppress_context__}")

print()


# ─────────────────────────────────────────────
# EXAMPLE 4: Implicit Chaining (Without 'from')
# ─────────────────────────────────────────────

# If you raise inside an except block *without* 'from', Python still records
# the original exception automatically as __context__ (not __cause__).
# This is called "implicit chaining".

print("=" * 55)
print("EXAMPLE 4: Implicit Chaining (automatic context)")
print("=" * 55)

def divide_safe(a, b):
    try:
        result = a / b    # This will raise ZeroDivisionError if b == 0
    except ZeroDivisionError:
        # No 'from' here — Python implicitly chains the ZeroDivisionError
        raise ValueError("Division failed: denominator must not be zero")


try:
    divide_safe(10, 0)
except ValueError as e:
    print(f"[Caught] {type(e).__name__}: {e}")
    # __context__ is set automatically (implicit chaining), __cause__ is None
    print(f"[Implicit context] {type(e.__context__).__name__}: {e.__context__}")
    print(f"[Explicit cause]   __cause__ = {e.__cause__}")

print()


# ─────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────

print("=" * 55)
print("SUMMARY: Exception Chaining Quick Reference")
print("=" * 55)
print("  raise NewError() from original_err  → Explicit chain (__cause__)")
print("  raise NewError() from None           → Suppress original (__suppress_context__=True)")
print("  raise NewError() inside except       → Implicit chain (__context__)")
print()
print("  e.__cause__            → The explicitly chained exception (or None)")
print("  e.__context__          → The implicitly chained exception (or None)")
print("  e.__suppress_context__ → True when 'from None' was used")


if __name__ == "__main__":
    pass  # All examples run at module level above for clear sequential output
