#!/usr/bin/python
from pwn import proc
import os
import time
def print_descendants(pid, iterations):
    if (pid is None):
        return
    cid = proc.descendants(pid)
    for x in cid:
        print "\t" + " "*iterations + proc.exe(pid) +":\t" + "--> " + proc.exe(x)
        print_descendants(x, iterations+1)
    
    spaces = 0

if os.geteuid() != 0:
        print "You need to have root privileges to run this script."
        time.sleep(2)
        print "Dumbass..."
        exit()

p = proc.descendants(1)
for i in p:
    print proc.exe(i)
    print_descendants(i, 0)
