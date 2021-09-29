# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *


class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch

    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    @staticmethod
    def isLetter(ch):
        return ch >= 'a' and ch <= 'z'

    @staticmethod
    def isSpecialInitial(ch):
        return ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '`'

    @staticmethod
    def isSpecialSub(ch):
        return ch == '+' or ch == '-' or ch == '.' or ch == '@'

    @staticmethod
    def isPeculiarIdentifier(ch):
        return ch == '+' or ch == '-'

    @staticmethod
    def isInitial(ch):
        # return ch.isLetter() or ch.isSpecialInitial()
        return (ch >= 'a' and ch <= 'z') or (ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '`')

    @staticmethod
    def isSubsequent(ch):
        # return ch.isIntial() or ch.isDigit() or ch.specialSub()
        return ((ch >= 'a' and ch <= 'z') or (ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '`')) or (ch >= '0' and ch <= '9') or (ch == '+' or ch == '-' or ch == '.' or ch == '@')

    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            # HOPEFULLY: Skip white space and comments
            loopBool = False
            while(loopBool == False):
                if(ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n'):
                    return self.getNextToken()
                elif(ch == ';'):
                    commentLoop = False
                    while(commentLoop == False):
                        ch = self.read()
                        if(ch == '\r' or ch == '\n'):
                            commentLoop = True
                            return self.getNextToken()
                else:
                    loopBool = True

            # Return None on EOF
            if ch == "":
                return None

            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '"':
                self.buf = []
                # HOPEFULLY: scan a string into the buffer variable buf
                stringLoop = False
                while (stringLoop == False):
                    ch = self.read()
                    if (ch != '"'):
                        self.buf.append(ch)
                    else:
                        stringLoop = True

                return StrToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')

                # HOPEFULLY: scan the number and convert it to an integer
                curVal = i
                intLoop = False
                while (intLoop == False):
                    if (self.isDigit(self.peek())):
                        ch = self.read()
                        i = ord(ch) - ord('0')
                        curVal = (curVal * 10) + i
                    else:
                        intLoop = True

                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(curVal)

            # Identifiers
            elif ((ch >= 'A' and ch <= 'Z') or self.isInitial(ch) or self.isPeculiarIdentifier(ch)):
                # or ch is some other valid first character
                # for an identifier
                self.buf = []

                if self.isInitial(ch):
                    self.buf.append(ch)
                    ch = self.read()
                    while(self.isSubsequent(ch)):
                        self.buf.append(ch)
                        if(self.isSubsequent(self.peek())):
                            ch = self.read()
                        else:
                            break
                elif self.isPeculiarIdentifier(ch):
                    self.buf.append(ch)

                # HOPEFULLY: scan an identifier into the buffer variable buf

                # make sure that the character following the identifier
                # is not removed from the input stream
                return IdentToken("".join(self.buf))

            # Illegal character
            else:
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
