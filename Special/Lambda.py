# Lambda -- Parse tree node strategy for printing the special form lambda

from Special import Special
import sys


class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for _ in range(n):
            sys.stdout.write(' ')

        car = t.getCar()
        cdr = t.getCdr()
        cddr = t.getCdr().getCdr()

        sys.stdout.write("(")
        car.print(0, True)
        sys.stdout.write(" ")
        cdr.getCar().print(0, False)
        sys.stdout.write("\n")
        while(cddr.isNull() == False):
            cddr.getCar().print(n+4, True)
            cddr = cddr.getCdr()
            sys.stdout.write("\n")
        cddr.print(n, True)
        pass

#   (lambda (x y)
#       (...)
#   )
