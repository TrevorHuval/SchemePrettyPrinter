# Let -- Parse tree node strategy for printing the special form let

from Special import Special
import sys


class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for _ in range(n):
            sys.stdout.write(' ')
        cdr = t.getCdr()
        sys.stdout.write("(let \n")
        n = n + 4
        while(cdr.isNull() == False):
            for _ in range(n):
                sys.stdout.write(' ')
            cdr.getCar().print(0, False)
            sys.stdout.write("\n")
            cdr = cdr.getCdr()
        sys.stdout.write(")")
        pass
