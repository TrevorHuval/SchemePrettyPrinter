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

from Tree import *
from Tokens import *
from Parse.Scanner import Scanner
import sys


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
            tempToken = Scanner.getNextToken(self.scanner)
            if tempToken.getType() == TokenType.DOT:
                sys.stdout.write("parse error: illegal dot \n")
                return self.parseExp()
            return self.__parseRest(tempToken)

        elif tok.getType() == TokenType.FALSE:
            return BoolLit.getInstance(False)

        elif tok.getType() == TokenType.TRUE:
            return BoolLit.getInstance(True)

        elif tok.getType() == TokenType.QUOTE:
            return Cons(Ident("'"), self.parseExp())

        elif tok.getType() == TokenType.INT:
            return IntLit(IntToken.getIntVal(tok))

        elif tok.getType() == TokenType.STR:
            return StrLit(StrToken.getStrVal(tok))

        elif tok.getType() == TokenType.IDENT:
            return Ident(IdentToken.getName(tok))

        elif tok.getType() == TokenType.RPAREN:
            return self.parseExp()

        elif tok.getType() == TokenType.DOT:
            return self.parseExp()

        return None

    def parseRest(self):
        # HOPEFULLY: write code for parsing a rest
        tok = Scanner.getNextToken(self.scanner)
        return self.__parseRest(tok)

    def __parseRest(self, tok):

        if tok == None:
            return None
        if tok.getType() == TokenType.RPAREN:
            return Nil.getInstance()
        tnext = Scanner.getNextToken(self.scanner)
        if tok.getType() == TokenType.LPAREN:
            if tnext == None:
                return None
            if tnext.getType() == TokenType.RPAREN:
                return Cons(Nil.getInstance(), self.parseRest())
            elif tnext.getType() == TokenType.DOT:
                return self.parseExp()
            else:
                return Cons(Cons(self.__parseExp(tnext), self.parseRest()), self.parseRest())
        elif tnext.getType() == TokenType.RPAREN:
            return Cons(self.__parseExp(tok), Nil.getInstance())
        elif tok.getType() == TokenType.DOT:
            tempNode = self.__parseExp(tnext)
            Scanner.getNextToken(self.scanner)
            return tempNode
        elif tnext.getType() == TokenType.DOT:
            tempNode = Cons(self.__parseExp(tok), self.parseExp())
            Scanner.getNextToken(self.scanner)
            return tempNode
        else:
            return Cons(self.__parseExp(tok), Cons(self.__parseExp(tnext), self.parseRest()))

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
