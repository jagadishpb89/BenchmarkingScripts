#! /usr/bin/python
import os
import commands
import time

for i in os.listdir("./normal-pods-yamls"):
   name = "./normal-pods-yamls/" + i
   cmd = "kubectl delete -f " + name
   print commands.getoutput(cmd)

os.system("rm -rf ./normal-pods-yamls")
