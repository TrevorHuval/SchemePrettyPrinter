# Regular -- Parse tree node strategy for printing regular lists

from Special import Special
from Tree import *
import sys


class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.

        car = t.getCar()
        cdr = t.getCdr()

        for _ in range(n):
            sys.stdout.write(' ')

        if p == False:
            sys.stdout.write("(")

        if(car.isPair()):
            car.print(0, False)
        else:
            car.print(0, True)

        if(cdr.isPair() or cdr.isNull()):
            if cdr.isNull():
                cdr.print(0, True)

            else:
                sys.stdout.write(" ")
                cdr.print(0, True)

        else:
            sys.stdout.write(".")
            cdr.print(n, True)
            sys.stdout.write(")")
        pass
