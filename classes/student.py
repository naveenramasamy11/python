#!/usr/bin/env python3.7
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Full name is", '{} {}'.format(fname.capitalize(),lname.capitalize()))
    def salary(self,rs):
        self.rs = rs
        rs = rs * 25 / 100
        print("Salary increment for", '{} {}'.format(self.fname.capitalize(),self.lname.capitalize()),  'is:',rs)

std1 = Student('naveen', 'ramasamy')
std2 = Student('roger', 'federer')
std3 = Student('Peter', 'smith')
std1.salary(2000)
std2.salary(3000)
std3.salary(4000)
