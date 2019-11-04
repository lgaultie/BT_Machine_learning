#!/usr/bin/env python

import sys

t = (3,30,2019,9,25)

# sys.stdout.write(str(t[3]))
# sys.stdout.write("/")
# sys.stdout.write(str(t[4]))
# sys.stdout.write("/")
# sys.stdout.write(str(t[2]))
# sys.stdout.write(" 0")
# sys.stdout.write(str(t[0]))
# sys.stdout.write(":")
# sys.stdout.write(str(t[1]))
# sys.stdout.write("\n")

print("0{}/{}/{} 0{}:{}".format(t[3], t[4], t[2], t[0], t[1]))
