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

        # if p == False:
        #    sys.stdout.write("(")
        #
        #t.car.print(n, p)
        #sys.stdout.write(" ")
        #t.cdr.print(n, True)
        # pass

        car = t.getCar()
        cdr = t.getCdr()

        if p == False:
            sys.stdout.write("(")

        if(car.isPair):
            car.print(0, False)
            sys.stdout.write(" ")
        else:
            car.print(0, True)

        if(cdr.isPair or cdr.isNull):
            if cdr.isNull:
                cdr.print(0, True)
            else:
                sys.stdout.write(" ")
                cdr.print(0, True)
        else:
            sys.stdout.write(".")
            cdr.print(n, True)
            sys.stdout.write(")")
        pass
