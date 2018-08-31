#! /usr/bin/python

import commands

output = commands.getoutput("kubectl get nodes")

outputLines = output.split("\n")

index = 0;

for outputLine in outputLines[1:] :
   name = outputLine.split(" ")[0]
   if "real-master" not in name:
     cmd = "kubectl label nodes " + name + " " + "key" + str(index) + "- "
     index += 1
     print commands.getoutput(cmd)
