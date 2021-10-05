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

from Tokens.IdentToken import IdentToken
from Tree import *
from Tokens import *
from Parse.Scanner import Scanner
import sys
from Tokens import TokenType
from Tree import BoolLit


class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        # HOPEFULLY: write code for parsing an exp
        tok = Scanner.getNextToken(self.scanner)
        return self.__parseExp(tok)

    def __parseExp(self, tok):

        if tok.getType() == None:
            return None
        elif tok.getType() == TokenType.LPAREN:
            return self.parseRest()
        elif tok.getType() == TokenType.FALSE:
            return BoolLit.getInstance(False)
        elif tok.getType() == TokenType.TRUE:
            return BoolLit.getInstance(True)
        elif tok.getType() == TokenType.QUOTE:
            return Cons(Ident("quote"), Cons(self.parseExp(), Nil.getInstance()))
        elif tok.getType() == TokenType.INT:
            return IntLit(IntToken.getIntVal(tok))
        elif tok.getType() == TokenType.STR:
            return StrLit(StrToken.getStrVal(tok))
        elif tok.getType() == TokenType.IDENT:
            return Ident(IdentToken.getName(tok))
        return None

    def parseRest(self):
        # HOPEFULLY: write code for parsing a rest
        tok = Scanner.getNextToken(self.scanner)
        return self.__parseRest(tok)

    def __parseRest(self, tok):
        # If current token is right paren
        if Token.getType(tok) == None:
            return None

        elif Token.getType(tok) == TokenType.RPAREN:
            return Nil.getInstance()

        # else, current token is an expression
        elif Token.getType(tok) == TokenType.DOT:
            return Cons(self.__parseExp(tok), self.parseExp())

        else:
            return Cons(self.__parseExp(tok), self.parseRest())
        # else:
        #    # If current token is a dot
        #    if tok.getType() == TokenType.DOT:
        #        return Cons(self.__parseExp(tok), self.parseExp())
        #    else:
        #        return Cons(self.__parseExp(tok), self.parseRest())

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
