#!/usr/bin/env python3
"""Temperature converter between Celsius and Fahrenheit."""

temp = input("Enter temperature (e.g. 30C or 120F): ").strip()
try:
    value = int(temp[:-1])
    unit = temp[-1].upper()
    if unit == "C":
        result = round((9 * value) / 5 + 32)
        print(f"{temp} = {result}F")
    elif unit == "F":
        result = round((value - 32) * 5 / 9)
        print(f"{temp} = {result}C")
    else:
        print("Invalid unit. Use C for Celsius or F for Fahrenheit (e.g. 30C or 120F).")
except ValueError:
    print("Invalid input. Please enter a number followed by C or F (e.g. 30C).")
