# System

Python scripts that interact with the operating system using the `subprocess` module.

## Scripts

| File | Description |
|------|-------------|
| `bash.py` | Runs `ls -l` shell commands via `subprocess.run()`, counts total files and directories, and compares a calculated ratio against a threshold |

## Concepts Covered

- `subprocess.run()` with `shell=True` and `stdout=PIPE`
- Capturing and parsing shell command output
- Conditional logic based on system state

## Example

```bash
python3 bash.py
# Runs in the current directory and prints whether the file/directory ratio is > 90
```

> **Note:** Output will vary depending on the directory from which the script is run.
