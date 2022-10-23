import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
num = [i for i in range(1, n+1)]
num = list(permutations(num, m))

for i in num:
    for j in i:
        print(j, end=' ')
    print()