#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    sum_alice = 0
    sum_bob = 0
    try:
        alice_scores = [int(i) for i in a.strip(' ').split()]
        bob_scores = [int(i) for i in b.strip(' ').split()]
    except TypeError:
        return ("Did not enter integer")
    
    if len(alice_scores) == len(bob_scores) and len(alice_scores) == 3:
        for i in range(0, 3):
            if alice_scores[i] > bob_scores[i]:
                sum_alice += 1
            elif alice_scores[i] < bob_scores[i]:
                sum_bob += 1
        return [sum_alice, sum_bob]


a = input()
b = input()
# a = list(map(int, input().rstrip().split()))
# b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(result)

  

 
