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

    def isLetter(ch):
        return ch >= 'a' and ch<= 'z'

    def isSpecialInitial(ch):
        return ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '`'
    
    def isSpecialSub(ch):
        return ch == '+' or ch == '-' or ch == '.' or ch == '@'

    def isPeculiarIdentifier(ch):
        return ch == '+' or ch == '-'

    def isInitial(ch):
        return isLetter(ch) or isSpecialInitial(ch)

    def isSubsequent(ch):
        return isInitial(ch) or isDigit(ch) or isSpecialSub(ch)


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
                if(ch == ' ' or '\t' or '\r' or '\n'):
                    return self.getNextToken()
                elif(ch == ';'):
                    commentLoop = False
                    while(commentLoop == False):
                        ch = self.read()
                        if(ch == '\r' or '\n'):
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
                i = 0
                # HOPEFULLY: scan a string into the buffer variable buf
                stringLoop = False
                while (stringLoop == False):
                    if (ch != '"'):
                        self.buf.append(ch)
                        ch = self.read()
                    else:
                        stringLoop = True
    
                return StrToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')
                # HOPEFULLY: scan the number and convert it to an integer
                previous = 0
                intLoop = False
                while (intLoop == False):
                    if (ch.isDigit()):
                        previous = ((previous * 10) + i)                        
                    else:
                        intLoop == False

                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(previous)
    
            # Identifiers
            elif ((ch >= 'A' and ch <= 'Z') or isInitial(ch) or isPeculiarIdentifier(ch)):
                # or ch is some other valid first character
                # for an identifier
                self.buf = []
                i = 0
                if isInitial(ch):
                    self.buf.append(ch)
                    while(isSubsequent(ch)):
                        self.buf.append(ch)
                elif isPeculiarIdentifier(ch):
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
