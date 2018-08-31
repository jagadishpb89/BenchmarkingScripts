#! /usr/bin/python

import commands
import os




output = commands.getoutput("kubectl get rs")

lines = output.split("\n")[1:]

for line in lines:
   rs = line.split(" ")[0]
   cmd = "kubectl delete rs " + rs + " &"
   os.system(cmd)
