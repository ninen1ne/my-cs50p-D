import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    print("=====================")
    cowsay.trex("Hello, " + sys.argv[1])
