# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

from Tree import Cons
import sys
from Tokens import TokenType
from Tree import BoolLit
from Tree import StrLit
from Tree import IntLit
from Tree import Ident
from Tree import Nil


class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        # HOPEFULLY: write code for parsing an exp
        print("parsing")
        tok = self.scanner.getNextToken()
        return self.__parseExp(tok)

    def __parseExp(self, tok):
        #print("made it to __parseExp")
        if tok == None:
            return None
        elif tok.getType() == TokenType.LPAREN:
            print("token is: (")
            self.parseRest()
        elif tok.getType() == TokenType.FALSE:
            print("token is: #f")
            return BoolLit.getInstance(False)
        elif tok.getType() == TokenType.TRUE:
            print("token is: #t")
            return BoolLit.getInstance(True)
        elif tok.getType() == TokenType.QUOTE:
            print("token is: '")
            self.parseExp()
        elif tok.getType() == TokenType.INT:
            print("token is: ", tok.getIntVal())
            return IntLit(tok.getIntVal())
        elif tok.getType() == TokenType.STR:
            print("token is: ", tok.getStrVal())
            return StrLit(tok.getStrVal())
        elif tok.getType() == TokenType.IDENT:
            print("token is: ", tok.getName())
            return Ident(tok.getName())

        return None

    def parseRest(self):
        # TODO: write code for parsing a rest
        #print("made it to parseRest")
        tok = self.scanner.getNextToken()
        return self.__parseRest(tok)

    def __parseRest(self, tok):
        #print("made it to __parseRest")

        # If current token is right paren
        if tok.getType() == TokenType.RPAREN:
            print("token is: )")
            return Nil.getInstance()

        # else, current token is an expression
        else:
            # self.__parseExp(tok)
            #tok = self.scanner.getNextToken()
            # If current token is a dot
            if tok.getType() == TokenType.DOT:
                print("token is: .")
                # self.parseExp()
                return Cons(self.__parseExp(tok), self.parseRest())
            else:
                #print("is an exp")
                # self.__parseRest(tok)
                return Cons(self.__parseExp(tok), self.parseRest())

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
