#! /usr/bin/python
import os
import commands
import time

for i in os.listdir("./symmetry-pods-yamls"):
   name = "./symmetry-pods-yamls/" + i
   cmd = "kubectl delete -f " + name
   print commands.getoutput(cmd)

os.system("rm -rf ./symmetry-pods-yamls")
