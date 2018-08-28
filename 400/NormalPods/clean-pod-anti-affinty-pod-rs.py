#! /usr/bin/python
import os
import commands
import time

for i in os.listdir("./pod-anti-affinity-yamls"):
   name = "./pod-anti-affinity-yamls/" + i
   cmd = "kubectl delete -f " + name
   print commands.getoutput(cmd)

os.system("rm -rf ./pod-anti-affinity-yamls")
