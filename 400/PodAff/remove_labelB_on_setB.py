#! /usr/bin/python

import commands

output = commands.getoutput("kubectl get nodes | head -n 201")

outputLines = output.split("\n")

removelabelB = "labelb1-"

for outputLine in outputLines[1:] :
   name = outputLine.split(" ")[0]
   cmd = "kubectl label nodes " + name + " " + removelabelB + " &"
   print commands.getoutput(cmd)
