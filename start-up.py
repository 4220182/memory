#!/usr/bin/env python
 
import sys
import time

if len(sys.argv) != 3:
    print "usage: fillmem <init-of-megabytes> <up-of-megabytes>"
    sys.exit()

init_memory = int(sys.argv[1])
up_memory = int(sys.argv[2])

i = 0

while True:
    megabyte = (0,) * (1024 * 1024 / 8)
    data = megabyte * init_memory + megabyte * i
    i = i + up_memory
    time.sleep(1)
