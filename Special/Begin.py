# Begin -- Parse tree node strategy for printing the special form begin

from Special import Special
import sys


class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        for _ in range(n):          # for loop to indicate the number of spaces for indention
            sys.stdout.write(' ')
        cdr = t.getCdr()
        sys.stdout.write("(begin \n")

        n = n + 4   # Increase indention for everything in the begin function after "begin"

        while(cdr.isNull() == False):
            for _ in range(n):
                sys.stdout.write(' ')

            if(cdr.getCar().isPair()):
                cdr.getCar().print(0, False)
            else:
                cdr.getCar().print(0, True)
            sys.stdout.write("\n")
            cdr = cdr.getCdr()
        cdr.print(0, True)
        pass
