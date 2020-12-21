#!/usr/bin/env python3

import sys
from mt19937 import mt19937, untemper


if __name__ == '__main__':
    # create our own version of an MT19937 PRNG.
    myprng = mt19937(0)

    # here are the random numbers generated in the snowball game
    with open(sys.argv[1], 'r') as file:
        numbers = [int(x) for x in file.readlines()]

    # clone the prng
    for i in range(mt19937.n):
        myprng.MT[i] = untemper(numbers[i])
    
    # predict the seed for the game
    print(myprng.extract_number())
    print(myprng.extract_number())