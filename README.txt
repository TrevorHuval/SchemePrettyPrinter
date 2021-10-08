Blake Lalonde & Trevor Huval
CSC 4101 | Project 1 | Pretty Printer

We designed our program to sift through the input stream and separate each character into its according token.
From there we used Parser.py to parse token by token and connect them to cons nodes accordingly, sending them to Cons.py.
In Cons, we dictate whether or not it is a special identifier token and if so, we send it to the according .py file to print that specific function out how it should be.
This process repeats until all the tokens are printed out.

From the somewhat basic tests that were provided and that we've fabricated and run everything seems to be working fine.
