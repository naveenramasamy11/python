#!/usr/bin/env python3
"""Run shell commands using subprocess and compare file/directory ratio."""

import subprocess


def run_command(cmd: str) -> int:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return int(result.stdout.strip())


total_entries = run_command("ls -l | wc -l")
total_dirs = run_command("ls -l | grep '^d' | wc -l")

print(f"Total entries:     {total_entries}")
print(f"Total directories: {total_dirs}")

if total_dirs > 0:
    ratio = (total_entries / total_dirs) * 10
    if ratio > 90:
        print(f"Ratio {ratio:.1f} is greater than 90")
    else:
        print(f"Ratio {ratio:.1f} is less than or equal to 90")
else:
    print("No subdirectories found.")
