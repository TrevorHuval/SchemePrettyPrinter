# Ident -- Parse tree node class for representing identifiers

import sys
from Tree import Node


class Ident(Node):
    def __init__(self, n):
        self.name = n

    def print(self, n, p=False):
        # There got to be a more efficient way to print n spaces.
        for _ in range(n):
            sys.stdout.write(' ')
            sys.stdout.flush()
        sys.stdout.write(self.name)
        sys.stdout.flush()

    def isSymbol(self):
        return True

    def getName(self):
        return self.name


if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
