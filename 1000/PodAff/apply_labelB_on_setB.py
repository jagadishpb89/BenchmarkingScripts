#! /usr/bin/python

import commands

output = commands.getoutput("kubectl get nodes | tail -n 200")

outputLines = output.split("\n")

labelB = "labelb1=labelb2"

for outputLine in outputLines[1:]:
   name = outputLine.split(" ")[0]
   cmd = "kubectl label nodes " + name + " " + labelB
   print commands.getoutput(cmd)
