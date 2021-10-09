Blake Lalonde & Trevor Huval
CSC 4101 | Project 1 | Pretty Printer

    We designed our program to first utilize the Scanner.py to sift character by character through the input stream and assign each to its according
token type value.  Once it is finished it goes to the Parser.py to create nodes based off of those tokens to build the parse tree.

    Cons.py is used as a bridge to other files for special identifiers to print out their functions in their unique correct format in terms of line usage and indentation.
If the node is not a special identifier, or an identifier at all, it goes directly to Special.py where it is printed accordingly.  Each document has its own if statements
to decide what to do based on previous outputs thus far (i.e. whether or not a left parentheses has been printed).  This process will continue over and over until
all of the nodes have been printed our an error in the input has been hit.

    From the tests that we've ran everything seems to be fine except for dealing with quote.  '(1 2 3) and quote(1 2 3) both print out '(1 2 3).  However; whenever we
try to throw a parentheses before the quote, it separates the rest of the list -->    ('(1 2 3)) or (quote(1 2 3)) = ('1 (2 3)).  Instead of keeping it as an entire list it
breaks it up.  We recognized this error just now but ran out of time to track down exactly what is causing it.  We believe it is in Parser.py, more specifically in __parseRest and 
its handling of left parentheses. 