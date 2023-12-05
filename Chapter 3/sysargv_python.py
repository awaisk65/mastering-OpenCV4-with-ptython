#!/usr/bin/env python3

import sys	

"""
USAGE: python3 sysargv_python.py <first input> <second input> 
"""

# We will print some information in connection with sys.argv to see how it works:
print("The name of the 1st script being processed is:		'{}'".format(sys.argv[0]))
print("The name of the 2nd script being processed is:		'{}'".format(sys.argv[1]))
print("The name of the 3rd script being processed is:		'{}'".format(sys.argv[2]))
print("The number of arguments of the script is:		'{}'".format(len(sys.argv)))
print("The arguments of the script are: '{}'".format(str(sys.argv)))