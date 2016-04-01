#!/usr/bin/python

import sys
print sys.argv[1]

with open(sys.argv[1], 'r') as f:
    print f
    print f.read()

f.close()
