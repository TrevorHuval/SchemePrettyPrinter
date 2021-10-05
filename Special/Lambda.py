# Lambda -- Parse tree node strategy for printing the special form lambda

from Special import Special


class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        if p == False:
            print("(")
        else:
            print("lambda")
        t.cdr
        # TODO: Implement this function.
        pass

#   (lambda (x y)
#       (...)
#   )
#
#
#
