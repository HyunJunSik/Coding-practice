import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    num[i] = num[i] + num[i - 1]
for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(num[j - 1])
    elif i == j:
        print(num[i - 1] - num[i - 2])
    else:
        print(num[j - 1] - num[i - 2])
    