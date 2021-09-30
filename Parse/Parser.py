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

import sys
from Tokens import TokenType
from Tree import BoolLit
from Tree import StrLit
from Tree import IntLit
from Tree import Ident

class Parser:
    def __init__(self, s):
        self.scanner = s



    def parseExp(self):
        # TODO: write code for parsing an exp
        tok = self.scanner.getNextToken()
        return self.__parseExp(tok)

    def __parseExp(self, tok):
        if tok == None:
            return None
        elif tok.getType() == TokenType.LLPAREN:
            self.parseRest(tok)
        elif tok.getType() == TokenType.FALSE:
            return BoolLit.getInstance(False)
        elif tok.getType() == TokenType.TRUE:
            return BoolLit.getInstance(True)
        elif tok.getType() == TokenType.QUOTE:
            self.parseExp(tok)
        elif tok.getType() == TokenType.INT:
            return IntLit(tok.getIntVal())
        elif tok.getType() == TokenType.STR:
            return StrLit(tok.getStrVal())
        elif tok.getType() == TokenType.IDENT:
            return Ident(tok.getName())


        return None

    def parseRest(self, tok):
        # TODO: write code for parsing a rest
        if tok.getType() == TokenType.RPAREN:
            return new Nil()
        else:
            
        return None

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
