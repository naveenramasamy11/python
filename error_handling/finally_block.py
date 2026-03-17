"""
Topic: Error Handling
File: finally_block.py
Description: Demonstrates the use of the `finally` block for guaranteed cleanup code that runs regardless of whether an exception occurred.

Learning Objectives:
    - Understand why `finally` is essential for resource cleanup
    - Use try/except/finally together to handle errors and clean up
    - Recognize that `finally` runs even when an exception is not caught
    - Apply `finally` in real-world patterns like file and connection handling

Usage:
    python finally_block.py
"""

# ─────────────────────────────────────────────
# EXAMPLE 1: Basic try/except/finally structure
# ─────────────────────────────────────────────

print("=" * 55)
print("EXAMPLE 1: Basic try/except/finally")
print("=" * 55)

def divide_numbers(a, b):
    """Divide a by b, demonstrating finally always runs."""
    try:
        # Attempt the division — this might raise ZeroDivisionError
        result = a / b
        print(f"  Result: {a} / {b} = {result}")
    except ZeroDivisionError:
        # This block only runs when b is 0
        print(f"  Error: Cannot divide {a} by zero!")
    finally:
        # This block ALWAYS runs — whether an error occurred or not
        # Great place for cleanup tasks (close files, release locks, etc.)
        print("  [finally] Cleanup complete — this always runs.\n")

if __name__ == "__main__":
    divide_numbers(10, 2)   # Normal case — no exception
    divide_numbers(10, 0)   # Exception case — finally still runs

# ─────────────────────────────────────────────
# EXAMPLE 2: finally with a simulated file operation
# ─────────────────────────────────────────────

print("=" * 55)
print("EXAMPLE 2: finally simulating file open/close")
print("=" * 55)

def read_file_simulation(filename, should_fail=False):
    """
    Simulates opening a file and reading from it.
    Uses finally to guarantee the 'file' is always 'closed'.
    """
    file_handle = None
    try:
        print(f"  Opening file: {filename}")
        file_handle = f"<FileHandle:{filename}>"  # Simulated file handle

        if should_fail:
            # Simulate an unexpected read error
            raise IOError("Disk read error!")

        # Simulate successful read
        print(f"  Reading from {filename}... done.")

    except IOError as e:
        # Handle specific I/O errors gracefully
        print(f"  IOError caught: {e}")

    finally:
        # Always close the file — even if an exception was raised
        if file_handle:
            print(f"  [finally] Closing {file_handle}")
        else:
            print("  [finally] No file was opened.")
        print()

if __name__ == "__main__":
    read_file_simulation("data.txt", should_fail=False)  # Succeeds
    read_file_simulation("data.txt", should_fail=True)   # Fails — finally still closes

# ─────────────────────────────────────────────
# EXAMPLE 3: finally runs even without except
# ─────────────────────────────────────────────

print("=" * 55)
print("EXAMPLE 3: finally without except (re-raises exception)")
print("=" * 55)

def risky_operation(value):
    """
    Uses try/finally WITHOUT except.
    If an exception occurs it still propagates up, but finally runs first.
    """
    try:
        print(f"  Processing value: {value}")
        if not isinstance(value, int):
            # Raise a TypeError if value isn't an integer
            raise TypeError(f"Expected int, got {type(value).__name__}")
        print(f"  Squared: {value ** 2}")
    finally:
        # This cleanup runs even if the exception is not caught here
        print("  [finally] Always cleaning up after risky_operation.\n")

if __name__ == "__main__":
    risky_operation(5)       # Works fine

    try:
        risky_operation("oops")  # Raises TypeError — caught by outer try
    except TypeError as e:
        print(f"  Outer except caught: {e}\n")

# ─────────────────────────────────────────────
# EXAMPLE 4: Real-world pattern — database connection simulation
# ─────────────────────────────────────────────

print("=" * 55)
print("EXAMPLE 4: Database connection simulation")
print("=" * 55)

class FakeDatabase:
    """Simulates a database connection for demo purposes."""

    def connect(self):
        print("  [DB] Connection opened.")
        self.connected = True

    def query(self, sql, fail=False):
        if fail:
            raise RuntimeError("Query execution failed!")
        print(f"  [DB] Executed: {sql}")
        return [{"id": 1, "name": "Naveen"}, {"id": 2, "name": "Alice"}]

    def close(self):
        self.connected = False
        print("  [DB] Connection closed.")

def fetch_users(fail_query=False):
    db = FakeDatabase()
    try:
        db.connect()
        # Attempt to run a query — may raise RuntimeError
        results = db.query("SELECT * FROM users", fail=fail_query)
        for row in results:
            print(f"  [DB] Row: {row}")
    except RuntimeError as e:
        # Handle query failures
        print(f"  [DB] Error: {e}")
    finally:
        # Always close the connection — this prevents resource leaks
        db.close()
        print()

if __name__ == "__main__":
    fetch_users(fail_query=False)  # Successful query
    fetch_users(fail_query=True)   # Failed query — connection still closed
