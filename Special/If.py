# If -- Parse tree node strategy for printing the special form if

from Special import Special
import sys


class If(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        if p == False:
            sys.stdout.write("(")

        t.car.print(1)
        t.cdr.print(1, True)

        pass
