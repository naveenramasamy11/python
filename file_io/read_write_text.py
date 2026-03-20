"""
Topic: File I/O – Reading and Writing Text Files
File: read_write_text.py
Description: Learn how to create, write to, read from, and safely handle text files in Python.

Learning Objectives:
    - Open files using the built-in open() function with different modes
    - Write text content to a file and read it back
    - Use the 'with' statement for safe, automatic file closing
    - Understand common file modes: 'w' (write), 'r' (read), 'r+' (read+write)

Usage:
    python read_write_text.py
"""

# ─────────────────────────────────────────────
# EXAMPLE 1: Writing a Text File
# ─────────────────────────────────────────────

# 'with open(...)' is the preferred way to work with files.
# It automatically closes the file when the block ends — even if an error occurs.
# Mode 'w' creates the file if it doesn't exist, or OVERWRITES it if it does.

print("=" * 50)
print("EXAMPLE 1: Writing a text file")
print("=" * 50)

filename = "/tmp/sample.txt"  # We'll use /tmp so the file doesn't litter the project

with open(filename, "w") as file:
    # write() writes a single string — you must add \n manually for newlines
    file.write("Hello, Python File I/O!\n")
    file.write("This is the second line.\n")
    file.write("Writing to files is straightforward.\n")

print(f"File '{filename}' written successfully.")


# ─────────────────────────────────────────────
# EXAMPLE 2: Reading the Entire File at Once
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("EXAMPLE 2: Reading the entire file at once")
print("=" * 50)

# Mode 'r' opens the file for reading (this is also the default mode)
with open(filename, "r") as file:
    content = file.read()  # read() returns the whole file as a single string

print("File contents:")
print(content)


# ─────────────────────────────────────────────
# EXAMPLE 3: Reading Line by Line
# ─────────────────────────────────────────────

print("=" * 50)
print("EXAMPLE 3: Reading line by line")
print("=" * 50)

with open(filename, "r") as file:
    # readlines() returns a list where each element is one line (including '\n')
    lines = file.readlines()

# enumerate() gives us both the index (line number) and the value (line text)
for i, line in enumerate(lines, start=1):
    # strip() removes the trailing newline character from each line
    print(f"  Line {i}: {line.strip()}")


# ─────────────────────────────────────────────
# EXAMPLE 4: Iterating Over Lines (Memory Efficient)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("EXAMPLE 4: Iterating over lines (memory-efficient)")
print("=" * 50)

# For large files, iterating directly over the file object is best practice.
# Python reads one line at a time instead of loading everything into memory.
with open(filename, "r") as file:
    print("Lines containing 'Python':")
    for line in file:
        if "Python" in line:   # check if the line contains a keyword
            print(f"  >> {line.strip()}")


# ─────────────────────────────────────────────
# EXAMPLE 5: Writing Multiple Lines with writelines()
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("EXAMPLE 5: Writing multiple lines with writelines()")
print("=" * 50)

multi_filename = "/tmp/multi_lines.txt"

# writelines() accepts a list of strings and writes them all — no automatic newlines
lines_to_write = [
    "Line A: AWS Cloud\n",
    "Line B: Terraform IaC\n",
    "Line C: Kubernetes Orchestration\n",
    "Line D: Python Automation\n",
]

with open(multi_filename, "w") as file:
    file.writelines(lines_to_write)  # writes each string in the list sequentially

print(f"Wrote {len(lines_to_write)} lines to '{multi_filename}'.")

# Verify by reading back
with open(multi_filename, "r") as file:
    print("Read back:")
    for line in file:
        print(f"  {line.strip()}")


# ─────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("SUMMARY: File mode quick reference")
    print("=" * 50)
    modes = {
        "'w'":  "Write  – Create new / overwrite existing",
        "'r'":  "Read   – Read only (default mode)",
        "'a'":  "Append – Add to end of existing file",
        "'r+'": "Read+Write – File must already exist",
        "'w+'": "Write+Read – Create new / overwrite existing",
        "'b'":  "Binary – Combine with above, e.g. 'rb', 'wb'",
    }
    for mode, desc in modes.items():
        print(f"  {mode:<6} → {desc}")

    print("\nKey takeaway: Always use 'with open(...)' to ensure files are closed properly.")
