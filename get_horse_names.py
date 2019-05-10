import sys

from horse import Horse

for i in range(0, int(sys.argv[1])):
    h = Horse()
    print(h.name)
