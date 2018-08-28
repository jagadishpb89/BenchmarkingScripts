#! /usr/bin/python
import os
import commands
import time

for i in os.listdir("./pod-affinity-yamls"):
   name = "./pod-affinity-yamls/" + i
   cmd = "kubectl delete -f " + name
   print commands.getoutput(cmd)

os.system("rm -rf ./pod-affinity-yamls")
