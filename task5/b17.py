#!/bin/python3

import math
import os
import random
import re
import sys





first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

transponded = "".join([matrix[j][i] for i in range(m) for j in range(n)])

ending = re.search("[^a-zA-Z0-9]*$", transponded).group()[1:]
middle = re.sub("[^a-zA-Z0-9]+", " ", transponded).strip()
begining = re.search("^[^a-zA-Z0-9]*", transponded).group()[:-1]

result = ""
result += begining
result += middle
result += ending

print(result)
