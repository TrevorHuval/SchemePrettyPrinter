# Define -- Parse tree node strategy for printing the special form define

from Special import Special
import sys


class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        car = t.getCar()
        cdr = t.getCdr()

        # If the next token is a Cons node...
        if cdr.getCar().isPair():
            sys.stdout.write("(")
            car.print(0, True)
            sys.stdout.write(" ")
            cdr.getCar().print(0, False)
            sys.stdout.write("\n")
            cdr = cdr.getCdr()
            n = n + 4
            while(cdr.isNull == False):
                cdr.getCar().print(n, False)
                sys.stdout.write("\n")
                cdr = cdr.getCdr()
            sys.stdout.write(")")
        else:
            sys.stdout.write("(define ")
            cdr.print(0, True)
        pass
