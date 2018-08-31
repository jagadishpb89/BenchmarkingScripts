#! /usr/bin/python
import os
import commands
import time

for i in os.listdir("./normal-pods-yamls"):
   time.sleep(1)
   name = "./normal-pods-yamls/" + i
   cmd = "kubectl delete -f " + name + " &"
   os.system(cmd)
#   print commands.getoutput(cmd)

os.system("rm -rf ./normal-pods-yamls")
