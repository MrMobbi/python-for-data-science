
import sys

assert len(sys.argv) == 2, "more than one atgument is provided"

first_arg = sys.argv[1]

try:
    nbr = int(first_arg)
    if nbr % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
except:
    raise AssertionError("argument is not an integer")
