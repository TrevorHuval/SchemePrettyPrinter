# Cons -- Parse tree node class for representing a Cons node

from Special.Begin import Begin
from Special.Cond import Cond
from Special.Define import Define
from Special.If import If
from Special.Lambda import Lambda
from Special.Let import Let
from Special.Regular import Regular
from Special.Set import Set
from Special.Quote import Quote
from Tree import Node
from Tree import *


class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.

    def parseList(self):
        # TODO: implement this function and any helper functions
        # you might need
        self.form = None

        if self.car.isSymbol() == True:
            # print(self.car.name)
            if self.car.name == "quote":
                self.form = Quote()
            elif self.car.name == "lambda":
                self.form = Lambda()
            elif self.car.name == "begin":
                self.form = Begin()
            elif self.car.name == "if":
                self.form = If()
            elif self.car.name == "let":
                self.form = Let()
            elif self.car.name == "cond":
                self.form = Cond()
            elif self.car.name == "define":
                self.form = Define()
            elif self.car.name == "set!":
                self.form = Set()
            else:
                self.form = Regular()
        else:
            self.form = Regular()

    def print(self, n, p=False):
        self.form.print(self, n, p)

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr


if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
