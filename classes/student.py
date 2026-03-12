#!/usr/bin/env python3
"""Student class demonstrating instance variables and methods."""


class Student:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        print(f"Full name: {self.fname} {self.lname}")

    def salary_increment(self, current_salary: float) -> None:
        increment = current_salary * 0.25
        print(f"Salary increment for {self.fname} {self.lname}: {increment:.2f}")


std1 = Student("naveen", "ramasamy")
std2 = Student("roger", "federer")
std3 = Student("peter", "smith")
std1.salary_increment(2000)
std2.salary_increment(3000)
std3.salary_increment(4000)
