#!/usr/bin/env python3.7
temp=input("Enter Celcius/Farenheit like 30C/120F:\n")
value=int(temp[:-1])
cf=(temp[-1])
print(cf)
if (cf == "C") or (cf == "c"):
  ext="F"
  result = int(round((9 * value) / 5 + 32))
elif (cf == "f") or (cf == "F"):
  ext="C"
  result = int(round((value - 32) * 5 / 9))
else:
  print("enter the value with proper extention")
  quit()
val=str(result)
print("The conversion of", temp, "is :" , val+ext)


