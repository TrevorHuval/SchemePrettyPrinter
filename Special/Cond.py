# Cond -- Parse tree node strategy for printing the special form cond

from Special import Special
import sys


class Cond(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for _ in range(n):
            sys.stdout.write(' ')
        cdr = t.getCdr()
        sys.stdout.write("(cond \n")
        n = n + 4
        while(cdr.isNull() == False):
            for _ in range(n):
                sys.stdout.write(' ')
            cdr.getCar().print(0, False)
            sys.stdout.write("\n")
            cdr = cdr.getCdr()
        cdr.print(0, True)
        pass
