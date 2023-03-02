'''Write a script that accepts two command line arguments and checks that exactly two
command line arguments are passed, no less or no more, and that the first argument is an
integer and the second is a string. Make useful feedback if they are not.'''

import sys

try:
    if(len(sys.argv)==3 and isinstance(int(sys.argv[1]), int)):
        print("Arguments are totally fine!")
    elif(len(sys.argv)!=3):
        print("Arguments are not 2 in number!")
except ValueError:
    print("First argument is not an integer!")