#ex2c
from random import *

def arn(n):

    b = {0 : "A", 1 : "U", 2 : "G", 3 : "C"}
    mylist = []
    for i  in range(n):
        mylist.append((b[randint(0, 3)], b[randint(0, 3)], b[randint(0, 3)]))

    return mylist
