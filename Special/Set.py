# Set -- Parse tree node strategy for printing the special form set!

from Special import Special
import sys


class Set(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for _ in range(n):
            sys.stdout.write(' ')

        sys.stdout.write("(set! ")
        t.getCdr().print(0, True)

        pass
