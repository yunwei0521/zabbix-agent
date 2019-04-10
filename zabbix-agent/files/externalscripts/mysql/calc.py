#!/bin/env python
import sys
def calc(a,b) :
        return "%.2f" % (a/b*100)
print calc(float(sys.argv[1]),float(sys.argv[2]))
