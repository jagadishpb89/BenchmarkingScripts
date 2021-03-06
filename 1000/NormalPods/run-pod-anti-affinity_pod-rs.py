#! /usr/bin/python
import sys
import os
import commands

if len(sys.argv) <= 2:
  print("Minimum one argument needed for this python file!")
else:
  print commands.getoutput("mkdir -p pod-anti-affinity-yamls")
  for index in range(int(sys.argv[1])):
     f = open("template-pod-anti-affinity-pod-rs-with-labelC.yaml", "r")
     filedata = f.read()
     f.close()
     #filedata = filedata.replace("key", "key" + str(index))
     #filedata = filedata.replace("value", "value" + str(index))
     filedata = filedata.replace("cpureq", str(int(sys.argv[3])) + "m")
     filedata = filedata.replace("memreq", str(int(sys.argv[4])) + "Ki")
     filedata = filedata.replace("cpulim", str(int(sys.argv[5])) + "m")
     filedata = filedata.replace("memlim", str(int(sys.argv[6])) + "Ki")
     filedata = filedata.replace("nginx-pod-anti-affinity-pod", "nginx-pod-anti-affinity-pod-" + str(index) + "-" + str(int(sys.argv[7])))
     filedata = filedata.replace("replicas_value", sys.argv[2])
     newfile = "pod-anti-affinity-pod-rs-" + str(index) + "-" + str(int(sys.argv[7])) + ".yaml"
     f_new = open("pod-anti-affinity-yamls/" + newfile, "w")
     f_new.write(filedata)
     f_new.close()
     cmd = "kubectl create -f " + "pod-anti-affinity-yamls/" + newfile
     print cmd
     os.system(cmd)
#     print commands.getoutput(cmd)
