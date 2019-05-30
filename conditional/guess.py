#!/usr/bin/env python3.7
while True:
  x = input("Guess a number that I have in my mind:\n")
  if int(x) <= 9 and int(x) >= 0:
    print("You guessed it right!!")
    break
  else:
    print("Try again")
