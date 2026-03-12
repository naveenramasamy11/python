#!/usr/bin/env python3.7
#!/usr/bin/env python3.7
import subprocess
var1 = int((subprocess.run("ls -l| wc -l", shell=True, stdout=subprocess.PIPE, universal_newlines=True)).stdout)
var2 = int((subprocess.run("ls -l| grep '^d' | wc -l", shell=True, stdout=subprocess.PIPE, universal_newlines=True)).stdout)
print(var1)
var3 = var1/var2 * 10
if var3 > 90:
  print("greater than")
else:
  print("less than")