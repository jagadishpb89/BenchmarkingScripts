#!/usr/bin/python

import commands

output = commands.getoutput("kubectl get nodes | head -n 201")

outputLines = output.split("\n")

labelA = "labela1=labela2"

for outputLine in outputLines[1:] :
   name = outputLine.split(" ")[0]
   cmd = "kubectl label nodes " + name + " " + labelA
   print cmd
   print commands.getoutput(cmd)
